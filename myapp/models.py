from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Notes(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1500, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    submitted_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
