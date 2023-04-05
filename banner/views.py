from django.shortcuts import render, redirect
from .forms import signupForm, updateform, notesForm, feedbackForm
from .models import usersignup, mynotes, feedback
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from bannerinfonem import settings
import requests

# Create your views here.


def index(request):
       user = request.session.get('user')
       if request.method == 'POST':
          if request.POST.get('Signup') == 'Signup':

              newuser = signupForm(request.POST)
              if newuser.is_valid():
                newuser.save()
                print("signup sucessfully")

                # emali sending
                sub = "Thank you!"
                msg = f"Dear User\nThank you for your interest.\nNeed any help, \nContact us on +91 9601268814 | ravaiyahardik@gmail.com"
                from_ID = settings.EMAIL_HOST_USER
                to_ID = [request.POST['username']]
                send_mail(subject=sub, message=msg,
                          from_email=from_ID, recipient_list=to_ID)

              else:
                print(newuser.errors)
          elif request.POST.get('login') == 'login':
              unm = request.POST['username']
              pas = request.POST['password']
              user = usersignup.objects.filter(username=unm, password=pas)
              uid = usersignup.objects.get(username=unm)
              print("userid:", uid, id)
              if user:
                  print("login sucessfully")
                  request.session['user'] = unm
                  request.session['uid'] = uid.id

                  return redirect(notes)
              else:
                  print("Error! does not match username and passwoed")

       return render(request, 'index.html', {'user': user})


def con(request):
    user = request.session.get('user')
    if request.method == 'POST':
        if request.POST.get('Signup') == 'Signup':
              newuser = signupForm(request.POST)
              if newuser.is_valid():
                newuser.save()
                print("signup sucessfully")
              else:
                print(newuser.errors)
        elif request.POST.get('login') == 'login':
              unm = request.POST['username']
              pas = request.POST['password']
              user = usersignup.objects.filter(username=unm, password=pas)
              uid = usersignup.objects.get(username=unm)
              print("userid:", uid, id)
              if user:
                  print("login sucessfully")
                  request.session['user'] = unm
                  request.session['uid'] = uid.id
                  return redirect(notes)
              else:
                  print("Error! does not match username and passwoed")
        elif request.POST.get('contact') == 'contact':
                newfeedback = feedbackForm(request.POST)
                if newfeedback.is_valid():
                    newfeedback.save()
                    print("Your feedback has been sent!")

            # Email Sending Code
            # send_mail(subject="Thank you!",message=f"Dear User\nWe got your feedback,\nThank you for your interest.\nNeed any help, \nContact us on +91 9724799469 | sanket@gmail.com",from_email=settings.EMAIL_HOST_USER,recipient_list=['komaldarjiv@gmail.com','jotangiyabinal17@gmail.com','nenshibhanderi885@gmail.com','asodariyarutvi@gmail.com','adimandaliya03@gmail.com','smitbhatti30@gmail.com','patelbhumil8666@gmail.com'])
                    sub="Thank you!"
                    msg=f"Dear User\nWe got your feedback,\nThank you for your interest.\nNeed any help, \nContact us on +91 9601268814 | ravaiyahardik@gmail.com"
                    from_ID=settings.EMAIL_HOST_USER
                    to_ID=[request.POST['email']]
                    send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)

    return render(request , 'contact.html',{'user':user})

def about(request):
    user=request.session.get('user')
    return render(request  ,'about.html',{'user':user})


def notes(request):
    user=request.session.get('user')
    if request.method=='POST':
        abcd=notesForm(request.POST,request.FILES)
        if abcd.is_valid():
            abcd.save()
            print("Your notes has been uploaded!")

            
            
        else:
            print(abcd.errors)
    return render(request  ,'notes.html',{'user':user})



def Profile(request):
   user=request.session.get('user')
   uid=request.session.get('uid')
   cid=usersignup.objects.get(id=uid)
   if request.method=='POST':
       update=signupForm(request.POST)
       if update.is_valid():
           updateuser=signupForm(request.POST,instance=cid)
           update.save()
           print("your profile is updated")
       else:
        print(update.errors) 
   return render(request,'profile.html',{'user':user,'uid':usersignup.objects.get(id=uid)})

def userlogout(request):
    logout(request)
    return redirect('/')