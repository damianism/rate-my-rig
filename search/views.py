from django.shortcuts import render
from blog.models import Post


def do_search(request):
    
    selections = ["title", "gpu", "cpu", "ram", "psu", "mainboard" ]
    search_type = request.GET.get('type')

    # DOING A FOR LOOP HERE DIDNT WORK! IT DOESNT SEEM TO LIKE IT!
    if search_type == "title":   posts = Post.objects.filter(title__icontains=request.GET['q'])
    elif search_type == "gpu":   posts = Post.objects.filter(gpu__icontains=request.GET['q'])
    elif search_type == "cpu":   posts = Post.objects.filter(cpu__icontains=request.GET['q'])
    elif search_type == "ram":   posts = Post.objects.filter(ram__icontains=request.GET['q'])
    elif search_type == "psu":   posts = Post.objects.filter(psu__icontains=request.GET['q'])
    elif search_type == "mainboard":   posts = Post.objects.filter(mainboard__icontains=request.GET['q'])
    
    context = {
        "object_list": posts,
        "selections": selections,
        "type": search_type
    }
    
    return render(request, "search/search.html", context )
    
def pre_search(request):

    context = {
        "selections": ["title", "gpu", "cpu", "ram", "psu", "mainboard" ]
    }
    return render(request, "search/pre_search.html", context)