from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("signup", views.signup, name="signup"),
  path("signin", views.signin, name="signin"),
  path("signout", views.signout, name="signout"),
  path("activate/<uidb64>/<token>", views.activate, name="activate"),
  path("view", views.show_file, name="view"),
  path("upload", views.upload, name="upload"),
  path("files/", views.file_list, name="file_list"),
  path("files/upload", views.upload_file, name="upload_file"),
  path("files/<int:pk>/", views.delete_file, name="delete_file"),
  path("class/files/", views.FileListView.as_view(), name="class_file_list"),
  path("class/files/upload", views.UploadFileView.as_view(), name="class_upload_file"),


]