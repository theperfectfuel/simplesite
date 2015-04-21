from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from simplesite.forms import LoginForm

def home(request):
	return render_to_response('index.html')

def about(request):
	return render_to_response('about.html')

def login(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = auth.authenticate(username=username, password=password)
			if user is not None:
				auth.login(request, user)
				return HttpResponseRedirect('/accounts/loggedin')
			else:
				message = "Invalid username and / or password, try again."
	else:
		form = LoginForm()
	return render_to_response('registration/login.html', {'message': message, 'form': form}, context_instance=RequestContext(request))

def loggedin(request):
	return render_to_response('registration/loggedin.html', {'username': request.user.username})

def logout(request):
	auth.logout(request)
	return render_to_response('registration/logged_out.html')