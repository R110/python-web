from django.db import models

class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
#
# from django.db import models
#
# class Shoe(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     title = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     description = models.TextField()
#     sizes = models.CharField(max_length=100)
#     tag = models.CharField(max_length=20, blank=True, null=True)
#     image = models.ImageField(upload_to="images", blank=True, null=True)
#     views = models.IntegerField(default=0)
#     def __str__(self):
#         return self.title
