from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, Booking, User
from .forms import EventForm, UserRegistrationForm
from django.db.models import Count
from django.urls import reverse



def home_view(request):
    events = Event.objects.all().annotate(booking_count=Count('booking'))
    user_bookings = Booking.objects.filter(user=request.user).values_list('event_id', flat=True) if request.user.is_authenticated else []
    context = {
        'events': events,
        'user_bookings': user_bookings,
    }
    return render(request, 'events/home.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'events/register.html', {'form': form})

@login_required
def create_event_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            messages.success(request, "Event created successfully!")
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})


@login_required
def book_event_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.booking_set.count() >= event.capacity:
        messages.warning(request, "Event fully booked!")
        return redirect('home')

    Booking.objects.create(event=event, user=request.user)
    messages.success(request, "Event booked successfully!")
    return redirect('home')



@login_required
def booked_events_view(request):
    bookings = Booking.objects.filter(user=request.user).select_related('event')
    return render(request, 'events/booked_events.html', {'bookings': bookings})



@login_required
def profile_view(request):
    return render(request, 'events/profile.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a homepage or dashboard after login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'events_app/login.html')  


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
   










