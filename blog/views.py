from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from .forms import BlogPostForm  # Assuming you have a BlogPostForm for creating/updating posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# BlogPost list view
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog/blogpost_list.html'  # Specify your template
    context_object_name = 'posts'
    paginate_by = 10  # Add pagination

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True).order_by('-created_at')


# BlogPost detail view
class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'  # Specify your template
    context_object_name = 'post'

    def get_object(self):
        # Increment view count
        post = super().get_object()
        post.view_count += 1
        post.save()
        return post


# Create BlogPost view
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Automatically set the author
        return super().form_valid(form)


# Update BlogPost view
class BlogPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure the user is the author


# Delete BlogPost view
class BlogPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'
    success_url = reverse_lazy('blog:blogpost_list')  # Redirect to blog list

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
