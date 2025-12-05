from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tag, Post, Comment

#-------- Register Form
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


#-------- Form for creating & updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
            
        tags_str = self.cleaned_data['tags']
        tags_list = [t.strip() for t in tags_str.split(',') if t.strip()]
        
        final_tags = []
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            final_tags.append[tag]
            
        instance.tags.set(final_tags)
        return instance


#-------- Form for creating & updating blog post comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Write a comment...'}),
        }
        
    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError('Comment cannot be empty!')
        return content