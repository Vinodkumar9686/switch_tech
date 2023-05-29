
from django.contrib import admin
from django.urls import path,include
from . import views
from . import forms

urlpatterns = [
    path('', views.loginPage,name='login'),
    path('home/',views.home,name='home'),
    path('validate/',views.validate, name='validate'),
    path('api/get-quiz/',views.get_quiz,name='get_quiz'),
    path('api/result/',views.result,name='result'),
    path('quiz/',views.quiz,name='quiz'),
    path('logout/', views.logoutPage,name='logout'),
    path('api/save-remaining-time/', views.save_remaining_time, name='save_remaining_time'),
    # path('register/', views.registerPage,name='register'),
    path('skipquiz/', views.skip_quiz, name='skipquiz'),
    path('final/',views.final,name='final'),
]

admin.site.site_header = "Switch Tech System Admin"
admin.site.site_title = "Switch Tech System Admin Portal"
admin.site.index_title = "Welcome to Admin Portal"
# urlpatterns = [
#     path('',views.loginPage,name='login'),
#     path('home/',views.jotQuiz,name='home'),
#     path('logout/', views.logoutPage,name='logout'),
#     path('register/', views.registerPage,name='register')
# ]
