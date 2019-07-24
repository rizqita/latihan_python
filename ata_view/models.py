from django.db import models

# Create your models here.
class Mentor(models.Model):   
    nama=models.CharField(max_length=255)
    gambar=models.CharField(max_length=255)
    jabatan=models.CharField(max_length=255)
    durasi=models.IntegerField()
    quote=models.TextField()
    def __str__(self):
        return self.nama
        # return self.gambar
        # return self.jabatan
        # return self.durasi
        # return self.quote
class Mentee(models.Model):   
    nama=models.CharField(max_length=255)
    gambar=models.CharField(max_length=255)
    quote=models.TextField()
    def __str__(self):
        return self.nama
        # return self.gambar
        # return self.jabatan
        # return self.durasi
        # return self.quote
class Blog(models.Model):
    judul=models.CharField(max_length=255)
    gambar=models.CharField(max_length=255)
    isi=models.TextField()
    date =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.judul