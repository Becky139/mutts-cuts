from django.shortcuts import render

# Create your views here.


def bookings(request):
    """
    Bookings view
    """
    return render(request, 'bookings/bookings.html')
