from django import forms

from playground.models import Blog, Comment, Post, Classify
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field


class BlogCreateForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Blog
        exclude = ('author', 'created_at', 'updated_at',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BlogCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):

        self.instance.author = self.user
        print('SAVE', self.instance.author)
        return


class CommentCreateForm(forms.ModelForm):
    text = forms.CharField()

    class Meta:
        model = Comment
        exclude = ('author', 'created_at', 'updated_at','post',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentCreateForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.instance.author = self.user
        print('SAVE', self.instance.author)
        return


class PostCreateForm(forms.ModelForm):
    # text = forms.CharField()

    class Meta:
        model = Post
        exclude = ('author', 'created_at', 'updated_at')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('blog', css_class='chosen-select'),
                'text',
            ),
            ButtonHolder(
                Submit('submit', 'Отправить')
            )
        )

    def save(self, *args, **kwargs):
        self.instance.author = self.user
        print('SAVE', self.instance.author)
        return super(PostCreateForm, self).save(*args, **kwargs)


# class ClassifyForm(forms.ModelForm):
#     text = forms.CharField()
#
#     class Meta:
#         model = Classify
#
#     def form_valid(self, form):
#         # Тут возможно заполнение чего-то типа автора итп
#         resp = super(Classify, self).form_valid(form)
#         # Здесь мы вызываем метод родителя, чтобы данные сохранились, но ответ не возвращаем
#         return "OK"
#         # Ну вот, просто вернули "OK", если все хорошо


class SearchForm(forms.Form):
    search = forms.CharField()
