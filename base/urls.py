from django.urls import path
from .views import create_folder, folder_detail, upload_photo

urlpatterns = [
    path('create_folder/', create_folder, name='create_folder'),
    path('folder/<int:folder_id>/', folder_detail, name='folder_detail'),
    path('folder/<int:folder_id>/upload_photo/', upload_photo, name='upload_photo'),
    
]
