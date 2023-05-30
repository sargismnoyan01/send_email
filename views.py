from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import *
from .forms import *
from django.core.mail import EmailMessage
from lship.settings import EMAIL_HOST_USER



class Exp(ListView):
    template_name='exp.html'


    def get(self,request):
        form=ConForm()
            
            



        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=ContForm(request.POST)
        subject='Նոր նամակ Leadership-ից'

        body=f" Բարև հարգելի {request.POST['name']}, ձեր կարծիքը կարևոր է մեզ համար"

        try:
            form.save()
            email=EmailMessage(
            subject=subject,
            body=body,
            from_email=EMAIL_HOST_USER,
            to=[request.POST.get('email')]
            )
            email.send()
            return redirect('home')
        except Exception:
            form=ContForm()




        return render(request,self.template_name,{'form':form})
    
