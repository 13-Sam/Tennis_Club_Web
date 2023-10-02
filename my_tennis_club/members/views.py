from django.shortcuts import render
from django.http import HttpResponse
from . models import Members
# Create your views here.

def members(request):
    members = Members.objects.all()
    
    dict = {'members': members}
    return render(request, 'member_list.html', context=dict)

def member_details(request, pk):
    member = Members.objects.get(id=pk)
    dict = {'member':member}
    return render(request, 'member_details.html', context=dict)

def main(request):
    dict = {}
    return render(request, 'main.html', context=dict)

def testing(request):
    dict = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }
    return render(request, 'test.html', context=dict)