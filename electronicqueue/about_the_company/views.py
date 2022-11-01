from django.shortcuts import render

# Create your views here.
def about_the_company(request):
    return render(request, 'about_the_company.html')