from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import BlogForm, BlogModeratorForm
from blog.models import Blog


class BlogListview(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog



class BlogDetailview(DetailView):
    template_name = 'blog/blog_detail.html'
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ('title', 'content', 'images', 'publish_at', 'count_views')
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/blog_form.html'
    model = Blog
    fields = ('title', 'content', 'images', 'publish_at', 'count_views')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=(self.kwargs.get('pk'),))

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return BlogForm
        if user.has_perm("blog.can_edit"):
            return BlogModeratorForm

        raise PermissionDenied


class BlogDeleteView(DeleteView):
    template_name = 'blog/blog_delete.html'
    model = Blog
    success_url = reverse_lazy('blog:blog_list')