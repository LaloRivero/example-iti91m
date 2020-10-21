''' Posts Forms '''

# Django
from django import forms

# Models
from posts.models import Post

class PostForm(forms.ModelForm):
    ''' Post model form '''

    class Meta:
        ''' forms settings '''

        model = Post
        fields = ('profile','title','photo')