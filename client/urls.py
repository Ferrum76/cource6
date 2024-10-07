from django.urls import path
from django.views.decorators.cache import cache_page

from client.apps import ClientConfig
from client.views import (
    MailingListView,
    MailingSettingCreateView,
    MailingSettingDetailView,
    MailingSettingDeleteView,
    MailingSettingUpdateView,
    ClientListView,
    ClientCreateView,
    ClientDetailView,
    ClientUpdateView,
    ClientDeleteView,
    MessageListView,
    MessageCreateView,
    MessageDetailView,
    MessageUpdateView,
    MessageDeleteView,
    MailingLogListView,
)

app_name = ClientConfig.name

urlpatterns = [
    path('', cache_page(60)(MailingListView.as_view()), name='mailing_list'),
    path('create/', MailingSettingCreateView.as_view(), name='mailing_create'),
    path('detail/<int:pk>/', MailingSettingDetailView.as_view(), name='mailing_detail'),
    path('update/<int:pk>/', MailingSettingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingSettingDeleteView.as_view(), name='mailing_delete'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/detail/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('message/detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),

    path('log_list/', MailingLogListView.as_view(), name='log_list')

]