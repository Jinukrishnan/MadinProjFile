from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import StudentCreationForm
from .models import Course, Department, Student


# Create your views here.

def Content(request):
    return render(request, 'Content.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cnfpwd = request.POST['cnfpwd']
        if pwd == cnfpwd:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "Username Already Taken")
                return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('/register')
            else:
                user = User.objects.create_user(username=user_name, password=pwd, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()

        else:
            messages.info(request, "Check and verify Your Pass word")
            return redirect('/register')
        return redirect('/login')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Entry')
            return redirect('/login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



def dpt(request, pk):
    dept=None
    if pk != None:
        dept = Department.objects.get(id=pk)
    return render(request, 'Department.html', {'dept': dept})



#
# def dpt(request, D_slug=None):
#     dept=None
#     if D_slug != None:
#         dept = Department.objects.get(D_slug=D_slug)
#     return render(request, 'Department.html', {'dept': dept})


def student_create_view(request):
    form = Department.objects.all()
    # form = StudentCreationForm()
    # if request.method == 'POST':
    #     form = StudentCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('student_add')

    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        genter = request.POST['genter']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['adress']
        department = request.POST.get('department',False)
        course = request.POST['course']
        purpose = request.POST['purpose']
        Material = request.POST['Material']
        print(department)
        user = Student.objects.create(name=name, dob=dob, age=age, genter=genter, phone=phone, email=email,
                                      address=address, department_id=department, course_id=course, Purpose=purpose,
                                      Material=Material)
        user.save
        return redirect("/")

    return render(request, 'home.html', {'form': form})


def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    # return render(request, 'home.html', {'courses': courses})
    return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
