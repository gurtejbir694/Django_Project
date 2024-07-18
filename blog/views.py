from django.shortcuts import render, redirect
from . models import *
# Create your views here.
def home(request):
    cname = "Home"
    prod = product.objects.filter(cat__name="Home")
    return render(request, 'blog/index.html', {'prods': prod, 'link': cname})

def contact(request):
    if request.method == "POST":
        name_ = request.POST['name']
        email_ = request.POST['email']
        sub_ = request.POST['subject']
        mesg_ = request.POST['message']
        Contact.objects.create(name=name_, email=email_, subject=sub_, message=mesg_, answer="Pending")
        return redirect("/")

    return render(request, 'blog/contact.html')

def signin(request):
    if request.method == "POST":
        fName = request.POST['fname']
        lName = request.POST['lname']
        uName = request.POST['uname']
        eMail = request.POST['email']
        passWD = request.POST['passwd']
        cPassWD = request.POST['cpasswd']
        if registration.objects.filter(email_id=eMail):
            mesg = "Email ID already exits"
            return render(request, 'blog/signin.html', {'msg': mesg})
        elif registration.objects.filter(userid=uName):
            mesg = "This username is taken. Please enter another one"
            return render(request, 'blog/signin.html', {'msg': mesg})
        elif cPassWD != passWD:
            mesg = "Confirm Password and Password do not Match!!"
            return render(request, 'blog/signin.html', {'msg': mesg})
        else:
            registration.objects.create(first_name=fName, last_name=lName, userid=uName, email_id=eMail, password=passWD)
            mesg = "You are signed in. Go to Homepage"
            return render(request, 'blog/signin.html', {'msg': mesg})
            
    return render(request, 'blog/signin.html')

def login(request):
    if request.method == "POST":
        emid = request.POST['email']
        pswd = request.POST['passwd']
    
        if registration.objects.filter(email_id=emid) and registration.objects.filter(password=pswd):
            request.session['email'] = emid
            return redirect("/")
        else:
            mesg = "Incorrect Credentials"
            return render(request, 'blog/login.html', {'msg': mesg})
    return render(request, 'blog/login.html')

def books(request):
    cat = categories.objects.all()
    return render(request, 'blog/categories.html', {'categ': cat})

def library(request, name):
    if categories.objects.filter(name=name):
        lib = product.objects.filter(cat__name=name)
        return render(request, 'blog/products.html', {'prod': lib, 'cat_name': name})

def details(request, cname, pname):
    if categories.objects.filter(name=cname):
        if product.objects.filter(name=pname):
            data = product.objects.filter(name=pname).first()
            return render(request, 'blog/details.html', {'book': data, 'cat_name': cname})

def authors(request):
    writer = author.objects.all()
    return render(request, 'blog/authors.html', {'auth': writer})

def about_author(request, aname):
    if author.objects.filter(name=aname):
        about = author.objects.filter(name=aname).first()
        novels= product.objects.filter(author=aname)
        return render(request, 'blog/adetails.html', {'record': about, 'auth_name': aname, 'more': novels})

def freeread(request):
        data = FreeBooks.objects.all()
        return render(request, 'blog/freeread.html', {'bk': data})


def search(request):
    s1 = request.GET['query']
    if product.objects.filter(name__icontains=s1):
        prod = product.objects.filter(name__icontains=s1)
        return render(request, "blog/search.html", {'que': prod})
          
    elif product.objects.filter(author__icontains=s1):
        prod = product.objects.filter(author__icontains=s1)
        return render(request, "blog/search.html", {'que': prod})
    
def read(request):
    if 'email' in request.session:
        return redirect("/")
    
def logout(request):
    del request.session['email']
    return redirect("/")


