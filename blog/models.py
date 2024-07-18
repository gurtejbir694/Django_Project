from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    answer = models.CharField(default=False, max_length=200)
    
    def __str__(self):
        return self.email
    
    
class registration(models.Model):
    first_name = models.CharField(default=False, max_length=200)
    last_name = models.CharField(default=False, max_length=200)
    userid = models.CharField(default=False, max_length=50)
    email_id = models.CharField(default=False, max_length=100)
    password = models.CharField(default=False, max_length=100)
        
    def __str__(self):
        return self.first_name

class categories(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='upload/')
    
    def __str__(self):
        return self.name

class product(models.Model):
    cat = models.ForeignKey(categories, on_delete=models.CASCADE)
    name = models.CharField(default=False, max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='upload/')
    author = models.CharField(default=False, max_length=40)
    description=models.CharField(default=False, max_length=1000)
    
    def __str__(self):
        return self.name
    
class author(models.Model):
    name = models.CharField(default=False, max_length=100)
    image = models.ImageField(upload_to='author_profile/')
    about = models.CharField(default=False, max_length=3000)
    
    def __str__(self):
        return self.name



class FreeBooks(models.Model):
    name = models.CharField(default=False, max_length=100)
    image = models.ImageField(upload_to='free_books/')
    pdf = models.FileField(upload_to='books_file/')
    
    def __str__(self):
        return self.name    