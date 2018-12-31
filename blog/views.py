from django_filters.views import FilterView
from .filters import PostFilter
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from comments.forms import CommentForm
from comments.models import Comment
from .forms import BlogPostForm
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
)


# function based views!
def home(request):
    """ a view to render blog's home page """
    context = {
        'posts': Post.objects.all()
    }
    
    return render(request, "blog/home.html", context)
    

def about(request):
    """ view to render blog's about page  """
    context = {
        
    }
    return render(request, "blog/about.html", context)
    

# CLASS BASED VIEWS

# class PostListView(ListView):
#     """ class base view to display all the posts """
    
#     # where it looks for the template and what template
#     # <app>/<model>_<viewtype>.html     - e.g. blog/post_list.html
    
#     model = Post    # based on what class
#     template_name = 'blog/home.html'    # to replace the default template (blog/posts_list.html) use "template_name"
#     # context_object_name = 'posts'     # to replace the default context name (object_list) use "context_object_name"
#     ordering = ['-date_posted']         # change the order  - ['-date_posted'] to reverse the order
#     paginate_by = 10                    # paginate the posts by an integer
    

class FilterPostListView(ListView):
    """ class-base view to display all the posts based on what's being filtered
        via the installed third party library called "django_filters"
        
        Based on model "Post"
        Renders to the "blog/home.html" template.
        Pagination active by 10
    """
    
    # where it looks for the template and what template
    # <app>/<model>_<viewtype>.html     - e.g. blog/post_list.html
    
    model = Post    # based on what class
    template_name = 'blog/home.html'    # to replace the default template (blog/posts_list.html) use "template_name"
    # context_object_name = 'posts'     # to replace the default context name (object_list) use "context_object_name"
    ordering = ['-date_posted']         # change the order  - ['-date_posted'] to reverse the order
    context_object_name = 'object_list'       # Default: object_list
    paginate_by = 5                    # paginate the posts by an integer
    filterset_class = PostFilter

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()


    def get_context_data(self, **kwrgs):
        context = super().get_context_data(**kwrgs)
        context['filter'] = self.filterset # PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    """ class-based view to display a single post in detail 
        
        Based on model "Post"
        Renders to the "post_detail.html" template
    """
    
    # <app>/<model>_<viewtype>.html     - e.g. blog/post_detail.html
    # context by default will be object
    model = Post

        
        
# the login_required decorator CANNOT be used with class based views
# instead, LoginRequiredMixin (imported above) needs to be passed into the class in far left
# now the user has to be logged in, in order to create a post
class PostCreateView(LoginRequiredMixin, CreateView):
    """ class base view to display all the posts """
    
    # <app>/<model>_<viewtype>.html     - e.g. blog/post_detail.html
    # context by default will be object
    model = Post
    # success_url = '/'   # optional to redirect to another url upon post! - by defualt it redirects to detail-post
    fields = [
        'title', 
        'cpu',
        'gpu',
        'ram',
        'psu',
        'primary_storage',
        'secondary_storage',
        'mainboard',
        'description',
        'image'
    ]
    
    # the form requires a user to be passed in 
    def form_valid(self, form):
        form.instance.author = self.request.user  # passing in an instance of the use 
        
        # overwrite the parent class
        return super().form_valid(form)
        
        
# UserPassesTestMixin passed into the function to restrict user from updating/editting 
# posts made by other users
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ class base view to display all the posts """
    
    # uses the same template as create
    # context by default will be object
    model = Post
    fields = [
        'title', 
        'cpu',
        'gpu',
        'ram',
        'psu',
        'primary_storage',
        'secondary_storage',
        'mainboard',
        'description',
        'image'
    ]
    #
    
    # the form requires a user to be passed in 
    def form_valid(self, form):
        form.instance.author = self.request.user  # passing in an instance of the use 
        
        # overwrite the parent class
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()    # a method to get post object
        
        # returns True if they're the same, False if they're not the same 
        return (self.request.user == post.author)



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ class base view to display all the posts """
    
    # post_confirm_delete.html will be used!
    # context by default will be object
    model = Post
    success_url = '/'
    
    def test_func(self):
        post = self.get_object()    # a method to get post object
        
        # returns True if they're the same, False if they're not the same 
        return (self.request.user == post.author)
        



"""
NOTE!
    some of the classbased views have to be replaced due to the fact that modifying 
    such views turned out to be alot more complex than initially assumed! there's not 
    enough clear examples online and the documentations only do the bear minimum to 
    explain everything
    
    so the following class-based views will be converted to function-based view in the 
    order listed below!
    
        1) "PostDetailView" class-based view was replaced by 
                            function-based view "post_detail_view" 
        2) "PostCreateView" & "PostUpdateView" class-based views were replaced by 
                            function-based view "create_or_edit_post" 

"""

def post_detail_view(request, pk):
    """ Function-based view to display a single post in detail 
        
    - Renders to the "post_detail.html" template based on instance of Post ID
    - Returns 404 error if post not found - incorrect ID
    
    """
    
    # get object
    post = get_object_or_404(Post, pk=pk)
    post.views += 1   # increment view
    post.save()       # save post
    
    # isnt actually needed as i could simply use "object.comment_set.all" to loop over
    # however, the older comments were listed first - so we pass in an ordered comments list
    comments = Comment.objects.filter(post=post).order_by('-id')
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.cleaned_data.get('comment')
            Comment.objects.create(author=request.user, post=post, comment=comment)
            return redirect("post-detail", pk=pk)   # redirecting back to "user-profile" to avoid post-get direct pattern
    else:
        form = CommentForm()
    
    
    context = {
        "object": post,
        "comments": comments,
        "form": form
    }
    
    return render(request, "blog/post_detail.html", context)
    
    
# def create_or_edit_post(request, pk=None):
#     """ Function-based view to:
#         - create a new post
#         - edit an existing post
        
#         based on post being null or not
#     """
    
#     # get object
#     post = get_object_or_404(Post, pk=pk) if pk else None
    
#     if request.method == "POST":
#         # form posted with post(object) as either None or an existing post(object) 
#         # is post == None:  instance will be None so a new post will be created
#         # if an instance if passed in then it will edit
#         form = BlogPostForm(request.POST, request.FILES, instance=post )
#         if form.is_valid():
#             form.save()
#             return redirect('post-detail')
#     else:
#         form = BlogPostForm(instance=post)
    
#     context = {
#         "form":form
#     }
    
#     return render(request, "blog/post_form.html", context)
        