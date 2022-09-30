from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import User

import json
import os

from hashlib import sha256

def index(request):
    return render(request, 'index.html')  

def login(request):
    if request.method == "POST":  # All POSTs
        try:  # Valid JSON
            req_json = json.loads(request.body)
        except:
            return JsonResponse({"status":"err"},status=400)
        login = req_json["login"]
        password = req_json["password"]
        # Hashing is done server-side, otherwise it has no difference than plaintext.
        user = User.objects.filter(login=login)
        if user:
            hash = user[0].password
            salt = hash.split(":")[1]
            comp_hash = sha256(password.encode() + salt.encode()).hexdigest() + ':' + salt
            if hash == comp_hash:
                resp = JsonResponse({"status": "ok", "login":login,"hash":hash,"id":user[0].id})
                # Maybe, some random hex ID from DB?
                resp.set_cookie('token', hash, max_age=86400)
                return resp
        return JsonResponse({"status":"err", "id":-1},status=401)
        
    else:
        return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        try:
            req_json = json.loads(request.body)
        except:
            return JsonResponse({"status":"err"},status=400)
        login = req_json["login"]
        password = req_json["password"]
        salt = os.urandom(16).hex()
        hash = sha256(password.encode() + salt.encode()).hexdigest() + ':' + salt
        user = User.objects.filter(login=login)
        if user:
            return JsonResponse({"status":"err", "id":-1},status=403)
        newuser = User.objects.create(
            login=login,
            password=hash
        )
        resp = JsonResponse({"status": "ok", "login":login,"hash":hash,"id":newuser.id})
        resp.set_cookie('token', hash, max_age=86400)
        return resp
    else:
        return render(request, 'index.html')

def logout(request):
    resp = redirect("/")
    token = request.COOKIES.get("token")
    if not token is None:
        resp.delete_cookie("token")
    return resp
