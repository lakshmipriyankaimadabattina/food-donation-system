from django.http import HttpResponse
from .models import Page,bookedlist
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def send(request):
    if request.method=='POST':
        image = request.FILES.get('image')
        title = request.POST['title']
        phonenumber = request.POST['phonenumber']
        hmhrsback = request.POST['hmhrsback']
        quantity = request.POST['quantity']
        address = request.POST['address']


        k=Page(image=image, title=title, phonenumber=phonenumber, hmhrsback=hmhrsback, quantity=quantity, address=address)
        k.save()
    return render(request, "sender.html")
def receive(request):
    post = Page.objects.all()
    if request.method == 'POST':
	    username = request.form.POST.get('username')
	    m=bookedlist(username=username)
	    m.save()
    return render(request, "receiver.html", {'post' : post})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
def homepage_request(request):
     return render(request, "homepage.html")


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
