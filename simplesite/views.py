from django.shortcuts import render_to_response

def home(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def loggedin(request):
	return render_to_response('registration/loggedin.html', {'username': request.user.username})