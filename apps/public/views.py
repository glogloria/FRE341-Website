from django.shortcuts import render

# Create your views here.
def landing_page(request):
    """
    View for the home/landing page.
    """
    return render(request, 'home.html', {
        'current_page': 'home'
    })

def about(request):
    """
    View for the about page
    """
    return render(request, 'about.html', {
        'current_page': 'about'
    })

def products(request):
    """
    View for the products page
    """
    return render(request, 'products.html', {
        'current_page': 'products'
    })

def gallery(request):
    """
    View for the gallery page
    """
    return render(request, 'gallery.html', {
        'current_page': 'gallery'
    })

def video(request):
    """
    View for the video page
    """
    return render(request, 'video.html', {
        'current_page': 'video'
    })