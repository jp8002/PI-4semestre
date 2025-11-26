from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.urls import reverse as r

class viewTelaLogin(View):
    def get(self, request):

        if request.user.is_authenticated:
            return redirect("paginaInicial")
            
        return render(request, "templateLogin.html")

    def post(self,request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is None:
            return render(request, "templateLogin.html",{"error":"Credenciais erradas"})

        
        login(request,user)
        return redirect('paginaInicial')
