from django.shortcuts import render

def index(request):
	context={}
	return render(request, 'myapp/error-authenticate.html', context)