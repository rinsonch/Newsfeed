# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from allauth.account.views import SignupView
from django.contrib.auth import authenticate,login

from django.shortcuts import render,redirect

from .forms import SignUpForm

from django.shortcuts import render



def signup(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user=form.save()
            user.email= form.cleaned_data.get('username')
            user.refresh_from_db()
            user.profile.dob = form.cleaned_data.get('dob')
            user.profile.profpic=request.FILES['profpic']
            b=user.id
            user.profile.save()
            user.profile.follow.add(b)
            user.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password2')
            user = authenticate(username=username,password=raw_password)
            login(request, user)
            return redirect('/posts/')


    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})



