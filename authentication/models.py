from django.db import models

# Create your models here.
class Files(models.Model):
    title = models.CharField(max_length=100)
    data = models.FileField(upload_to="")
    cover = models.ImageField(upload_to="", null=True, blank=True)

    def __str__(self):
        return self.title

class file_upload(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to="")

    def __str__(self):
        return self.file_name 
    
    def delete(self, *args, **kwargs):
        self.data.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


    # fileall = Files.objects.all()

    # for files in fileall:
    #     files.delete()
