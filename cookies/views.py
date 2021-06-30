
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
# Create your views here.

def index(request):
    context = "Woow it works"
    return  render(request,'cookies\index.html',{'context':context})

def setcookie(request):
    html = HttpResponse("<h1>DataFlair Django tutorial</h1>")
    if request.COOKIES.get("visits"):
        html.set_cookie('dataflair','Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits',value+1)
    else:
        value = 1
        text = "Welcome first time dude"
        html.set_cookie('visits',value)
        html.set_cookie('dataflair',text)
    return html


def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}</h1>you have requested this page {1} times</center>".format(text,value))
        html.set_cookie('visits',int(value) +1)
        return html
    else:
        #return redirect("/setcookie/")
        return redirect('/cookies/setcookie')

def delete_co(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
       response.delete_cookie("visits")
       response.delete_cookie("dataflair")
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")
def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("<h1>dataflair  cookie created</h1>")
    else:
        response = HttpResponse("<h1>Your browser does not accept cookies</h1>")

    return  response

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return  redirect("/cookies/create/")

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except  KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")
