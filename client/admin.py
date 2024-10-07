from django.contrib import admin

from client.models import Client, MailingMessage, MailingSettings


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'owner',)
    list_filter = ('owner',)
    search_fields = ('email', 'owner',)


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'letter', 'owner',)
    list_filter = ('subject', 'owner',)
    search_fields = ('subject', 'owner',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'period', 'status', 'message', 'owner',)
    list_filter = ('start_time', 'status', 'owner',)
    search_fields = ('clients', 'owner',)