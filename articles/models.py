from django.db import models
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field


    
class Post(models.Model):
    class PublishedManager(models.Model):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='uploads/articles/%Y/%m/%d')
    body = CKEditor5Field('Text', config_name='extends')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    
    object = models.Manager() # default manager
    published = PublishedManager() # custom Manager
    

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ('-publish',)

    def __str__(self):
        """Unicode representation of MODELNAME."""
        return self.title

