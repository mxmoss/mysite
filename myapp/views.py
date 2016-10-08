from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello, world. You're at the myapp index.")
	
def post_list(request):
    return render(request, 'myapp/post_list.html', {})