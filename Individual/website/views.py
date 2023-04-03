from django.shortcuts import render,HttpResponseRedirect
from .models import Register_Login,Transaction_History,Query
from .forms import Register_Details,Transaction_History_Details,Query_submit
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
import math
from . import utils
from django.db.models import Sum
import random
from django.conf import settings
from django.core.mail import send_mail
import json
from . import Security
from django.http import *
def navbar(request):
    try:
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session and request.session['session_id']==xe.id:
            return render(request,"navbar.html",{'x2':xe.role})
        return render(request,'Sessiontimeout.html')
    except:
        return render(request,'Sessiontimeout.html')
def Register(request):
    global k1
    global form1
    email=request.POST.get("email")
    r=Register_Login.objects.filter(email=email)
    if r:
        return render(request,'Register.html',{'m':"Email Already Found!!Try with another Id"})
    elif request.method=="POST":
        form1=Register_Details(request.POST or None)
        x=Register_Login.objects.all
        print(x)
        if form1.is_valid:
            name="Balu"
            subject = 'welcome to BudgetBoss'
            k1=generateOTP()
            print(k1)
            message ='Hi, thank you for registering in BudgetBoss.Your otp is '+k1
            email_from = settings.EMAIL_HOST_USER
            recipient_list =email
            send_mail(subject, message, email_from, [recipient_list],fail_silently=False)
            return render(request,'otp_v.html')
    else:
        return render(request,'Register.html')
def Login(request):
    if request.method=='POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        user=Register_Login.objects.filter(email=email,password=password).values()
        d=list(user.values_list('id'))
        if user :
            request.session.clear_expired() 
            x11=request.session['session_id']=d[0][0]
            x2=Register_Login.objects.get(id=d[0][0])
            x=Transaction_History.objects.filter(id1=d[0][0])
            Total_credit=0
            Total_debit=0
            for i in x:
                if i.type_amount=='debit':
                    Total_debit=Total_debit+int(i.amount)
                else:
                    Total_credit=Total_credit+int(i.amount)
            return render(request,'homepage.html',{'x':d[0][0],'y':Total_credit,'z':Total_debit,'w':x2.balance,'x2':x2})
        else:
            return render(request,'Login.html' ,{'message':"Invalid Credentials"})
    return render(request,'Login.html')
def main(request):
    return render(request,"main.html")
