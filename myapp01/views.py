from django.shortcuts import render, redirect

# Create your views here.
from django.http.response import HttpResponse
def index(request):
    return HttpResponse("My First Django App.")

from django.template.loader import get_template
from .models import Post
from datetime import datetime

# def homepage(request):
#    template = get_template('index.html')
#    posts = Post.objects.all()
#    now = datetime.datetime.now()
#    html = template.render(locals())
#     post_lists= list()
#     for count, post in enumerate(posts):
#        post_lists.append("No.{}:".format(str(count)))
#        post_lists.append("<small>"+str(post.body)+"</small><br><br>")
#     return render(request, 'index.html', locals())


#====================================================================只把資料庫的號碼、名稱及內容顯示出來

# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count+1)) +str(post)+"<br>")
#         post_lists.append("<small>" + str(post.body)+ "</small></br></br>")
#     return HttpResponse(post_lists)#HttpResponse:我們在views.py 裡寫html的語法，借由它直接推到網頁上顯示出來

#========================================================================================
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    post_lists= list()
    for count, post in enumerate(posts):
        post_lists.append("No.{}".format(str(count)) + str(post) + "</br>")
        post_lists.append("<small>" + str(post.body) + "</small><br></br>")
    return render(request, 'index.html', locals())
#    尚未完成index.html 先行註解

def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')        