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
class comment(models.model):
    post = models.Foreignkey(Post, on_delte=models. CASCADE)
    author=models.Forignkey(User, on_delete=models.CASCADE)
    message=models.CharField(max_lenght=255)
    create =models. DateTimeFeild(auto_add=True)  

    