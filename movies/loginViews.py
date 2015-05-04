'''
Created on May 3, 2015

@author: Polarbear
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import Http404

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail

from django.contrib.auth.models import User
from django.db import transaction
from forms import RegisterForm
from forms import SigninForm
from forms import ResendEmailForm
from forms import ForgetPasswordForm
from forms import ResetUserPassword
from models import UserInfo



@transaction.commit_on_success
def register(request):
    context={}
    if request.method == 'GET':
        return render(request,'LoginRegister.html',context)
    
    form = RegisterForm(request.POST)
    if not form.is_valid():
        context['registerform'] = form
        return render(request, 'LoginRegister.html', context)

    try:
        new_user = User.objects.create_user(username = form.cleaned_data['username'], password = form.cleaned_data['password1'], email = form.cleaned_data['email'])
        new_user.is_active = False
        new_user.save()
        new_user_info = UserInfo.objects.create(user=new_user)
        UserInfo.id = new_user.id
        new_user_info.save()
        token = default_token_generator.make_token(new_user)
        email_body = """Please click the link below to verify your registration and complete the the whole registeration process:
        http://%s%s""" %(request.get_host(),reverse('confirm',args=(new_user.id,token)))
        send_mail(subject="Verify your email address", message=email_body, from_email="summerxyt@163.com", recipient_list=[new_user.email])
        context['text'] = True
    except Exception:
        if new_user_info:
            new_user_info.delete()
        if new_user:
            new_user.delete()
        return render(request, 'LoginRegister.html', context)

    return render(request, 'needs-confirmation.html',{'sent':True})

def signin(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'LoginRegister.html', context)
    
    form = SigninForm(request.POST)
    context['signinform']=form
    if not form.is_valid():
        return render(request, 'LoginRegister.html', context)
    
    user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
    if user and user.is_active:
        login(request, user)
    if 'next' not in request.POST:
        return redirect('/movies')
    else:
        return render(request, 'LoginRegister.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('/movies/login')

@transaction.commit_on_success
def confirm_registeration(request, userid, token):
    user = get_object_or_404(User, id=userid)
    if not default_token_generator.check_token(user, token):
        raise Http404
    user.is_active = True
    user.save()
    return render(request, 'needs-confirmation.html', {'confirmed':True})

def send_new_confirm_email(request):
    if request.method != 'POST':
        form = ResendEmailForm()
        return render(request, 'needs-confirmation.html',{'form':form})

    form = ResendEmailForm(request.POST)
    if form.is_valid():
        new_user = User.objects.get(email=form.cleaned_data['email'])
        token = default_token_generator.make_token(new_user)
        email_body = """Please click the link below to verify your registration and complete the the whole registeration process:
        http://%s%s""" %(request.get_host(),reverse('confirm',args=(new_user.id,token)))
        send_mail(subject="Verify your email address", message=email_body, from_email="summerxyt@163.com", recipient_list=[new_user.email])
        return render(request, 'needs-confirmation.html',{'sent':True})
    else: 
        return render(request, 'needs-confirmation.html',{'form':form})
 
@transaction.commit_on_success
def reset_user_password(request, userid, token):   
    user = get_object_or_404(User, id=userid)
    # Send 404 error if token is invalid
    if not default_token_generator.check_token(user, token):
        raise Http404

    context = {}
    context['userid'] = userid
    context['token'] = token

    if request.method != 'POST':
        form = ResetUserPassword()
        context['form'] = form
    else:
        form = ResetUserPassword(request.POST)
        context['form'] = form
    if form.is_valid():
        user.set_password(form.cleaned_data['password1'])
        user.save()
        context['reset'] = 'success'
    return render(request,'ResetPassword.html',context);

@transaction.commit_on_success
def forget_password(request):
    context={}
    if request.method!='POST':
        form = ForgetPasswordForm()
        context['form'] = form
        return render(request,'ForgetPassword.html',context)

    form = ForgetPasswordForm(request.POST)
    context['form'] = form
    if not form.is_valid():
        return render(request,'ForgetPassword.html',context)
    user=User.objects.get(email=form.cleaned_data['email'])

    token=default_token_generator.make_token(user)
    email_body= """Please click the link belwo to reset your password:
    http://%s%s""" %(request.get_host(),reverse('reset_password',args=(user.id,token)))
    send_mail(subject="Reset your password",
        message=email_body,
        from_email="summerxyt@163.com",
        recipient_list=[user.email])
    return render(request, 'ForgetPassword.html', {'sent':True})
