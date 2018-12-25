from django.urls import path
from .views import register, profile

# class based authentication views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html') , name='user-login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name='user-logout' ),
    path('register/',register, name='user-register' ),
    path('profile/', profile , name='user-profile' ),
]


""" 
auth_views NOTES:
    - these are class based views created by django itself
    - they handle the login and logout forms and NOT the templates!
    
    auth_views.LoginView.as_view() 
        - the as_view() at the end is neccesary
        - it does take in arguements
    
    auth_views.LoginView.as_view(template_name='users/login.html')
        - as mentioned aboive, the view only handles forms and NOT the templates
        - error it gives if run without a template
            
            TemplateDoesNotExist at /login   ERROR PAGE
            Request Method: 	GET
            Request URL: 	    http://django-practice-2-damianism.c9users.io/login/
            Django Version: 	2.0
            Exception Type: 	TemplateDoesNotExist
            Exception Value:    registration/login.html
        
        - it will be fault look for it at "registration/login.html"
        - template_name ARGUEMENT
            -TELL DJANGO WHERE TO LOOK FOR THE TEMPLATE in this case 'users/login.html'
"""