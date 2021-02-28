from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import sign_inForm, sign_upForm


def sign_up(request):
    if request.method == 'POST':
        signupform = sign_upForm(request.POST)
        if signupform.is_valid():
            first_name = signupform.cleaned_data['first_name']
            last_name = signupform.cleaned_data['last_name']
            email = signupform.cleaned_data['email']
            username = signupform.cleaned_data['username']
            password1 = signupform.cleaned_data['password1']
            password2 = signupform.cleaned_data['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username mavjud iltimos boshqa username kiriting !')
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Elektron pochta mavjud !')
                    return redirect('sign_up')
                else:
                    user = User.objects.create_user(
                        username=username, password=password1,
                        email=email, first_name=first_name, 
                        last_name=last_name)
                    user.save()
            else:
                messages.info(request, "Parollar bir-biriga to'g'ri kelmadi !")
                return redirect('sign_up')
            author = auth.authenticate(username=username, password=password1)
            auth.login(request, author)
            return redirect('../' + username)
    
    else:
        signupform = sign_upForm()
    return render(request, 'accounts/sign_up.html', {'form': signupform})


def sign_in(request):
    if request.method == 'POST':
        signinform = sign_inForm(request.POST)
        if signinform.is_valid():
            username = signinform.cleaned_data['username']
            password = signinform.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('../' + username)
            else:
                messages.error(request, 'Username yoki Parolda hatolik bor !')
                return redirect('sign_in')
    
    else:
        signinform = sign_inForm()
    return render(request, 'accounts/sign_in.html', {'form': signinform})


def sign_out(request):
    auth.logout(request)
    return redirect('/')

