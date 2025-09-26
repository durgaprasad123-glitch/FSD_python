import django.db.models as models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class Products(models.Model):
    # id field automatically created by Django
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

@receiver(post_save, sender='website.AuthUser')
def create_auth_user_token(sender, instance, created, **kwargs):
    if created:
        from rest_framework.authtoken.models import Token
        Token.objects.create(user=instance)


class AuthUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    user_permissions = None  # Disable user permissions
    groups = None  # Disable groups
    first_name = None  # Disable first name
    last_name = None  # Disable last name   


    def __str__(self):
        return self.email