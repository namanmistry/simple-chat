from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'chat/sign-in.html')

@csrf_exempt
def chat_room(request):
    if request.method=="POST":
        username=request.POST.get('username')
        group_name=request.POST.get('group_name')
        return render(request,'chat/index.html',{'username':username,'group_name':group_name})
    else:
        return HttpResponse("<h1>Method not allowed</h1>")