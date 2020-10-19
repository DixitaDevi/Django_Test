from django.shortcuts import render, redirect
from .models import *
from .forms import NoteForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def home(request):
    notes = Notes.objects.all()
    users = User.objects.all()
    return render(request, "home.html", {'notes': notes, 'users': users})

def user(request, pk_test):
    user = User.objects.get(id=pk_test)
    notes = user.notes_set.all()
    notes_count = notes.count()
    context = {'user': user, 'notes': notes}
    return render(request, "users.html", context)


def createNote(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'note_form.html', context)


def updateNote(request, pk):
    note = Notes.objects.get(id=pk)
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'note_form.html', context)

def deleteNote(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == "POST":
        note.delete()
        return redirect('/')
    context = {'item': note}
    return render(request, 'delete.html', context)
