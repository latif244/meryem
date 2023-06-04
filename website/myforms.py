from django.db import models


class Nachrichts(models.Model):
    name = models.TextField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=False)
    subject = models.TextField(blank=False, null=True)
    message = models.TextField(blank=False, null=False)
    time = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(auto_created=True, null=True)


# class Newsletters(models.Model):
#     email = models.EmailField(blank=False, null=False, unique=True)
#     time = models.DateTimeField(auto_now_add=True)
#     ip_address = models.GenericIPAddressField(auto_created=True, null=True) 