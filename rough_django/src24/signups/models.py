from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.


class SignUp(models.Model):
    for_you = models.BooleanField(default=True,verbose_name="Is this purchase for you? If so, check the box ")
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode("-> " + self.email)
