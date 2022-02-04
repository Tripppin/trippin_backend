from django.shortcuts import render


    
# return null value right now
def index(request):
    context = {}
    return render(request, "index.html", context=context)

# return null value right now
def login_view(request):
    context = {}
    return render(request, "login.html", context=context)
