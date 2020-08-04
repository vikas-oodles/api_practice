from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    street_address = models.CharField(max_length=100)
    city_name = models.CharField(max_length=50, blank=True)
    state_name = models.CharField(max_length=50, blank=False)
    pin_code = models.PositiveIntegerField()
    country_name = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.street_address

class Profile(models.Model):

    Male = 'Male'
    Female = 'Female'
    Other = 'Other'
    

    choices = (
        (Male,'male'),
        (Female,'female'),
        (Other,'other'),
    )

    user = models.OneToOneField(User, related_name='profiles', on_delete=models.CASCADE)
    phone_number = models.PositiveIntegerField(unique=True, blank=False)
    gender = models.CharField(max_length=15,choices=choices,default=Male, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    date_of_birth = models.DateTimeField(blank=True)
    permanent_address = models.ForeignKey(Address,related_name='permanent_address', on_delete=models.CASCADE)
    company_address = models.ForeignKey(Address,related_name='company_address',on_delete=models.CASCADE)
    user_friend = models.ManyToManyField(User,related_name='friends')

    def __str__(self):
        return self.user.username

