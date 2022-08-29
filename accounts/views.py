from django.shortcuts import render,redirect
from .forms import CustomeUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Register user
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomeUserForm()
        if request.method == 'POST':
            form = CustomeUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'User ' + '' + user + '' + ' have been created now you can login')
                return redirect('home')
    context = {'form':form}
    return render(request, 'registration/signup.html', context)