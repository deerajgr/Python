from django import forms
from .models import Habit, HabitLog

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency', 'start_date']

class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ['completed']