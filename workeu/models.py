from django.db import models
from django.utils import timezone




class Post(models.Model): # Посты по Польше
    photo = models.ImageField("фотография", upload_to="workeu/media/photos/poland", default="", blank=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
		

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
	

class Postp(models.Model): # Посты по Прибалтике
    photo = models.ImageField("фотография", upload_to="workeu/media/photos/pribaltik", default="", blank=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
		

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title	
		
class Postf(models.Model): # Посты по Финляндии
    photo = models.ImageField("фотография", upload_to="workeu/media/photos/finland", default="", blank=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
		

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title		