from django.conf import settings
from django.core.mail import send_mail
def Mail_Sent():
    name="Balu"
    subject = 'welcome to BudgetBoss'
    message = f'Hi, thank you for registering in BudgetBoss.Your otp is 112233'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['venkatasairamreddy0404@gmail.com', ]
    print(email_from,recipient_list,message,email)
    send_mail(subject, message, email_from, recipient_list,fail_silently=False)
    print("Hii")
Mail_Sent()