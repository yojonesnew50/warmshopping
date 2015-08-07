from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, RequestContext, Http404, HttpResponseRedirect, HttpResponse
from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory

from .models import UserPurchase
from .Forms import LoginForm


@login_required
def lib(request):
    try:
        products = request.user.userpurchase.products.all()
    except:
        products = None
    return render(request, "profiles/register.html", {"products": products })

def register (request): 
    if  request.user.is_authenticated():
                raise Http404 

    if request.method == 'POST':  # If the form has been submitted...
        form = RegisterationForm(request.POST, request.FILES)  # A form bound to the POST data
        if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                salt = sha.new(str(random.random())).hexdigest()[:5]
                confirmation_code = sha.new(salt + email).hexdigest()
                new_user = User.objects.create(username=username)
                new_user.set_password(password)
                new_user.is_active = False 
                new_user.save()
                user_profile = UserProfile(user=new_user , useremail=email , confirmation_code=confirmation_code)
                user_profile.save()
                send_confirmation_mail(email, confirmation_code , username)
                message = "A Confirmation mesage has sent to your email"
                return render (request , "messages.html", {"message": message} , context_instance=RequestContext(request))

    else:
        form = RegisterationForm()  # An unbound form

    return render(request , "register.html", {
        'form': form,
    }, context_instance=RequestContext(request))

def signup_confirm (request , confirm_code):
    profile = UserProfile.objects.get(confirmation_code=confirm_code)
    user = profile.user
    
    
    if user == None:
        raise Http404
    user_profile = UserProfile.objects.get(user=user)
    
    if  str (user_profile.confirmation_code) == str (confirm_code):
        user.is_active = True
        user_profile.confirmation_code = 'Confirmed'
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        user_profile.save()
        user.save()
        message = " Congratulation, your account has been verified " 
        return render (request , "messages.html", {"message": message} , context_instance=RequestContext(request))

    else:
        raise Http404

def signin(request):
    if  request.user.is_authenticated():
                raise Http404 

    error = ""
    if request.method == 'POST':  # If the form has been submitted...
        forma = LoginForm(request.POST or None)  # A form bound to the POST data
        if forma.is_valid() :  # All validation rules pass
            
            name = request.POST['username']
            password = request.POST['password']
            # ...
            user = authenticate(username=name, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
#                     if 'next' in request.POST:
#                         return  HttpResponseRedirect(request.POST['next'])
                    return HttpResponseRedirect("/")
                else:
                    error = "User hasn't been activated yet"
                    return render(request , "messages.html", {'form':forma, 'error':error }, context_instance=RequestContext(request))         
            else:
                    error = "Wrong user name or password"        
                    return render(request , "messages.html", {'form':forma, 'error':error, 'user':request.user, 'categories':Category.objects.all()  }, context_instance=RequestContext(request))

    else:
        forma = LoginForm()
        
    return render(request , "login.html", {'form':forma, 'error':error , 'user':request.user}, context_instance=RequestContext(request))
    
def signout (request):
    auth.logout(request)
    return HttpResponseRedirect('/')