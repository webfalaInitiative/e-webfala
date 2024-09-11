from django.shortcuts import render

# Create your views here.

# from django.shortcuts import redirect
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.views import LoginView

# class CustomLoginView(LoginView):
#     def form_valid(self, form):
#         user = form.get_user()
#         if user.role == 'USER':
#             return redirect('user_home')  # Redirect to user-specific home page
#         elif user.role == 'INSTRUCTOR':
#             return redirect('instructor_home')  # Redirect to instructor-specific home page
#         return super().form_valid(form)

# def register_user(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)
#             return redirect('home')  # Redirect to a success page
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register_user.html', {'form': form})

# def register_instructor(request):
#     if request.method == 'POST':
#         form = InstructorRegistrationForm(request.POST)
#         if form.is_valid():
#             instructor = form.save(commit=False)
#             instructor.set_password(form.cleaned_data['password'])
#             instructor.save()
#             login(request, instructor)
#             return redirect('home')  # Redirect to a success page
#     else:
#         form = InstructorRegistrationForm()
#     return render(request, 'register_instructor.html', {'form': form})