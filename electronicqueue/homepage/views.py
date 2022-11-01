from django.shortcuts import render

# Create your views here.



def homepage(request):
    return render(request, 'homepage_detail.html')

