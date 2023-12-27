from django.shortcuts import render, redirect

from django.http import HttpResponse

def homepage(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        # Save form data into the database
        student_obj = student(name=name, age=age, email=email, phone=phone, address=address)
        student_obj.save()

        # Optionally, you can redirect to a success page or render a template
        return HttpResponse('Form submitted successfully!')

    return render(request, 'form.html')



from django.shortcuts import render, get_object_or_404
from .models import student
from django.http import HttpResponse

def update_student(request, student_id):
    student_obj = get_object_or_404(student, id=student_id)

    if request.method == 'POST':
        # Retrieve form data from POST request
        student_obj.name = request.POST.get('name')
        student_obj.age = request.POST.get('age')
        student_obj.email = request.POST.get('email')
        student_obj.phone = request.POST.get('phone')
        student_obj.address = request.POST.get('address')

        # Save the updated data into the database
        student_obj.save()

        # Optionally, you can redirect to a success page or render a template
        return HttpResponse('Student updated successfully!')

    return render(request, 'update_student.html', {'student': student_obj})

def student_list(request):
    students = student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def delete_student(request, student_id):
    student_obj = get_object_or_404(student, id=student_id)

    if request.method == 'POST':
        # Delete the student instance
        student_obj.delete()
        return HttpResponse('Student deleted successfully!')

    return render(request, 'delete_student.html', {'student': student_obj})

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, UserLoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('homepage')  # Change to your desired redirect page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')  # Change to your desired redirect page
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})
