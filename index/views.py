from django.shortcuts import render

def index(request):
    context = {}
    print(request.path)
    return render(request, "index/index.html", context)
