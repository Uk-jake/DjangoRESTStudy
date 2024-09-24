from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50) 
    author = models.CharField(max_length=50) 
    category = models.CharField(max_length=50) 
    pages = models.IntegerField()
    price = models.IntegerField()
    published_date = models.DateField() 
    description = models.TextField()
    
# {
#     "bid": 1,
#     "title": "Django Book",
#     "author": "Kim",
#     "category": "Programming",
#     "pages": 500,
#     "price": 30000,
#     "published_date": "2020-01-01",
#     "description": "Django Book Description"
# }