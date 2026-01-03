import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medscan_project.settings')
django.setup()

from django.contrib.auth.models import User
from scanner.models import Profile, MedicalReport

print("-" * 30)
print("CHECKING DATABASE STORAGE")
print("-" * 30)

# Check Users
users = User.objects.all()
print(f"Total Users Found: {users.count()}")
for user in users:
    role = "No Profile"
    if hasattr(user, 'profile'):
        role = user.profile.role
    print(f"User: {user.username} | Role: {role} | Email: {user.email}")

print("\n" + "-" * 30)

# Check Reports
reports = MedicalReport.objects.all()
print(f"Total Medical Reports Found: {reports.count()}")
for report in reports:
    print(f"Report ID: {report.id} | Patient: {report.patient.username} | Disease: {report.predicted_disease} | File: {report.report_file}")

print("-" * 30)
