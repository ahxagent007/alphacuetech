from django.db import models


class Legends(models.Model):
    L_id = models.AutoField(primary_key=True)
    L_name = models.CharField(max_length=200)
    L_codeName = models.CharField(max_length=100, unique=True)
    L_title = models.CharField(max_length=100)
    L_email = models.EmailField()
    L_phone = models.CharField(max_length=100)
    L_website = models.CharField(max_length=100)
    L_address = models.CharField(max_length=200)
    L_intro = models.CharField(max_length=200)
    L_introDes = models.CharField(max_length=1000)
    L_proPic = models.CharField(max_length=200)
    L_FB = models.CharField(max_length=100)
    L_Instagram = models.CharField(max_length=100)
    L_LinkedIn = models.CharField(max_length=100)
    L_GitHub = models.CharField(max_length=100)

class WorkExperience(models.Model):
    WE_id = models.AutoField(primary_key=True)
    L_id = models.ForeignKey(Legends, on_delete=models.CASCADE)
    WE_title = models.CharField(max_length=100)
    WE_companyName = models.CharField(max_length=100)
    WE_from = models.CharField(max_length=10)
    WE_to = models.CharField(max_length=10)
    WE_Details = models.CharField(max_length=300)

class Education(models.Model):
    L_id = models.ForeignKey(Legends, on_delete=models.CASCADE)
    E_title = models.CharField(max_length=100)
    E_name = models.CharField(max_length=100)
    E_from = models.CharField(max_length=10)
    E_to = models.CharField(max_length=10)
    E_details = models.CharField(max_length=300)
    E_id = models.AutoField(primary_key=True)

class Skills(models.Model):
    L_id = models.ForeignKey(Legends, on_delete=models.CASCADE)
    S_id = models.AutoField(primary_key=True)
    S_name = models.CharField(max_length=100)
    S_power = models.IntegerField()

class Works(models.Model):
    L_id = models.ForeignKey(Legends, on_delete=models.CASCADE)
    W_id = models.AutoField(primary_key=True)
    W_name = models.CharField(max_length=100)
    W_skill = models.CharField(max_length=100)
    W_link = models.CharField(max_length=300)
    W_pic = models.CharField(max_length=100)