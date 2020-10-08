from django.conf import settings
from django.db import models
from django.utils import timezone

class Post3(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    short_text = models.TextField()
    img = models.ImageField(upload_to='images/', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    @property
    def img_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def image_img(self):
        if self.img:
            return u'< img src="%s" width="100"/>' % self.imgfile.url
        else:
            return '(none)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
