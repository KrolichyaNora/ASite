from importlib.metadata import requires
from urllib import request
from django.db import models
from django.db.models import CheckConstraint, Q, F

# Q - фильтр
# F - обращение к полю в модели
class Role(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f"({self.role}) {self.login}: {self.password}"

    class Meta:
        constraints = [
            CheckConstraint(
                check = ~Q(login = ""), 
                name = 'login_isnt_empty',
            ),
            CheckConstraint(
                check = ~Q(password = ""), 
                name = 'password_isnt_empty',
            ),
        ]

