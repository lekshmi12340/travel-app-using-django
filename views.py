from django.core.mail import EmailMessage
from django.shortcuts import render
from django.http import HttpResponse
from .forms import mailsendingform, signupform,destinationdetails,blogreplydetails,joinform
from .models import person,destinations,blogreply,join


def home(request):
    return HttpResponse('Hello world')

def about(request):
    return render(request,'travelapp/about.html')
def subscribe(request):
    return render(request,'travelapp/subscribe.html')
def blog(request):
    return render(request,'travelapp/blog.html')
def contact(request):
    return render(request,'travelapp/contact.html')
def destination_details(request):
    return render(request,'travelapp/destination_details.html')
def elements(request):
    return render(request,'travelapp/elements.html')
def index(request):
    return render(request,'travelapp/index.html')
def main(request):
    return render(request,'travelapp/main.html')
def singleblog(request):
    return render(request,'travelapp/single-blog.html')
def travel_destination(request):
    return render(request,'travelapp/travel_destination.html')
def index(request):
    return render(request,'travelapp/index.html')

def loginn(request):
    return render(request,'travelapp/login.html')
def mailsending(request):
    form=mailsendingform
    if request.method=="POST":
        form=mailsendingform(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_mail = form.cleaned_data['from_mail']
            to_mail = form.cleaned_data['to_mail']

            email=EmailMessage(subject,message,from_mail,[to_mail])
            email.send()
            return HttpResponse('Email send successfully')
    else:

        form=mailsendingform()
    return render(request,'travelapp/contact.html',{'form':form})
def signup(request):
    form = signupform()

    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            dateofbirth = form.cleaned_data['dateofbirth']
            contactnumber = form.cleaned_data['contactnumber']
            country = form.cleaned_data['country']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            idproofnumber = form.cleaned_data['idproofnumber']
            Person=person()
            Person.firstname=firstname
            Person.lastname = lastname
            Person.dateofbirth= dateofbirth
            Person.contactnumber= contactnumber
            Person.country= country
            Person.address = address
            Person.password = password
            Person.idproofnumber= idproofnumber
            Person.save()
            return render(request,'travelapp/signupconfirm.html')

    return render(request,'travelapp/signup.html',{'form':form})
def login(request):
    if request.method=="POST":
        firstname=request.POST.get("firstname")
        password=request.POST.get("password")
        print(firstname,password)
        userdata=person.objects.filter(firstname=firstname,password=password)
        if userdata:
            form=signupform()
            return render(request,'travelapp/travellersdata.html')

    return render(request,'travelapp/signup.html')
def destiny(request):
    form=destinationdetails()
    if request.method=='POST':
        form=destinationdetails(request.POST)
        if form.is_valid():
            wheretogo=form.cleaned_data['wheretogo']
            date = form.cleaned_data['date']
            traveltype = form.cleaned_data['traveltype']
            Destiny=destinations()
            Destiny.wheretogo=wheretogo
            Destiny.date = date
            Destiny.traveltype = traveltype
            Destiny.save()
            return HttpResponse("Form submitted successfully")
    return render(request,'travelapp/travel_destination.html',{'form':form})
def availability(request):
    if request.method=="GET":
        wheretogo=request.POST.get("wheretogo")

        traveltype=request.POST.get('traveltype')

        print(wheretogo,traveltype)
        userdata=destinations.objects.filter(wheretogo='California',traveltype='Advance')
        if userdata:
            form=destinationdetails()
            return render(request,"travelapp/availability.html")

    return render(request,'travelapp/redirect.html')

def breply(request):
    form=blogreplydetails()
    if request.method=='POST':
        form=blogreplydetails(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            website = form.cleaned_data['website']
            blog=blogreply()
            blog.comment=comment
            blog.name=name
            blog.email=email
            blog.website=website
            blog.save()
            return HttpResponse("Form submitted successfully")
    return render(request,'travelapp/blogreply.html',{'form':form})
def joindetails(request):
    form=joinform()
    if request.method=='POST':
        form=joinform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phonenumber = form.cleaned_data['phonenumber']
            message = form.cleaned_data['website']
            joins=join()
            joins.name=name
            joins.phonenumber=phonenumber
            joins.message=message
            joins.save()
            return HttpResponse("Form submitted successfully")
    return render(request,'travelapp/blogreply.html',{'form':form})








# Create your views here.
