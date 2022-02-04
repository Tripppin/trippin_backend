from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from languages.fields import LanguageField

from django.contrib.postgres.fields import ArrayField




class Query(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    query = models.CharField(max_length=1000, blank=False)
    email = models.EmailField(default=None, null=True)

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]


# To implement
class Homestay(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #department = models.CharField(max_length=100)
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    services = ArrayField(models.CharField(max_length=50, default=None, null=True), default=None, null=True)
    
    location = models.CharField(max_length=50, default=None, null=True)
    phone_numbers = ArrayField(models.DecimalField(max_digits=10, decimal_places=0, default=0), default=None, null=True, db_index=True)
    languages = ArrayField(LanguageField(), default=None, null=True)
    
    email = models.EmailField(default=None, null=True)
    date = models.DateTimeField('date published', default=timezone.now)
    

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        ordering = ["-id"]


class Guide(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    query = models.CharField(max_length=1000, blank=False)
    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_numbers = ArrayField(models.DecimalField(max_digits=10, decimal_places=0, default=0), default=None, null=True, db_index=True)
    email = models.EmailField(default=None, null=True)
    
    nationality = models.CharField(max_length=50, default=None, null=True)
    languages = ArrayField(LanguageField(), default=None, null=True)

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]


class Tourist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #user = User
    
    
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_numbers = ArrayField(models.DecimalField(max_digits=10, decimal_places=0, default=0), default=None, null=True, db_index=True)
    email = models.EmailField(default=None, null=True)
    
    nationality = models.CharField(max_length=50, default=None, null=True)
    languages = ArrayField(LanguageField(), default=None, null=True)
    
    date = models.DateTimeField('date published', default=timezone.now)
    

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]
