from django.shortcuts import render
from .models import Image, Location,Category
from django.http import HttpResponse ,Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    print(request)
    title = "Welcome to Her Gallery"
    return render(request, 'pictures/index.html',{"image":images , "title":title})

def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'pictures/search_result.html',{"message":message,"image": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'pictures/search_result.html',{"message":message})

