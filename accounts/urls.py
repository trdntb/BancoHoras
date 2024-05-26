from django.urls import path
from .views import register, login, logout, view_funcionarios, back_to_home, home_page

urlpatterns = [
    path('', home_page, name='home'),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("view_funcionarios/", view_funcionarios, name="view_funcionarios"),
    path('backtohome/', back_to_home, name='back_to_home')
]
