from django.shortcuts import render

# Create your views here.
def show_main(request):
    names = ['Sword', 'Shield', 'Potion']
    descriptions = [
                    'A sword made of steel', 
                    'A shield made of steel', 
                    'A potion of healing'
                    ]
    amount = [1, 1, 4]

    zipped = zip(names, descriptions, amount)
    context = {
        'zipped': zipped
        
    }
    return render(request, 'main.html', context)