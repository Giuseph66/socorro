from django.shortcuts import render

def index(request):
    return render(request, 'socorro_app/main.html')

def pergunta(request):
    soma="1+20"
    return render(request,'socorro_app/pergunta.html',{'soma':soma})