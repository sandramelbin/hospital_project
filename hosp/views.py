from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import hospital
from .models import doctor
# Create your views here.

# Create your views here.
def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')
def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')

def adminview(request):
    return render(request,'adminview.html')

def doctorview(request):
    return render(request,'doctorview.html')

def base2(request):
    return render(request,'base2.html')

def admin_signup_view(request):
    if request.method == 'POST':
        f_name = request.POST.get("fname")
        l_name = request.POST.get("lname")

        uname = request.POST.get("uname")
        passw = request.POST.get("pwd")
        rec =hospital(first_name = f_name,last_name =l_name,user_name =uname,password =passw)
        rec.save()
        return render(request, 'adminsignup.html')

    return render(request, 'adminsignup.html')
def adminlogin(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pwd')
        print(username)

        check_user =hospital.objects.filter(user_name=username,password= password)

        if check_user:
            request.session['admin1'] = username

            return render(request ,'admindashboard.html')
        else:
            return HttpResponse('please enter valid username or password.')
    return render(request,'adminlogin.html')

def admin_dashboard(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        # for i in data:
        #     print(i.first_name)
        param = {
            'data' : data,
            'current_user': current_user
        }
        return render(request, 'admindashboard.html', param)

    return render(request, 'admindashboard.html')

def admin_dash1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        param = {
            'data' : data,
            'current_user': current_user,
            'admin_dash1' :1,
        }
        return render(request, 'admindashboard.html', param)
    else:
        return redirect ('adminlogin')

def doctor1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        param = {
            'data':data,
            'current_user': current_user,
            'doctor1':1,
        }
        return render(request, 'admindashboard.html', param)
    else:
        return redirect ('doctor1')

def patient1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        param = {
            'data': data,
            'current_user':current_user,
            'patient1': 1,
        }
        return render(request, 'admindashboard.html',param)
    else:
        return redirect('patient1')

def appointment1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        param = {
            'data': data,
            'current_user': current_user,
            'appointment1': 1,
        }
        return render(request, 'admindashboard.html', param)
    else:
        return redirect('appointment1')
def doctor_signup(request):
    if request.method == 'POST':
        f_name = request.POST.get('fname')
        print(f_name)
        l_name = request.POST.get('lastname')

        uname = request.POST.get('uname')
        passw = request.POST.get('password')
        department = request.POST.get('department')
        # print(department)

        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        f = request.POST.get('photo')
        rec = doctor(first_name=f_name, last_name=l_name, user_name=uname, password=passw,department=department,mobile=mobile,address=address,file=f)
        rec.save()
        return render(request, 'doctorsignup.html')
    return render(request, 'doctorsignup.html')

def doctor_login(request):
    if request.method == 'POST':

        username = request.POST.get('uname')
        password = request.POST.get('pwd')

        # print(username)
        check_user = doctor.objects.filter(user_name=username,password=password)
        if check_user:

            request.session["doctor1"] = username
            return redirect('doctordashboard')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'doctorlogin.html')

def approvedoctor(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = doctor.objects.filter(user_name=current_user)
        data2 = doctor.objects.all()
        param = {
            'data': data,
            'data2':data2,
            'current_user': current_user,
            'approvedoctor': 1,
        }
        return render(request, 'admindashboard.html', param)
    else:
        return redirect('admindashboard')
def approve_doc1(request):
    if 'admin1' in request.session:
        current_user = request.session['admin1']
        data = hospital.objects.filter(user_name=current_user)
        data2 = doctor.objects.all()
        param = {
            'data': data,
            'data2':data2,
            'current_user': current_user,
            'approve_doc1': 1,
        }
        return render(request, 'admindashboard.html', param)
    else:
        return redirect('admindashboard')