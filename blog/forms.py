from django.forms import ModelForm
from .models import Post
class Post_form(ModelForm):
    class Meta:
        model=Post
        fields =('title','body','featured_image')