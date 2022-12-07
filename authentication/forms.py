from django import forms 

from .models import Files

class AuthenticationUploadForm(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))

class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ("title", "data", "cover")