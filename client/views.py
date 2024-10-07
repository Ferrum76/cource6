from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog
from client.forms import MailingSettingsForm, ClientForm, MailingSettingsManagerForm
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from client.models import MailingSettings, Client, MailingMessage, MailingLog


class MailingListView(ListView):
    model = MailingSettings
    template_name = "client/mailingsettings_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['blog_list'] = Blog.objects.order_by('?')[:3]
        context['mailing_all'] = len(MailingSettings.objects.all())
        context['mailing_active'] = len(MailingSettings.objects.filter(status='started'))
        context['client_unique'] = len(Client.objects.all().distinct())
        return context


class MailingSettingCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("client:mailing_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingSettingUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy("client:mailing_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingSettingsForm
        elif user.has_perm("client.switch_status"):
            return MailingSettingsManagerForm
        raise PermissionDenied


class MailingSettingDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("client:mailing_list")

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class MailingSettingDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings
    template_name = "client/mailingsettings_detail.html"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client/client_list.html'


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client/client_detail.html'


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client:client_list')


class MessageListView(LoginRequiredMixin, ListView):
    model = MailingMessage
    template_name = 'client/mailingmessage_list.html'


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = MailingMessage
    template_name = 'client/mailingmessage_detail.html'


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = MailingMessage
    fields = '__all__'
    success_url = reverse_lazy('client:message_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingMessage
    fields = '__all__'
    success_url = reverse_lazy('client:message_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('client:message_list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if obj.owner == self.request.user:
            return obj
        raise PermissionDenied


class MailingLogListView(LoginRequiredMixin, ListView):
    model = MailingLog
    template_name = 'client/mailinglog_list.html'
