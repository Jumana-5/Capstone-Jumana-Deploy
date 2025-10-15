from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class category(models.Model):
    category_id = models.BigAutoField(primary_key=True)
    category_name = models.CharField(max_length=100,unique=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.category_name


class item(models.Model):
    item_id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=100, null=False)
    is_used = models.BooleanField(default=False)
    price_in_JOD = models.IntegerField(null=True)

    #item_category = models.ForeignKey(category, on_delete=models.CASCADE)
    categories = models.ManyToManyField(category, related_name='items', default='other')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='items')

    item_image = models.ImageField(upload_to='images/', default ='default.jpg') # Images will be stored in media/images/
    item_description = models.TextField(default= '', max_length=10000)

    def __str__(self):
        return self.item_name

    class Meta:
        db_table = 'items'



