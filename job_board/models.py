from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Company(models.Model):
    companyName=models.CharField(max_length=100)
    companyDescription=models.TextField()
    companyIndustry=models.CharField(max_length=50)
    companyLocation=models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.companyName
    

class Job(models.Model):
    jobTitle=models.CharField(max_length=300)
    jobDescription=models.TextField()
    jobCompany=models.ForeignKey(Company, on_delete=models.CASCADE)
    jobSalary=models.IntegerField()
    jobWorkTime=models.CharField(max_length=50)
    jobType=models.CharField(max_length=50)
    jobSkills=models.TextField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
