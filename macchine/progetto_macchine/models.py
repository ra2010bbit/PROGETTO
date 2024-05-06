from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, Group, Permission
class Machine(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    year_manufactured = models.IntegerField()
    serial_number = models.CharField(max_length=50)
    machine_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MachineImage(models.Model):
    machine = models.ForeignKey(Machine, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='machine_photos')

    def __str__(self):
        return f"Image of {self.machine.name}"

class CustomUser(AbstractUser):
    # Aggiungi l'attributo related_name personalizzato per il campo groups
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    
    # Aggiungi l'attributo related_name personalizzato per il campo user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',
        related_query_name='custom_user'
    )