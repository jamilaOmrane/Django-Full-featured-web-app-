from django.shortcuts import render
#from django.http import HttpResponse

posts = [
    {
        'author': 'CoreyMS',
        'title' : 'Blog post 1',
        'content' : 'First Post content',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title' : 'Blog post 2',
        'content' : 'Second Post content',
        'date_posted' : 'August 29, 2018'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    #return HttpResponse('<h1>Home</h1>')
    return render(request, 'blog/home.html', context)

def about(request):
   #return HttpResponse('<h1>About</h1>')
   return render(request, 'blog/about.html', {'title':'About'})