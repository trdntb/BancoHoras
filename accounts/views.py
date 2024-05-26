from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django, logout as logout_django
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from accounts.models import Funcionarios
from django.contrib import messages


# Create your views here.


def home_page(req):
    return HttpResponseRedirect("/login")


def login(req):
    if req.method == "GET":
        return render(req, "accounts/login.html")
    username = req.POST.get("login_template")
    password = req.POST.get("password_template")

    user = authenticate(username=username, password=password)

    if user:
        login_django(request=req, user=user)
        return HttpResponseRedirect("/register")
    messages.error(req, "Credenciais inválidas. Por favor, tente novamente.")
    return HttpResponseRedirect("/login")


def logout(req):
    user = req.user
    if user:
        logout_django(req)
        return HttpResponseRedirect("/login")
    return HttpResponse("Erro!")


@login_required(login_url="/login")
def register(req):
    if req.method == "GET":
        return render(req, "accounts/register.html")

    nome_completo = req.POST.get("nome_completo")
    horario_entrada = req.POST.get("horario_entrada")
    horario_saida = req.POST.get("horario_saida")

    if nome_completo and horario_entrada and horario_saida:
        funcionario = Funcionarios(
            nome_completo=nome_completo,
            horario_entrada=horario_entrada,
            horario_saida=horario_saida,
        )
        funcionario.save()
        messages.success(req, 'Funcionário adicionado com sucesso.')
        return HttpResponseRedirect("/register")
    return HttpResponse("Erro ao salvar!!!")


@login_required(login_url="/login")
def view_funcionarios(req):
    if req.method == "POST":
        funcionarios = Funcionarios.objects.all()
        return render(
            req, "accounts/index.html", context={"funcionarios": funcionarios}
        )
    return HttpResponse("Erro ao mostrar funcionários!")


@login_required(login_url="/login")
def back_to_home(req):
    return HttpResponseRedirect("/register")
