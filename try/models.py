from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=200)
    number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254)
    message = models.CharField(max_length=20000)

    def __str__(self):
        return f"'{self.Name}' messaged '{self.message}'"

class Direct(models.Model):
    number = models.CharField(max_length=20, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number} contacted on {self.date}"


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title