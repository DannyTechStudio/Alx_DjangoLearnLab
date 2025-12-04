from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)        #------- Auto login after registration
            return redirect('profile')
    else:
        form = RegisterForm()
        
    return render(request, 'blog/register.html', {'form': form})


@login_required
def profile(request):
    user = request.user   #------ Current logged-in user

    if request.method == 'POST':
        #-------  Read form inputs
        email = request.POST.get('email')
        username = request.POST.get('username')

        # Updating user model
        user.email = email
        user.username = username
        user.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Prevent resubmission on reload
    
    return render(request, 'blog/profile.html', {'user': user})


#-----------
# Implementing CRUD operations using class-based views
#-----------

#-------- ListView: For showing all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.htmnl'
    context_object_name = 'posts'
    ordering = ['-published_date']      #----- Order by newest posts
    
    
#-------- DetailView: For showing the details of a particular post can be seen or done by anyone
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    

#-------- CreateView: Only logged-in users can create posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user        #---- Setting author automatically
        return super().form_valid(form)
    

#--------- UpdateView: Only authors can edit posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author         #---- Allows only authors to edit posts
    

#-------- DeleteView: Only authors can delete posts
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')