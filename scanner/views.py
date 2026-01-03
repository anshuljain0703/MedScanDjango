from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .ml_model.predictor import predict_disease
from .utils.report_generator import generate_report
from .models import Profile, MedicalReport
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            # Create Profile
            Profile.objects.create(user=user, role=role)
            
            login(request, user)
            
            if role == 'DOCTOR':
                return redirect('doctor_dashboard')
            else:
                return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if hasattr(user, 'profile') and user.profile.role == 'DOCTOR':
                return redirect('doctor_dashboard')
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    # If a doctor tries to access home, redirect to dashboard
    if hasattr(request.user, 'profile') and request.user.profile.role == 'DOCTOR':
        return redirect('doctor_dashboard')

    result = None
    report_file = None
    confidence = 0.0
    disease = ""

    # Fetch user's history
    user_reports = MedicalReport.objects.filter(patient=request.user).order_by('-created_at')

    if request.method == "POST" and request.FILES.get("scan"):
        scan = request.FILES["scan"]

        fs = FileSystemStorage()
        filename = fs.save(scan.name, scan)
        image_path = fs.path(filename)

        disease, confidence = predict_disease(image_path)
        result = f"{disease} ({confidence:.2f}% confidence)"

        # Generate PDF report
        patient_name = request.user.get_full_name() if request.user.get_full_name() else request.user.username
        report_filename = generate_report(patient_name, filename, disease, confidence)
        report_file = report_filename # report_generator returns filename in media

        # Save to Database
        MedicalReport.objects.create(
            patient=request.user,
            predicted_disease=disease,
            confidence=confidence,
            report_file=report_filename 
        )
        
        # Refresh history
        user_reports = MedicalReport.objects.filter(patient=request.user).order_by('-created_at')

    return render(
        request,
        "home.html",
        {
            "result": result,
            "report_file": report_file,
            "user": request.user,
            "user_reports": user_reports
        }
    )

@login_required
def doctor_dashboard(request):
    # Ensure only doctors can access
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'DOCTOR':
        return redirect('home')

    reports = MedicalReport.objects.all().order_by('-created_at')
    
    return render(request, 'dashboard.html', {'reports': reports, 'user': request.user})

@login_required
def verify_report(request, report_id):
    # Ensure only doctors can access
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'DOCTOR':
        return redirect('home')

    report = get_object_or_404(MedicalReport, id=report_id)

    if request.method == "POST":
        comments = request.POST.get('doctor_comments')
        # Update Report
        report.is_verified = True
        report.verified_by = request.user
        report.doctor_comments = comments
        report.verification_date = timezone.now()
        report.save()
        return redirect('doctor_dashboard')

    return render(request, 'verify_report.html', {'report': report})