def home(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session and request.session['session_id']==xe.id:
            x=Transaction_History.objects.filter(id1=id)
            Total_credit=0
            Total_debit=0
            for i in x:
                if i.type_amount=='debit':
                    Total_debit=Total_debit+int(i.amount)
                else:
                    Total_credit=Total_credit+int(i.amount)
            return render(request,'homepage.html',{'x':id,'y':Total_credit,'z':Total_debit,'w':xe.balance})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def transaction(request):
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            xe=Transaction_History.objects.filter(id1=id).values('type_amount').annotate(balance=Sum('amount')).order_by('-type_amount')
            xe1=Transaction_History.objects.filter(id1=id).values('category').annotate(balance=Sum('amount')).order_by('-category')
            xe2=Transaction_History.objects.filter(id1=id).values('id1').annotate(balance=Sum('balance')).order_by('-id')
            xe3=Transaction_History.objects.filter(id1=id).values('month_name').annotate(balance=Sum('amount')).order_by('-month_name')
            print(xe3)
            return render(request,'transaction.html',{'data':xe,'data1':xe1,'data2':xe2,'data3':xe3})
        return render(request,'Sessiontimeout.html')
def finance(request):
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            return render(request,'finance.html',{'x':id})
        return render(request,'Sessiontimeout.html')
def query(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            return render(request,'query.html',{'x':id})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def credit(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            return render(request,'credit.html',{'x':id})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def profile(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x1=Register_Login.objects.get(id=id)
            return render(request,'profile.html',{'x':id,'x1':x1})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(5):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP
def edit(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x1=Register_Login.objects.get(id=id)
            return render(request,'edit.html',{'x':id,'x1':x1})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def editorder(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x1=Register_Login.objects.get(id=id)
            name= request.POST.get("name")
            age= request.POST.get("age")
            balance=request.POST.get("balance")
            x1.name=name
            x1.age=age
            x1.balance=balance
            x1.save()
            return render(request,'profile.html',{'x':id,'x1':x1})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def insert(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x1=Register_Login.objects.get(id=id)
            return render(request,'insert.html',{'x':id,'x1':x1})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def insertData(request):
    try:
        idx=request.session.get('session_id')
        xe=Register_Login.objects.get(id=idx)
        print(idx)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            if request.method=="POST":
                form=Transaction_History_Details(request.POST or None)
                if form.is_valid:
                    x1=Register_Login.objects.get(id=idx)
                    a=request.POST.get("category")
                    s=request.POST.get("type_amount")
                    b=request.POST.get("amount")
                    balance=request.POST.get("balance")
                    if(s=='credit'):
                        x=int(balance)+int(b)
                        x1.balance=str(x)
                    else:
                        x=int(balance)-int(b)
                        x1.balance=str(x)
                    form.save()
                    x1.save()
                    x2=Register_Login.objects.get(id=idx)
                    return render(request,'submit.html',{'x':idx,'x11':x2})
            else:
                return render(request,'insert.html',{})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def passbook(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x=Transaction_History.objects.filter(id1=id)
            y=Register_Login.objects.get(id=id)
            Total_credit=0
            Total_debit=0
            for i in x:
                if i.type_amount=='debit':
                    Total_debit=Total_debit+int(i.amount)
                else:
                    Total_credit=Total_credit+int(i.amount)
            return render(request,'Passbook.html',{'x':id,'all':x,'yy':y.balance,'t_d':Total_debit,'t_c':Total_credit})
        else:
            return render(request,'Sessiontimeout.html')
    except:
        return render(request,'Sessiontimeout.html')

def submit(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        email=xe.email
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            if request.method=='POST':
                form=Query_submit(request.POST or None)
                if form.is_valid:
                    form.save()
                    subject = 'Query Confirmation'
                    message ='Hello User,We recieved your query.We will work on it.Thank You!!'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list =email
                    send_mail(subject, message, email_from, [recipient_list],fail_silently=False)
                return render(request,"submit.html",{'x':id})
        return render(request,'Sessiontimeout.html')
    except :
        return render(request,'Sessiontimeout.html')
def submit1(request):
    # x=request.post.get('credit_amount')
    # print(x)
    return render(request,"submit.html",{'x':id})
def logout(request):
    try:
        request.session.flush()
        return render(request,'login.html')
    except :
        return render(request,'Sessiontimeout.html')
def users1(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            xe=Register_Login.objects.get(id=id)
            x=Register_Login.objects.all
            print(x)
            return render(request,'Users.html',{'x':id,'x1':x,'x2':xe})
        else:
            return render(request,'Sessiontimeout.html')
    except:
        return render(request,'Sessiontimeout.html')
def trans(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            x=Transaction_History.objects.all
            return render(request,'Trans.html',{'x':id,'x1':x,'x2':xe})
        else:
            return render(request,'Sessiontimeout.html')
    except:
        return render(request,'Sessiontimeout.html')
def query1(request):
    try:
        id=request.session['session_id']
        xe=Register_Login.objects.get(id=id)
        if 'session_id' in request.session  and request.session['session_id']==xe.id:
            xe=Register_Login.objects.get(id=id)
            x=Query.objects.all

            return render(request,'query_all.html',{'x':id,'x1':x,'x2':xe})
        else:
            return render(request,'Sessiontimeout.html')
    except:
        return render(request,'Sessiontimeout.html')
def otp_verification(request):
    rr=request.POST.get('ist')+""+request.POST.get('sec')+""+request.POST.get('third')+""+request.POST.get('fourth')+""+request.POST.get('fifth')
    if(rr==k1):
        form1.save()
        return render(request,'login.html')
    else:
        return render(request,'otp_v.html')


