# \




# from django.urls import path
# from .views import home
# from django.conf import settings
# from django.conf.urls.static import static



# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     path('', home),
   
# ]
from django.urls import path
from .views import home, signup_view, login_view, logout_view, doctor_dashboard, verify_report
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('verify/<int:report_id>/', verify_report, name='verify_report'),
]

# serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
