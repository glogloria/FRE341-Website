from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """
    View for the home/landing page.

    Renders base.html
    """
    return render(request, 'base/base.html')