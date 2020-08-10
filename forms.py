from django import forms
from . models import person,destinations,blogreply,join

class mailsendingform(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=50)
    from_mail = forms.CharField(max_length=50)
    to_mail = forms.CharField(max_length=50)

class signupform(forms.Form):
    firstname=forms.CharField(widget=forms.TextInput())
    lastname=forms.CharField(widget=forms.TextInput())
    GENDER_CHOICES=('male','male'),('female','female')
    gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    dateofbirth=forms.DateField()
    contactnumber=forms.IntegerField()
    country_choice=[('India','India'),('America','America'),('United Kingdom','United Kingdom')]
    country=forms.ChoiceField(choices=country_choice,widget=forms.RadioSelect())
    address=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())
    idproofnumber=forms.IntegerField(widget=forms.NumberInput)
class destinationdetails(forms.Form):
    wheretogo =forms.CharField(widget=forms.TextInput())
    date=forms.DateField()
    travel_choice=[('Advance','Advance'),('Premium','Premium')]
    traveltype=forms.ChoiceField(choices=travel_choice,widget=forms.RadioSelect())
class blogreplydetails(forms.Form):
    comment=forms.CharField(max_length=1000)
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    website=forms.CharField(max_length=100)
class joinform(forms.Form):
    name = forms.CharField(max_length=50)
    phonenumber=forms.IntegerField()
    message=forms.CharField(max_length=1000)







    
