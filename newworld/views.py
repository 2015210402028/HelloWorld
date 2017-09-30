#coding:utf-8
from django.http import render
def index(request):
       #return HttpResponse(u"Hello World! 大家好！")
       return render(request,"index.html",)
# Create your views here.