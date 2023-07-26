from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . models import *
from . models import PublicAd
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from urllib.parse import urlparse, urlunparse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login ,logout
from decimal import Decimal
@login_required

@login_required
def maintiance(request, id, name):
    user = Employe.objects.get(name=name)
    typebreak = TypeBreaks.objects.all()
    Maintainace = Maintainaces.objects.all().filter(device_id=id)
    devices = Device.objects.filter(Employe=user).select_related('TypeDevice', 'RamDevice', 'StorgeDevice', 'Employe', 'Employe__PublicAd', 'RamDevice__type', 'StorgeDevice__type')
    print(devices)
    return render(request, 'maintaince.html', {'devices': devices,'user':user,'typebreak':typebreak,'Maintainace':Maintainace})

def tablemain(request,id,name):
    Maintainace = Maintainaces.objects.all().filter(device_id=id)
    total_cost = Maintainaces.objects.filter(device_id=id).aggregate(sum_cost=Sum('cost'))['sum_cost'] or 0 

    return render(request,'tablemain.html',{'Maintainace':Maintainace,'total_cost':total_cost})
    

def welcome(request):
    return render(request,'welcome.html',{})

@login_required
def index(request):
    all_emp = Employe.objects.all()
    all_tyepram = TypeRamHard.objects.all()
    typedevice = TypeDevice.objects.all()
    ram = RamDevice.objects.all()
    storage = StorgeDevice.objects.all()



    return render(request,'index.html',{'all_emp':all_emp,
                                        'all_tyepram':all_tyepram,'typedevice':typedevice,'ram':ram,'storage':storage
                                        })

@login_required
def table(request):
 all_device = Device.objects.select_related('TypeDevice', 'RamDevice', 'StorgeDevice', 'Employe', 'Employe__PublicAd', 'RamDevice__type', 'StorgeDevice__type').all() 
 return render(request,'table.html',{'all_device':all_device})


@login_required
def indexpa(request):
    
    return render(request,'addpa.html',{})
