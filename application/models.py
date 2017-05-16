from django.db import models

class Address(models.Model):
    COUNTRY_CHOICES = (
        ('AU', 'Australia'),
        ('CN', 'China'),
        ('US', 'United States')
    )
    address_line = models.CharField(max_length=250)
    suburb = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50,choices = COUNTRY_CHOICES)
    post_code = models.CharField(max_length=10)

    def __str__(self):
        return self.address_line

class Applicant(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    income = models.DecimalField(max_digits=15,decimal_places=2)
    address = models.ManyToManyField(Address, related_name='appaddress')

    def __str__(self):
        return self.first_name + ',' + self.last_name
