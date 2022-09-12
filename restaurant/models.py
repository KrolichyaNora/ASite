from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=32)

class User(models.Model):
    login = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return f"({self.role}) {self.login}: {self.password}"
