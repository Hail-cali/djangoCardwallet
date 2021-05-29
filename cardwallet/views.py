from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django import forms
from django.http import HttpResponse
from djangoCardwallet.login.forms import UserForm, LoginForm
from djangoCardwallet.card.forms import cashForm, deleteCard
from djangoCardwallet.login.forms import Authen
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.
def Post(request):

    loginuser = request.user.get_username()
    user_name = Userinfo.objects.filter(u_name=loginuser)
    user_pnn = user_name.get().Pnn
    try:
        p_card = PersonalcardInfo.objects.filter(puser_Fpun=user_pnn).order_by('card_name')
    except:
        p_card = 'empty'

    return render(request, 'mycard.html', {'username': user_name, 'card': p_card})

def Uploads(request):

    pcn = int(list(request.GET.keys())[0])

    loginuser = request.user.get_username()
    user_name = Userinfo.objects.filter(u_name=loginuser)
    user_pnn = user_name.get().Pnn
    p_card = PersonalcardInfo.objects.filter(puser_Fpun=user_pnn, Pcn=pcn).order_by('card_name')
    p_card_name = p_card.get().card_name.lower()
    comp_nn = MetaCardInfo.objects.filter(c_name=p_card_name).get().companyNm
    #print(f'company name: {comp_nn}')

    return render(request, 'discover_card.html', {'username': user_name, 'card': p_card, 'company': comp_nn})

def Fillcash(request):
    form = cashForm()
    pcn = int(list(request.GET.keys())[0])

    loginuser = request.user.get_username()
    user_name = Userinfo.objects.filter(u_name=loginuser)
    user_pnn = user_name.get().Pnn
    p_card = PersonalcardInfo.objects.filter(puser_Fpun=user_pnn, Pcn=pcn).order_by('card_name')

    balance = p_card.get()
    balance.Balance += 10000
    balance.save()
    return redirect('mycard')

def deletecard(request):
    form = deleteCard(request)
    pcn = int(list(request.GET.keys())[0])
    loginuser = request.user.get_username()
    user_name = Userinfo.objects.filter(u_name=loginuser)
    user_pnn = user_name.get().Pnn
    p_card = PersonalcardInfo.objects.filter(puser_Fpun=user_pnn, Pcn=pcn).order_by('card_name')
    user_card = p_card.get()
    user_card.delete()
    return redirect('mycard')
def createcard(request):

    return redirect('mycard')

def Login(request):
    form = Authen()
    return render(request, 'loging.html', {'form': form})

def signin(request):
    if request.method =="POST":
        form = UserForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mycard')
        else:
            return HttpResponse('retry')
    else:
        form = LoginForm()
        return render(request, 'loging.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            #print(f"signup form : {form.cleaned_data}")
            new_pwd = form.cleaned_data['password']
            u = Userinfo.objects.create(u_name=new_user, pwd=new_pwd, pcard_Fpcn=0)

            login(request, new_user)
            return redirect('login')
    else:
        form = UserForm()
        return render(request, 'join.html', {'form': form})