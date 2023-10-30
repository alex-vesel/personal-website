from django.shortcuts import render
from bakery.views import BuildableDetailView, BuildableListView

# Create your views here.

def home(request):
    return render(request, "home/home.html", {"title": "Home"})


# bakery views
class HomeView(BuildableDetailView):
    template_name = "home/home.html"
    build_path = "index.html"
    model = None
    queryset = None
    context_object_name = "home"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    extra_context = {"title": "Home"}