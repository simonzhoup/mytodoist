from django.shortcuts import render
from .forms import Register,Login

def index(request):
    reform = Register()
    loform = Login()
    return render(request,'base.html',{'reform': reform,'loform':loform})