from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1':"This is sent"}
    return render(request,'index.html',context)

def services(request):
     return render(request,'services.html')

def donation(request):
     return render(request,'donation.html')

def inventory(request):
     return render(request,'inventory.html')

def alerts(request):
     return render(request,'alerts.html')
