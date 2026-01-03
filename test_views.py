import os
import django
from django.test import Client, RequestFactory
from django.urls import reverse

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medscan_project.settings')
django.setup()

from django.contrib.auth.models import User
from scanner.models import Profile, MedicalReport

print("-" * 30)
print("TESTING VIEWS FOR ERRORS")
print("-" * 30)

client = Client()

# 1. Test Login/Home
try:
    print("Testing Home Page (Patient)...")
    user = User.objects.get(username='testpatient')
    client.force_login(user)
    response = client.get(reverse('home'))
    if response.status_code == 200:
        print("✅ Home Page OK")
    else:
        print(f"❌ Home Page FAILED: {response.status_code}")
except Exception as e:
    print(f"❌ Home Page Error: {e}")

# 2. Test Doctor Dashboard
try:
    print("\nTesting Doctor Dashboard...")
    # Get or create doctor
    try:
        doctor = User.objects.get(username='raha')
    except User.DoesNotExist:
        doctor = User.objects.create_user('doc_test', 'doc@test.com', 'password')
        Profile.objects.create(user=doctor, role='DOCTOR')
    
    client.force_login(doctor)
    response = client.get(reverse('doctor_dashboard'))
    if response.status_code == 200:
        print("✅ Dashboard OK")
    else:
        print(f"❌ Dashboard FAILED: {response.status_code}")
except Exception as e:
    print(f"❌ Dashboard Error: {e}")

# 3. Test Verify Page
try:
    # ensure a report exists
    reports = MedicalReport.objects.all()
    if reports.exists():
        report = reports.first()
        print(f"\nTesting Verify Page for Report ID {report.id}...")
        response = client.get(reverse('verify_report', args=[report.id]))
        if response.status_code == 200:
            print("✅ Verify Page OK")
        else:
            print(f"❌ Verify Page FAILED: {response.status_code}")
    else:
        print("\n⚠️ No reports to test verification.")
except Exception as e:
    print(f"❌ Verify Page Error: {e}")
