from django.db import models
from django.contrib.auth.models import User

class Special(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default='special service')
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Services(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(default='service')
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Attribute(models.Model):
    name = models.CharField(max_length=100)
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)

class Price(models.Model):
    name = models.CharField(max_length=100)
    fee = models.FloatField(default=100)
    attribute = models.ManyToManyField(Attribute)
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('created_at',)
        
class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    statue = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ('created_at',)
        
class Skills(models.Model):
    name = models.CharField(max_length= 100)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.name
    
    class Mata:
        ordering = ('created_at',)
        
class Trainers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='trainers',default= 'unknown.jpg')
    skills = models.ManyToManyField(Skills)
    content = models.TextField('good teacher')
    status = models.BooleanField(default= False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    
    def __str__(self):
        return self.user.username
    
    class Mata:
        ordering = ('created_at',)
        
        
