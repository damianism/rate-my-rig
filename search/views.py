from django.shortcuts import render, redirect
from blog.models import Post
from django.core.paginator import Paginator

def do_search(request):
    
    type_session = request.session.get('type',None)
    print("type_session = ", type_session)
    
    selections = ["title", "gpu", "cpu", "ram", "psu", "mainboard" ]
    search_type = request.GET.get('type')
    if search_type is None:
        search_type = type_session
    
    # searching with blank will still work. However, it will cause errors with 
    # the pagination
    if request.GET['q'] == "":
        return redirect('search')
        

    # DOING A FOR LOOP HERE DIDNT WORK! IT DOESNT SEEM TO LIKE IT!
    if search_type == "title":   posts = Post.objects.filter(title__icontains=request.GET['q'])
    elif search_type == "gpu":   posts = Post.objects.filter(gpu__icontains=request.GET['q'])
    elif search_type == "cpu":   posts = Post.objects.filter(cpu__icontains=request.GET['q'])
    elif search_type == "ram":   posts = Post.objects.filter(ram__icontains=request.GET['q'])
    elif search_type == "psu":   posts = Post.objects.filter(psu__icontains=request.GET['q'])
    elif search_type == "mainboard":   posts = Post.objects.filter(mainboard__icontains=request.GET['q'])
    
    paginator = Paginator(posts, 5) # Show 5 posts per page
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "object_list": posts,
        "selections": selections,
        "type": search_type
    }
    
    request.session['type'] = search_type
    return render(request, "search/search_results.html", context )
    
    
    
def search_view(request):

    context = {
        "selections": ["title", "gpu", "cpu", "ram", "psu", "mainboard" ]
    }
    return render(request, "search/search.html", context)