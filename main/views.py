from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Sword',
        'description': 'A sword made of steel'
        
    }
    return render(request, 'main.html', context)