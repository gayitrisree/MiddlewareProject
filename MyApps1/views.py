from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page_view(request):
        return HttpResponse('<h1>Hello This is from home page view</h1><hr />')


# Create your views here.
def home_page_view2(request):
	print(10/0)
	return HttpResponse('<h1>Hello This is from home page view</h1><hr />')
def home_page_view3(request):
	print('This line printed by home_page_view3 function...')
	return HttpResponse('<h1>Hello this is from home page view3 </h1><hr />')


