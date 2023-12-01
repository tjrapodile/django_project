from django.urls import path
from .views import upload_csv,upload_success

urlpatterns = [
    path('upload/', upload_csv, name='upload_csv'),
    path('upload_success/', upload_success, name='upload_success'),
]


