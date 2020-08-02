from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='none.png',blank=True)
    category = models.ForeignKey(Category, default=None, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.title

    def shorter(self):
        return self.text[:100] +'...'
