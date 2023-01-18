from django.shortcuts import render
from .models import Booking

# Create your views here.


def create_booking(request):
    """
    Create booking
    """
    return render(request, 'bookings/create_booking.html')


def view_booking(request):
    """
    View booking
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/view_booking.html', context)
