from django.shortcuts import render

def infopage(request):
    return render(request, 'Infopage.html')
