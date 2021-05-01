from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime
from dateutil.relativedelta import relativedelta
from .funcs import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def inquiry(request):
    return render(request, 'inquiry.html')


def contact_us(request):
    result = False
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        text = request.POST['text']
        message = Message(firstName=fname, lastName=lname, phoneNumber=phone, email=email, message=text)
        message.save()
        result = True
    return render(request, 'contactus.html', {'result': result})


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
        for pre_n in pre:
            product = Warranty.objects.filter(serialNumber=SN+pre_n)
            if len(product) == 1:
                product = product[0]
                break
            else:
                product = None
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
