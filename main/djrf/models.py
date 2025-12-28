from django.db import models
# Create your models here.

# Model
class UserModel(models.Model):
    CHOICES = (("Unread", "unread"), ("read", "Read"))
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    status = models.CharField(choices=CHOICES, default="Unread", max_length=100)

    def __str__(self):
        return self.date
