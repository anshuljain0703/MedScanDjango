from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    ROLE_CHOICES = (
        ('PATIENT', 'Patient'),
        ('DOCTOR', 'Doctor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class MedicalReport(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="patient_reports"
    )
    predicted_disease = models.CharField(max_length=100)
    confidence = models.FloatField()
    report_file = models.FileField(upload_to="reports/")
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Doctor Verification
    is_verified = models.BooleanField(default=False)
    verified_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="verified_reports"
    )
    doctor_comments = models.TextField(blank=True, null=True)
    verification_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} - {self.predicted_disease}"
