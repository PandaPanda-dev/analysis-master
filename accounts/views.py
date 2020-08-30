from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

def logout(request):

    if not request.user.is_authenticated:
        return redirect('/login/')

    auth_logout(request)

    return render(request, 'accounts/logout.html')
