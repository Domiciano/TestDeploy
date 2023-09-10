from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout



@method_decorator(login_required, name='dispatch')
class CoursesMain(View):

    def get(self, request):
        return render(request, 'courses_main.html')
    
    def signout(request):
        logout(request)
        return redirect("/signin")
        
    