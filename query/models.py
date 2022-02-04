from django.db import models
from django.utils import timezone

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

'''
# To implement
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50, default=None, null=True)
    email = models.EmailField(default=None, null=True)
    
    date = models.DateTimeField('date published', default=timezone.now)
    

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]


class Guide(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    query = models.CharField(max_length=1000, blank=False)
    email = models.EmailField(default=None, null=True)

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]


class Tourist(models.Model):
    id = models.AutoField(primary_key=True)
    #user = User
    date = models.DateTimeField('date published', default=timezone.now)
    title = models.CharField(max_length=100, blank=True, null=True)
    query = models.CharField(max_length=1000, blank=False)
    email = models.EmailField(default=None, null=True)

    def __str__(self):
        return f"{self.title}: {self.query}"

    class Meta:
        ordering = ["-id"]'''
