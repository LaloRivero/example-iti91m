''' Users Views. '''
# Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm


def login_view(request):
    ''' Login view '''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect ('feed')
        else:
            return render(request,'users/login.html',{'error':'Invalid username and password'})

    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """ Logout a user """
    logout(request)
    return redirect('login')


def signup(request):
    """ Sign up view """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']

        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password do not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already taken'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request,'users/signup.html')



@login_required
def update_profile(request):
    """ Update a user's profile view """

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.bio = data['bio']
            profile.picture = data['picture']
            profile.save()
            messages.success(request, 'Your profile has been updated!')

            return redirect('feed')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )