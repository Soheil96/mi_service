from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
from django.conf import settings as conf_settings
from django.core.mail import send_mail
from .funcs import *
from .forms import CaptchaForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def inquiry(request):
    return render(request, 'inquiry.html')


def contact_us(request):
    result = False
    fname = lname = phone = email = text = serial = ''
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        serial = request.POST['serial']
        form = CaptchaForm(request.POST)
        if form.is_valid():
            message = Message(firstName=fname, lastName=lname, phoneNumber=phone, email=email, message=text, serialNumber=serial)
            message.save()
            email_message = fname + ' ' + lname + '\n' + phone + '\n' + email + '\n\n' + serial + '\n' + text
            send_mail(
                'گارانتی',
                email_message,
                conf_settings.DEFAULT_FROM_EMAIL,
                [conf_settings.DEFAULT_EMAIL_RECEIVER],
                fail_silently=False,
            )
            result = True
    else:
        form = CaptchaForm
    if result:
        fname = lname = phone = email = text = serial = ''
    return render(request, 'contactus.html', {'result': result, 'form': form, 'fname': fname, 'lname': lname,
                                              'phone': phone, 'email': email, 'text': text, 'serial': serial})


def terms_of_service(request):
    return render(request, 'termsofservice.html')


def result(request):
    product = None
    if request.method=='POST':
        SN = request.POST['warranty_number']
        product = Warranty.objects.filter(warrantyNumber=SN)
        if len(product) == 1:
            product = product[0]
        else:
            product = None
    return render(request, 'result.html', {'product': product})


def make_warranty(serial):
    newProduct = Warranty()
    newProduct.product = None
    newProduct.serialNumber = serial
    newProduct.endDate = date(2022, 5, 15)
    if '0502B0063' in serial and len(serial) == 13:
        newProduct.product = 'Solar ساعت هوشمند هایلو'
    if 'Q701A01B0' in serial and len(serial) == 18:
        newProduct.product = 'مشکی رنگ imilab kw66 ساعت هوشمند شیائومی'
    if '28818/A0Z9' in serial and len(serial) == 15:
        newProduct.product = 'مشکی mi watch lite ساعت هوشمند شیائومی'
    if '28818/B1QR1' in serial and len(serial) == 15:
        newProduct.product = 'مشکی mi watch lite ساعت هوشمند شیائومی'
    if newProduct.product is None:
        return None
    return newProduct


def result_1(request):
    product = None
    if request.method=='POST':
        post = ['', '(TH)']
        pre = ['', '28818/']
        SN = request.POST['serial_number'].replace(' ', '')
        for post_n in post:
            product = Warranty.objects.filter(serialNumber=SN+post_n)
            if len(product) == 1:
                product = product[0]
                break
            else:
                product = None
        if product is None:
            for pre_n in pre:
                product = Warranty.objects.filter(serialNumber=pre_n+SN)
                if len(product) == 1:
                    product = product[0]
                    break
                else:
                    product = None
        if product is None:
            product = make_warranty(SN)
    return render(request, 'result.html', {'product': product})


@login_required
def manager(request, serials=''):
    products = Warranty.objects.all()
    return render(request, 'manager.html', {'products': products, 'serials': serials.split('\r\n')})


@login_required
def add_warranty(request):
    if request.method == 'POST':
        serials = request.POST['serial_number'].split('\r\n')
        productName = request.POST['product']
        month = request.POST['length']
        startDate = datetime.strptime(request.POST['start_date'], '%Y-%m-%d').date()
        endDate = startDate + relativedelta(months=int(month))
        res = ""
        for serial in serials:
            if len(serial) > 5:
                SN = serial.replace(' ', '')
                res += SN + '\r\n'
                warrantyNumber = 'new-' + SN
                product = Warranty(serialNumber=SN, product=productName, length=month, startDate=startDate, endDate=endDate, warrantyNumber=warrantyNumber)
                product.save()
        return redirect(manager, res.replace('/', ''))
    return render(request, 'addwarranty.html')
