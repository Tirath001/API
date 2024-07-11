from django.db import models

class Services(models.Model):
    title = models.CharField(max_length=200)  
    detail = models.TextField()
    Page_detail_content = models.TextField()  
    image = models.ImageField(upload_to='services_images/', blank=True, null=True)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-id'] 

    def __str__(self):
        return self.title
    
class industries(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField() 
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='services_images/', blank=True, null=True) 
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Industries'
        verbose_name_plural = 'Industries'
        ordering = ['-id'] 

    def __str__(self):
        return self.title
    

class ARFeature(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='ar_features/', blank=True, null=True) 
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'AR Feature'
        verbose_name_plural = 'AR Features'
        ordering = ['-id']
    def __str__(self):
        return self.title


class ARBenefit(models.Model):
    title = models.CharField(max_length=200) 
    detail = models.TextField() 
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='ar_benefits/', blank=True, null=True)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'AR Benefit'
        verbose_name_plural = 'AR Benefits'
        ordering = ['-id']

    def __str__(self):
        return self.title


class ARCaseStudy(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='ar_case_studies/', blank=True, null=True)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'AR Case Study'
        verbose_name_plural = 'AR Case Studies'
        ordering = ['-id']

    def __str__(self):
        return self.title
    

class Home_CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='Home_CaseStudy/', blank=True, null=True)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Home Case Study'
        verbose_name_plural = 'Home Case Studies'
        ordering = ['-id']
    def __str__(self):
        return self.title
    
class Home_services(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='Home_services/', blank=True, null=True)
    float_icon=models.CharField(max_length=200)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Home Services'
        verbose_name_plural = 'Home Services'
        ordering = ['-id']

    def __str__(self):
        return self.title

class Blogs(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField()
    Page_detail_content = models.TextField()
    image = models.ImageField(upload_to='Blogs/', blank=True, null=True)
    meta_tag = models.SlugField(max_length=200)
    class Meta:
        verbose_name = 'Blogs'
        verbose_name_plural = 'Blogs'
        ordering = ['-id'] 

    def __str__(self):
        return self.title
    
