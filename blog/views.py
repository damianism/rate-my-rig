from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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

class PostListView(ListView):
    """ class base view to display all the posts """
    
    # where it looks for the template and what template
    # <app>/<model>_<viewtype>.html     - e.g. blog/post_list.html
    
    model = Post    # based on what class
    template_name = 'blog/home.html'    # to replace the default template (blog/posts_list.html) use "template_name"
    # context_object_name = 'posts'     # to replace the default context name (object_list) use "context_object_name"
    ordering = ['-date_posted']         # change the order  - ['-date_posted'] to reverse the order
    

class PostDetailView(DetailView):
    """ class base view to display all the posts """
    
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
        'short_info'
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
        'short_info'
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
        
        