from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})


def blueprint(request):
	return render(request, 'blueprint.html', {})


def calc(request):
	return render(request, 'calc.html', {})


def mystyle(request):
	return render(request, 'mystyle.html', {})