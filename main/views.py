from django.shortcuts import render

# Create your views here.
def show_main(request):
    """
    Render the main page of the website.
    """
    return render(request, 'main.html')