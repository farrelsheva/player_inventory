from django.shortcuts import render

# Create your views here.
def show_main(request):
    
    context = {
        'name' : "Farrel Sheva Alkautsar",
        'class' : "PBP A",
        'npm' : "2206030344"
        
    }
    return render(request, 'main.html', context)