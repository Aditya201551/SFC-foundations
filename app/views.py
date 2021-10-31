from django.contrib import auth
from django.forms.forms import Form
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse, request
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from app.models import *
from app import views
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView
from django.core.paginator import Paginator
import json
from django.http import Http404, HttpResponse, request
# Create your views here.


def index(request):
    return render(request, 'index.html',{'objects':BannerEvents.objects.all(),'events':Event.objects.all()[:2],
                                         'newslist': New.objects.all()[:2]
        })


def founder(request):
    return render(request, 'pages/About-Us/founder.html')


def know(request):
    return render(request, 'pages/About-Us/knowsfc.html')


def objectives(request):
    return render(request, 'pages/About-Us/objectives.html')


def workingmodel(request):
    return render(request, 'pages/KMP/kmp.html')


def core_team(request):
    return render(request, 'pages/About-Us/coreteam.html')

def blog(request,id):
    
    return render(request, 'pages/Blog/blog.html')


def BlogSlider(request):
    return render(request, 'pages/slider-event/slider-event.html')

def BlogDonate(request):
    return render(request, 'pages/Donate/Donate.html')

def Blog_feed(request):
    return render(request, 'pages/FEED/feed.html')

def contact(request):
    return render(request, 'pages/Contact-Us/contact.html')


def events(request):
    return render(request, 'pages/Events/events.html')


def join(request):
    return render(request, 'pages/Join-Us/joinus.html')
def Donate(request):
    return render(request, 'pages/Donate/Donate.html')

def news(request):
    return render(request, 'pages/news/news.html')

def gyan(request):
    return render(request,'pages/Projects/gyan.html')

def sampuran(request):
    return render(request, 'pages/Projects/Sampuran.html')


def vatavaran(request):
    return render(request, 'pages/Projects/vatavaran.html')



class BlogListView(ListView):
    model=BlogPost
    template_name='pages/Blog/blogList.html'
    paginate_by=1
    ordering=['-id']

    def get_context_data(self, *args, **kwargs):
        try:
            return super(BlogListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page']='last'
            return super(BlogListView, self).get_context_data(*args, **kwargs)
    
    

def BlogDetailView(request,pk):
    model = BlogPost
    template_name='pages/Blog/blog_detail.html'
    object = BlogPost.objects.get(id = pk)
    
    if request.method == 'POST':
        author = request.POST['name']
        comment = request.POST['comment']
        x= BlogPostComment.objects.create(author=author, comment=comment, post=object)
        x.save()
        
        
    context ={
        'object':object,
    }
    
    return render(request, 'pages/Blog/blog_detail.html', context)


class NewsListView(ListView):
    model = New
    template_name = 'pages/news/news.html'
    paginate_by = 1
    ordering = ['-date']

    def get_context_data(self, *args, **kwargs):
        try:
            return super(NewsListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 'last'
            return super(NewsListView, self).get_context_data(*args, **kwargs)


class NewsDetailView(DetailView):
    model=New
    template_name='pages/news/newsDetail.html'



class EventListView(ListView):
    model=Event
    template_name='pages/Events/events.html'
    paginate_by = 1
    ordering = ['-date']
    def get_context_data(self, *args, **kwargs):
        try:
            return super(EventListView, self).get_context_data(*args, **kwargs)
        except Http404:
            self.kwargs['page'] = 'last'
            return super(EventListView, self).get_context_data(*args, **kwargs)

class EventDetailView(DetailView):
    model=Event
    template_name = 'pages/Events/eventDetail.html'


def upcommingEvents(request, pk):
    model=BannerEvents.objects.get(id=pk)
    return render(request, 'pages/slider-event/bannerEvents.html', {'model': model})
