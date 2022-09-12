from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import User

def index(request):
    return render(request, 'index.html')  

def login(request):
    print(request.POST)
    if request.POST:
        login = request.POST["login"]
        # TODO: Add salt to hash. Now it's only a bit better than cleartext.
        password = request.POST["password"]
        found = False
        user = User.objects.filter(password=password,login=login)
        if user:
            found = True
        if not found:
            return JsonResponse({"status":"err", "id":-1},status=401)
        resp = JsonResponse({"status": "ok", "login":login,"password":password,"id":user[0].id})
        resp.set_cookie('token', login, max_age=86400)
        return resp
    else:
        return render(request, 'index.html')

def register(request):
    if request.POST:
        login = request.POST["login"]
        password = request.POST["password"]
        found = False
        user = User.objects.filter(login=login)
        if user:
            found = True
        if found:
            return JsonResponse({"status":"err", "id":-1},status=403)
        newuser = User.objects.create(
            login=login,
            password=password
        )
        resp = JsonResponse({"status": "ok", "login":login,"password":password,"id":newuser.id})
        resp.set_cookie('token', login, max_age=86400)
        return resp
    else:
        return render(request, 'index.html')

def logout(request):
    resp = redirect("/")
    token = request.COOKIES.get("token")
    if not token is None:
        resp.delete_cookie("token")
    return resp
