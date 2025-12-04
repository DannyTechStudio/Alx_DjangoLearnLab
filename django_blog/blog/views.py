from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm

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
            