from django.db import models

class Services(models.Model):
    # 'id' field is automatically added by Django as the primary key
    title = models.CharField(max_length=200)  # Title of the service
    detail = models.TextField()  # Detailed description of the service
    image = models.ImageField(upload_to='services_images/', blank=True, null=True)  # Image for the service

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['title']  # Order by title alphabetically

    def __str__(self):
        return self.title
    
class industries(models.Model):
    # 'id' field is automatically added by Django as the primary key
    title = models.CharField(max_length=200)  # Title of the service
    detail = models.TextField()  # Detailed description of the service
    image = models.ImageField(upload_to='services_images/', blank=True, null=True)  # Image for the service

    class Meta:
        verbose_name = 'Industries'
        verbose_name_plural = 'Industries'
        ordering = ['title']  # Order by title alphabetically

    def __str__(self):
        return self.title