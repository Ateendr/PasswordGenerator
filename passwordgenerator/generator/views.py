from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def about(request):
    return render(request,'generator/about.html')
def home(request):
    return render(request,'generator/home.html')
def password(request):
    len = int(request.GET.get('length'))
    print(len)
    password = ''
    arrLower = list("abcdefghijklmnopqrstuvwxyz")
    arrUpperAndLower = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    arrWithSpecial = list('!@#$%^&*')
    if request.GET.get('UpperCase') :
        arrLower.extend(arrUpperAndLower)
    if request.GET.get('SpecialCharacters'):
        arrLower.extend(arrWithSpecial)
    for x in range(len):
        password +=random.choice(arrLower);
    return render(request,'generator/password.html',{ 'keyword':password })
