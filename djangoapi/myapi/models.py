from django.db import models

# Create your models here.
class input(models.Model):
    title=models.CharField(max_length=20)
    createdAt=models.DateTimeField(auto_now_add=True)

    def __file__(self):
        return self.img
    class Meta:
        ordering=['-createdAt']