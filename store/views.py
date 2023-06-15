from django.views import View
from django.shortcuts import render


class HomeView(View):
    
    def get(self, request):
        return render(request, 'home.html')
    

class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')