@login_required
def insertpa(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pa = PublicAd(name=name)
        pa.save()
        return HttpResponse(status=200)  
    else:
        return HttpResponse(status=400) 
     
    
@login_required
def tablepa(request):
    all_public_ads = PublicAd.objects.all()
    return render(request,'tablepa.html',{'all_public_ads':all_public_ads})

@login_required
def indexemp(request):
    Publicad = PublicAd.objects.all()
    return render(request,'empindex.html',{'Publicad':Publicad})

@login_required
def tableemp(request):
    all_employe = Employe.objects.select_related('PublicAd').all()
    return render(request,'tableemp.html',{'all_employe':all_employe})
@login_required
def insertemp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        empnumber = request.POST.get('empnumber')
        location = request.POST.get('location')
        PublicAd_id = int(request.POST['pubad'])
        print(PublicAd_id)
        public_ad = PublicAd.objects.get(id=PublicAd_id)
        print(public_ad)
        
        pa = Employe(name=name, phone=phone, empnumber=empnumber, PublicAd=public_ad,location=location)
        pa.save()
        return HttpResponse(status=200)  
    else:
        return HttpResponse(status=400)
    

@login_required
def deletepa(request, id):
    user = request.user
    if request.method == 'DELETE':
        try:
            data = PublicAd.objects.get(id=id)
           
            data.delete()

       
       

            return JsonResponse({'message': 'Record deleted successfully'})
        except PublicAd.DoesNotExist:
            return JsonResponse({'message': 'Record does not exist'})
    else:
        return JsonResponse({'message': 'Invalid request method'})       
    
@login_required
def deleteemp(request, id):
    user = request.user
    if request.method == 'DELETE':
        try:
            data = Employe.objects.get(id=id)
           
            data.delete()

       
       

            return JsonResponse({'message': 'Record deleted successfully'})
        except PublicAd.DoesNotExist:
            return JsonResponse({'message': 'Record does not exist'})
    else:
        return JsonResponse({'message': 'Invalid request method'})  


@login_required
def editpa(request,id):
    all_pa = PublicAd.objects.get(id=id)
    return render(request,'editpa.html',{'all_pa':all_pa})

@login_required
def updatepa(request,id):
      if request.method == 'POST':  
        data = PublicAd.objects.get(id=id)
        print(data)
        data.name = request.POST.get('name')
    
        data.save()
        return JsonResponse({'success': True})
      
      return JsonResponse({'success': False})

@login_required
def editemp(request,id):
    all_emp = Employe.objects.get(id=id)
    all_pa = PublicAd.objects.all()
    return render(request,'editemp.html',{'all_pa':all_pa,'all_emp':all_emp})
@login_required
def updateemp(request,id):
      if request.method == 'POST':  
        data = Employe.objects.get(id=id)
        data.name = request.POST.get('name')
        data.phone = request.POST.get('phone')
        data.empnumber = request.POST.get('empnumber')
        data.location = request.POST.get('location')
        data.PublicAd_id = request.POST.get('pubad')

    
        data.save()
        return JsonResponse({'success': True})
      
      return JsonResponse({'success': False})
@login_required
def insertdevice(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        empnumber = request.POST.get('empnumber')
        PublicAd_id = int(request.POST['pubad'])
        print(PublicAd_id)
        public_ad = PublicAd.objects.get(id=PublicAd_id)
        print(public_ad)
        
        pa = Employe(name=name, phone=phone, empnumber=empnumber, PublicAd=public_ad)
        pa.save()
        return HttpResponse(status=200)  
    else:
        return HttpResponse(status=400)
@login_required   
def insert(request):
    if request.method == 'POST':
        serialnumber = request.POST.get('serialnumber')
        modal = request.POST.get('modal')
        date = request.POST.get('date')
        cpu = request.POST.get('cpu')
        rate = request.POST.get('rate')
        typedevice_id = request.POST.get('typedevice')
        ramdevice_id = request.POST.get('ramdevice')
        employe_id = request.POST.get('employe')
        storagedevice_id = request.POST.get('storagedevice')

        try:
            typedevice = TypeDevice.objects.get(id=typedevice_id)
            ramdevice = RamDevice.objects.get(id=ramdevice_id)
            employe = Employe.objects.get(id=employe_id)
            storagedevice = StorgeDevice.objects.get(id=storagedevice_id)

            device = Device(
                serialnumber=serialnumber,
                modal=modal,
                cpu=cpu,
                rate=rate,
                date=date,
                TypeDevice=typedevice,
                RamDevice=ramdevice,
                Employe=employe,
                StorgeDevice=storagedevice
            )
            device.save()

            return HttpResponse("Data inserted successfully.", status=200)
        except (TypeDevice.DoesNotExist, RamDevice.DoesNotExist, Employe.DoesNotExist, StorgeDevice.DoesNotExist):
            return HttpResponse("Invalid data provided.", status=400)
    else:
        return HttpResponse("Invalid request method.", status=405)
    


@login_required
def deletedevice(request, id):
    user = request.user
    if request.method == 'DELETE':
        try:
            data = Device.objects.get(id=id)
           
            data.delete()

       
       

            return JsonResponse({'message': 'Record deleted successfully'})
        except PublicAd.DoesNotExist:
            return JsonResponse({'message': 'Record does not exist'})
    else:
        return JsonResponse({'message': 'Invalid request method'})  

@login_required
def details(request, id, name):
    user = Employe.objects.get(name=name)
    device = Device.objects.filter(Employe=user).select_related('TypeDevice', 'RamDevice', 'StorgeDevice', 'Employe', 'Employe__PublicAd', 'RamDevice__type', 'StorgeDevice__type')
    return render(request, 'details.html', {'device': device,'user':user})    

@login_required
def edit(request,id):
    device = Device.objects.select_related('TypeDevice', 'RamDevice', 'StorgeDevice', 'Employe', 'Employe__PublicAd', 'RamDevice__type', 'StorgeDevice__type').get(id=id)
    types = TypeDevice.objects.all() 
    all_device = Device.objects.get(id=id)
    ram = RamDevice.objects.all()
    storage = StorgeDevice.objects.all()
    return render(request,'editdevice.html',{'device':device,'types':types,'ram':ram,'storage':storage,'all_device':all_device})
@login_required
def updatedevice(request, id):
    device = get_object_or_404(Device, pk=id)
    if request.method == 'POST':
        
        device.serialnumber = request.POST['serialnumber']
        device.modal = request.POST['modal']
        device.cpu = request.POST['cpu']
        device.rate = request.POST['rate']
        device.date = request.POST['date']
        device.TypeDevice_id = request.POST['typedevice']
        device.RamDevice_id = request.POST['ramdevice']
        device.StorgeDevice_id = request.POST['storagedevice']
        device.save()
        return JsonResponse({'success': True})
      
    return JsonResponse({'success': False}) 




def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
       
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                # Validate and sanitize the next_url to prevent open redirects
                parts = urlparse(next_url)
                if not parts.netloc:
                    return redirect(urlunparse(('', '', parts.path, parts.params, parts.query, parts.fragment)))
            return redirect('/')
           
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'accounts/login.html')



def logout_user(request):
    logout(request)
    return redirect('login/')



@login_required
def insertmain(request,id,name):
    if request.method == 'POST':
        stpes = request.POST.get('steps')
        cost = request.POST.get('cost')
        datein = request.POST.get('datein')
        dateout = request.POST.get('dateout')

        typebreak_id = int(request.POST['typebreak'])
      
        typebreak = TypeBreaks.objects.get(id=typebreak_id)
        try:
            datein = datetime.strptime(datein, '%Y-%m-%d').date() if datein else None
            dateout = datetime.strptime(dateout, '%Y-%m-%d').date() if dateout else None
        except ValueError:
            return HttpResponse('Invalid date format', status=400)
        
        pa = Maintainaces(stpes=stpes, cost=cost, datein=datein, dateout=dateout,TypeBreak_id=typebreak_id,device_id=id)
        print(pa)
        pa.save()
        return HttpResponse(status=200)  
    else:
        return HttpResponse(status=400)