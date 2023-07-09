from django.shortcuts import render
from App.models import Employee
from django.http import JsonResponse

# Function to render Homepage
def home(request):
    employ_list = Employee.objects.all()
    return render(request,"home.html",{"employees":employ_list})

def show_data(request):

    # return JsonResponse(data,safe=False)
    return render(request,"data.html",{"data":data})