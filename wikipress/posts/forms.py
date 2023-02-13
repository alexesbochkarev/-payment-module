from django import forms
from django.core.exceptions import ValidationError

from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Post


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          self.fields["text"].required = False

    class Meta:
        model = Post
        fields = ('title', 'text', 'slug', 'group')
        widgets = {
              'text': CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }