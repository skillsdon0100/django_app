from django.shortcuts import render

# Create your views here.


def contact(request):
	context = {}
	template = 'contact.html'
	return render(request,template,context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request,template,context)
