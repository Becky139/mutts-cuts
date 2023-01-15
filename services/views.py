from django.shortcuts import render

# Create your views here.


def services(request):
    """
    Services view
    """
    return render(request, 'services/services.html')
