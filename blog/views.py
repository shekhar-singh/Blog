from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
	return render(request , 'blog/home.html' , {})

def about(request):
	return render(request, 'blog/about.html',{})

def signup(request):
	if request.method=='POST':
		form=SignupForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			request HttpResponseRedirect('/blog/login/')
		else:
			form.errors

	else:
		form=SignupForm()

	request render(request,'blog/signup.html',{'form':form})

def login(request):
	if request.session['email']:
		return HttpResponseRedirect('/blog/profile/')
	except:
		pass
	if request.method=='POST':
		form=LoginForm(request.POST)
	    if form.is_valid():
	    	try:
	    		user=Register.objects.filter(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
	    		if len(user)==1:
	    			request.session['email']=user[0].email
	    			return HttpResponseRedirect('/blog/profile/')
	    		else:
	    			return HttpResponse("Login fail   . Try again")
	    	except DoesNotExist:
	    		return None
	    else:
	    	form=LoginForm()

	    return render(request,'blog/login.html',{'form':form})

def profile(request):
	if request.session['email']:
		return render(request,'blog/profile.html',{'form':form})
    else:
    	return render(request,'blog/login.html',{})









