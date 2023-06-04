from django.contrib import admin
from .models import Nachrichts


class NachrichtsAdmin(admin.ModelAdmin):
    list_display = ("id", "ip_address", "time", "name", "email", "subject", "message")

admin.site.register(Nachrichts, NachrichtsAdmin)