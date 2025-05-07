from django.shortcuts import render

# Create your views here.

# def home(request):
#     return render(request, "home/home.html", {"title": "Home"})

def bloglist(request):
    return render(request, "blog/bloglist.html", {"title": "Blog"})


def imitationlearning(request):
    return render(request, "blog/posts/imitationlearning.html", {"title": "Imitation Learning"})