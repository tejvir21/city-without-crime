from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def home_page(request):
    emergencies = Emergency.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'emergencies': emergencies})

# User Module Views
def register_user(request):
    if request.user.is_authenticated:
        return HttpResponse(f"<H1>You are already Logged in as <u>{request.user.username}<u></h1>")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            full_name = request.POST['full_name']

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
                return redirect('register')

            user = User.objects.create_user(username=username, password=password, email=email, first_name=full_name)
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')

        return render(request, 'register_user.html')


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponse(f"<H1>You are already Logged in as <u>{request.user.username}<u></h1>")
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
                        
            if user:
                login(request, user)
                station = PoliceStation.objects.filter(head_officer=user.username)
                if station:
                    return redirect('police_station_dashboard')
                elif user.is_superuser:
                    return redirect('admin_dashboard')
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials!")

        return render(request, 'login.html')

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url="login")
def user_dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url="login")
def lodge_complaint(request):
    if request.method == 'POST':
        description = request.POST['description']
        police_station_id = request.POST['police_station']
        police_station = PoliceStation.objects.get(id=police_station_id)

        complaint = Complaint.objects.create(user=request.user, description=description, police_station=police_station)
        complaint.save()
        messages.success(request, "Complaint lodged successfully!")
        return redirect('view_complaints')

    stations = PoliceStation.objects.all()
    return render(request, 'lodge_complaint.html', {'stations': stations})

@login_required(login_url="login")
def view_complaints(request):
    complaints = Complaint.objects.filter(user=request.user)
    return render(request, 'view_complaints.html', {'complaints': complaints})

# Police Station Module Views
@login_required(login_url="login")
def police_station_dashboard(request):
    station = PoliceStation.objects.filter(head_officer=request.user.username)
    if station:
        station = PoliceStation.objects.get(head_officer=request.user.username)
        complaints = Complaint.objects.filter(police_station=station)
        criminals = Criminal.objects.all()
        
        return render(request, 'station_dashboard.html', {'station': station, 'complaints': complaints, 'criminals': criminals})

    else:
        return HttpResponse("<h1>403 Forbidden</h1>")

@login_required(login_url="login")
def update_complaint_status(request, complaint_id):
    complaint = Complaint.objects.filter(id=complaint_id, police_station__head_officer=request.user)
    if complaint:
        if request.method == 'POST':
            status = request.POST['status']
            complaint[0].status = status
            complaint[0].save()
            messages.success(request, "Complaint status updated!")
            return redirect('police_station_dashboard')

        return render(request, 'update_complaint_status.html', {'complaint': complaint})
    else:
        return HttpResponse("<h1>403 Forbidden</h1>")

@login_required(login_url="login")
def admin_dashboard(request):
    if request.user.is_superuser:
        police_stations = PoliceStation.objects.all()
        complaints = Complaint.objects.all()
        return render(request, 'admin_dashboard.html', {'stations': police_stations, 'complaints': complaints})
    else:
        return redirect('admin')

@login_required(login_url="login")
def add_police_station(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            name = request.POST['name']
            address = request.POST['address']
            phone = request.POST['phone']
            mobile = request.POST['mobile']
            head_officer = request.POST['head_officer']
            password = request.POST['password']

            station = PoliceStation.objects.create(
                name=name,
                address=address,
                phone=phone,
                mobile=mobile,
                head_officer=head_officer,
                password=password,
            )
            station.save()
            messages.success(request, "Police Station added successfully!")
            return redirect('admin_dashboard')

        return render(request, 'add_police_station.html')
    else:
        return redirect('admin')

@login_required(login_url="login")
def delete_police_station(request, station_id):
    if request.user.is_superuser:
        station = PoliceStation.objects.get(id=station_id)
        station.delete()
        messages.success(request, "Police Station deleted successfully!")
        return redirect('admin_dashboard')
    else:
        return redirect('admin')

# Criminal Records Module Views

@login_required(login_url="login")
def add_criminal(request):
    station = PoliceStation.objects.filter(head_officer=request.user.username)
    if station:
    
        if request.method == 'POST':
            name = request.POST['name']
            gender = request.POST['gender']
            height = request.POST['height']
            weight = request.POST['weight']
            crime_level = request.POST['crime_level']
            status = request.POST['status']
            picture = request.FILES['picture']

            criminal = Criminal.objects.create(
                name=name,
                gender=gender,
                height=height,
                weight=weight,
                crime_level=crime_level,
                status=status,
                picture=picture,
            )
            criminal.save()
            messages.success(request, "Criminal added successfully!")
            return redirect('police_station_dashboard')

        return render(request, 'add_criminal.html')
    else:
        return HttpResponse("Unauthorized", status=401)

@login_required(login_url="login")
def criminal_detail(request, criminal_id):
    criminal = get_object_or_404(Criminal, id=criminal_id)
    return render(request, 'criminal_detail.html', {'criminal': criminal})

@login_required(login_url="login")
def edit_criminal(request, criminal_id):
    station = PoliceStation.objects.filter(head_officer=request.user.username)
    if station:
        
        criminal = Criminal.objects.get(id=criminal_id)
        if request.method == 'POST':
            criminal.name = request.POST['name']
            criminal.gender = request.POST['gender']
            criminal.height = request.POST['height']
            criminal.weight = request.POST['weight']
            criminal.crime_level = request.POST['crime_level']
            criminal.status = request.POST['status']
            if 'picture' in request.FILES:
                criminal.picture = request.FILES['picture']
            criminal.save()
            messages.success(request, "Criminal updated successfully!")
            return redirect('police_station_dashboard')

        return render(request, 'edit_criminal.html', {'criminal': criminal})
    else:
            return HttpResponse("Forbidden", status=403)


@login_required(login_url="login")
def delete_criminal(request, criminal_id):
    station = PoliceStation.objects.filter(head_officer=request.user.username)
    if station:
        
        criminal = Criminal.objects.get(id=criminal_id)
        criminal.delete()
        messages.success(request, "Criminal deleted successfully!")
        return redirect('police_station_dashboard')
    else:
        return HttpResponse("Forbidden", status=403)

# Emergency News Module Views

@login_required(login_url="login")
def add_emergency_news(request):
    station = PoliceStation.objects.filter(head_officer=request.user.username)
    if station:
        if request.method == 'POST':
            description = request.POST['description']
            emergency = Emergency.objects.create(description=description)
            emergency.save()
            messages.success(request, "Emergency news added successfully!")
            return redirect('police_station_dashboard')

        return render(request, 'add_emergency_news.html')
    else:
        return HttpResponse("Unauthorized", status=401)

def view_emergency_news(request):
    emergencies = Emergency.objects.all()
    return render(request, 'view_emergency_news.html', {'emergencies': emergencies})