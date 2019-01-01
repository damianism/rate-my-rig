from django.contrib.auth.models import User


class EmailAuth:
    """
    Authenticate a user by an exact match on the email and password,  
    in addition to username and password 
    """

    def authenticate(self, username=None, password=None):
        """
        Find the user based off the email and verify the password
        """

        try:
            # find the user via user email
            user = User.objects.get(email=username)
            
            # check passowrd to see if it checks out!
            if user.check_password(password):
                return user
            return None  # password verification FAILED!
            
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        """
        Used by the Django authentiation system to retrieve a user instance
        """
        
        try:
            # find the user via user id
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
            
        except User.DoesNotExist:
            return None