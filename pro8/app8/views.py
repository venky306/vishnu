from django.shortcuts import render
def show(request):
    return render(request,'index.html')


def showIndex(request):
    x=request.POST.get("first name")
    y=request.POST.get("second name")
    d1={"message":x+y}

    return render(request,'index.html',d1)


def index(request):
    return render(request,'index.html')