from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BandMember, Event

def home(request):
    """
    Render the homepage.

    This view handles the rendering of the main homepage of the application.
    It serves as the entry point for users exploring the band-related app.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered homepage.
    """
    return render(request, "band_app/home.html")

def band_members(request):
    """
    Display all band members.

    This view retrieves all band members from the database and displays them
    on the band members page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered band members page with the list of members.
    """
    members = BandMember.objects.all()
    return render(request, "band_app/members.html", {"members": members})

def events(request):
    """
    Display all events.

    This view fetches all events related to the band from the database and
    renders them on the events page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered events page with the list of events.
    """
    events = Event.objects.all()
    return render(request, "band_app/events.html", {"events": events})

def register(request):
    """
    Handle user registration and login after successful creation.

    This view handles user registration by displaying a form for account creation.
    If the form is valid (submitted via POST), it creates the new user, logs them in,
    and redirects to the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The registration page on GET or a redirect to the homepage on successful registration.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "band_app/register.html", {"form": form})

def user_login(request):
    """
    Handle user authentication and login.

    This view processes login attempts. On a POST request with valid credentials,
    it authenticates the user, logs them in, and redirects them to the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The login page on GET or a redirect to the homepage on successful login.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "band_app/login.html", {"form": form})

def user_logout(request):
    """
    Log the user out and redirect to the homepage.

    This view handles the user logout process. Once the logout is completed,
    the user is redirected back to the homepage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the homepage after successful logout.
    """
    logout(request)
    return redirect("home")
