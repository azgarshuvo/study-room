from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm # django default registration form
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # show all fields from Room model
        exclude  = ['host', 'participants'] # exclude from the form field list

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'avatar', 'bio']
