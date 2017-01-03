from django.db import models
from django.utils import timezone

# Create your models here.
class SalePost(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    age = models.IntegerField()
    original_price = models.IntegerField()
    quoted_price = models.IntegerField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    shipping = models.CharField(max_length=20)
    bill = models.CharField(max_length=20)
    negotiable = models.CharField(max_length=20)
    other_details = models.CharField(max_length=20)
    published_date = models.DateTimeField(blank=True, null=True)
    #picture = models.ImageField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



