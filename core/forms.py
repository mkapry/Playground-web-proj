from django import forms
from game.models import Game

class MyCoolForm(forms.Form):
    Course = forms.CharField()
    players = forms.CharField()
    # как быть если надо добавить других пользователей приложения


class NewGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('course', 'score')
        # не уверена что мне надо будет именно так

