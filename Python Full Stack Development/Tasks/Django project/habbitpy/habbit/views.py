from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, HabitLog
from django.contrib.auth.decorators import login_required
from datetime import date
from .forms import HabitForm, HabitLogForm


@login_required
def dashboard(request):
    habits = Habit.objects.filter(user=request.user, is_active=True)
    return render(request, 'habits/dashboard.html', {'habits': habits})
@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('dashboard')
    else:
        form = HabitForm()  # define form here as well

    return render(request, 'habits/create_habit.html', {'form': form})

@login_required
def log_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    today = date.today()
    HabitLog.objects.get_or_create(habit=habit, date=today, defaults={'completed': True})
    return redirect('dashboard')

@login_required
def view_logs(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    logs = HabitLog.objects.filter(habit=habit).order_by('-date')
    return render(request, 'habits/view_logs.html', {'habit': habit, 'logs': logs})
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # or wherever you want to go
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
@login_required
def habit_detail(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    return render(request, 'habits/habit_detail.html', {'habit': habit})
