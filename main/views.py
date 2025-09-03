from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406397750',
        'name' : 'Nazwa Zahra Sausan',
        'class' : 'PBP D'
    }

    return render(request, "main.html", context)