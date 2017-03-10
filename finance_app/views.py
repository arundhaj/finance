from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}

    return render(request, 'finance_app/index.html', context)
