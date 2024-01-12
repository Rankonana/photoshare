# photos/views.py
from django.shortcuts import render, redirect
from .models import Folder, Photo
from .forms import FolderForm, PhotoForm

def create_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save()
            # return redirect('base/folder_detail', folder_id=folder.id)
            return redirect('folder_detail', folder_id=folder.id)

    else:
        form = FolderForm()
    return render(request, 'base/create_folder.html', {'form': form})

def folder_detail(request, folder_id):
    print(request)
    print(folder_id)
    folder = Folder.objects.get(pk=folder_id)
    photos = Photo.objects.filter(folder=folder)
    return render(request, 'base/folder_detail.html', {'folder': folder, 'photos': photos})

def upload_photo(request, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.folder = folder
            photo.save()
            # return redirect('base/folder_detail', folder_id=folder.id)
            return redirect('folder_detail', folder_id=folder.id)
    else:
        form = PhotoForm()
    return render(request, 'base/upload_photo.html', {'form': form, 'folder': folder})
