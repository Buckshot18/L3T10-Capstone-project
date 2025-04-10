from .models import Post

class PostForm(forms.ModelForm):
    """
    A form for creating and editing posts.

    Attributes:
        model (Model): The model associated with the form.
        fields (list): The fields to be included in the form.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date']