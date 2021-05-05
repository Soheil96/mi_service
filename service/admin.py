from django.contrib import admin
from .models import Warranty, Message


class MessageAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Warranty)
