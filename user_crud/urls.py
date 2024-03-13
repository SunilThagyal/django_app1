from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('login',(views.login_view),name="login"),
    path('signup',views.signup,name="signup"),
    path('',login_required(views.index), name='index'),
    path('logout/',(views.logout_view), name='logout'),
    path('create/',login_required(views.create), name='create'),
    path('update/<int:id>',login_required(views.update), name='update'),
    path('delete/<int:id>/',login_required(views.delete), name='delete'),
]