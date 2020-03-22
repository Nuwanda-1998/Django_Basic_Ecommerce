from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class UserProfileInfo(models.Model):
    
#     user = models.OneToOneField(User)
#     #additional classes
#     portfolio_site = models.URLField(blank=True)

#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
#     def __str__(self):
#         return self.user.username


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)
    user_job = models.CharField(max_length=120)
    national_id = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class PCategory(models.Model):
    cat_name = models.CharField(max_length=100)

    def __str__(self):
        return self.cat_name

class Products(models.Model):
    category = models.ForeignKey(PCategory, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.product_name