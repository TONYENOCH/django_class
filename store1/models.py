from django.db import models 
from django.contrib.auth.models import User

class Post(models.Model):
    tittle = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now= True)

    # def _str_(self):
        # return f'{self.tittle}'
