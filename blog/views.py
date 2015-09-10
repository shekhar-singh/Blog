from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Register,UserEditPro,Post
from forms import UserForm,SignupForm,LoginForm,PostForm
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
            return HttpResponseRedirect('/blog/login/')
        else:
            form.errors

    else:
        form=SignupForm()

    return render(request,'blog/signup.html',{'form':form})

def login(request):
    try:
        if request.session['email']:
            return HttpResponseRedirect('/blog/profile_view/')
    except:
        pass
    if request.method == 'POST':
        form=LoginForm(request.POST) 
        if form.is_valid():
            try:
                user=Register.objects.filter(email=form.cleaned_data['email'],password=form.cleaned_data['password'])
                if len(user)==1:
                    request.session['email']=user[0].email
                    return HttpResponseRedirect('/blog/profile_view/')
                else:
                    return HttpResponse("Login fail   . Try again")
            except DoesNotExist:
                return None
    else:
        form=LoginForm()

        return render(request,'blog/login.html',{'form':form})


def profile_view(request):   
    if request.session['email']:
        a = Register.objects.get(email=request.session['email'])
        try:
            b=UserEditPro.objects.get(user=a)
        except:
            b=UserEditPro(user=a)
            b.save()
            b=UserEditPro.objects.get(user=a)
        return render(request,'blog/profile_view.html', {'profile':b})
    else:
        return HttpResponseRedirect('blog/login/')



def profile(request):
    if request.session['email']:
        if request.method=='POST':
            a=Register.objects.get(email=request.session['email'])
            try:
                b=UserEditPro.objects.get(user=a)
            except:
                b=UserEditPro(user=a)
                b.save()
                b=UserEditPro.objects.get(user=a)
            form=UserForm(request.POST,instance=b)
            if form.is_valid():
                f=form.save(commit=False)
                f.user=a
                f.save()
                return HttpResponseRedirect('/blog/login/')
            else:
                return render(request,'blog/profile.html',{'form':form})
        else:
            a=Register.objects.get(email=request.session['email'])
            try:
                b=UserEditPro.objects.get(user=a)
            except:
                b = UserEditPro(user=a)
                b.save()
                b=UserEditPro.objects.get(user=a)
            form=UserForm(instance=b)
            return render(request,'blog/profile.html',{'form':form})
    else:
        return HttpResponseRedirect('blog/login/')

def logout(request):
    del request.session['email']
    return HttpResponseRedirect('/blog/login/')

