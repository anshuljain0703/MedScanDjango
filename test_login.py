import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'medscan_project.settings')
django.setup()

from django.test import Client, RequestFactory
from django.contrib.auth.models import User
from scanner.models import Profile, MedicalReport

# Setup
client = Client()

def test_signup_and_login():
    print("--- Testing Signup ---")
    # Patient Signup
    response = client.post('/signup/', {
        'username': 'testpatient',
        'email': 'patient@test.com',
        'password': 'password123',
        'confirm_password': 'password123',
        'role': 'PATIENT'
    })
    
    if response.status_code == 302:
        print(f"Signup Redirects to: {response.url}")
        if response.url == '/' or response.url == '/dashboard/': # depending on logic
             print("Signup Successful (Redirected)")
    else:
        print(f"Signup Failed. Status: {response.status_code}")
        # print form errors if context exists
        if response.context and 'form' in response.context:
             print(f"Form Errors: {response.context['form'].errors}")
        elif response.context: 
             # Context is a list of dicts, search in last one
             for ctx in reversed(response.context):
                 if 'form' in ctx:
                     print(f"Form Errors: {ctx['form'].errors}")
                     break

    # Check User created
    try:
        user = User.objects.get(username='testpatient')
        print(f"User created: {user.username}, Role: {user.profile.role}")
    except User.DoesNotExist:
        print("User NOT created!")

    print("\n--- Testing Login ---")
    # Patient Login
    response = client.post('/login/', {
        'username': 'testpatient',
        'password': 'password123'
    })
    
    if response.status_code == 302:
         print(f"Login Redirects to: {response.url}")
    else:
         print(f"Login Failed. Status: {response.status_code}")
         if response.context:
             for ctx in reversed(response.context):
                 if 'form' in ctx:
                     print(f"Form Errors: {ctx['form'].errors}")
                     break

if __name__ == "__main__":
    # Clean up old test user
    User.objects.filter(username='testpatient').delete()
    test_signup_and_login()
