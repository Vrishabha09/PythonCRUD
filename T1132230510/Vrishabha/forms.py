from django import forms
from .models import Movies , Movie_T

class RegForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['V_movie_name','V_duration','V_genre','V_director','V_lead_actor','V_language']

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie_T
        fields = ['V_Movie_Name', 'V_trailer', 'V_launch_date']  
        widgets = {
            'V_launch_date': forms.DateInput(attrs={'type': 'date'}),
        }