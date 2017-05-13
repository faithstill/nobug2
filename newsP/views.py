from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from . import models


# Create your views here.
# something wrong
def index(request):
     news_list = models.NewsPost.objects.all()
     return render(request,'newsP/index.html', {'news_list': news_list})
  #  return HttpResponse("hello world!")

def news_content_page(request,news_list_id):
    news = models.NewsPost.objects.get(pk=news_list_id)
    return render(request,'newsP/news_content_page.html',{'news': news})
