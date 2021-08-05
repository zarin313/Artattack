from django.shortcuts import *
from django.http import HttpResponse
from . import myforms
from django.core.files.storage import FileSystemStorage
from .dbop import user
from .dbop import userDAO
from .dbop import product
from .dbop import works
from .dbop import productDAO

def homeview(request):
    dao=productDAO.ProductDAO()
    prodlist=dao.showall()
    udao=userDAO.UserDAO()
    w=udao.seework()

    return render(request, 'home.html',{'data':prodlist,'loggedin':False,'work':w})
def order(request):

    return render(request, 'orderpage.html')

def signup(request):
    dao=productDAO.ProductDAO()
    prodlist=dao.showall()
    udao=userDAO.UserDAO()
    w=udao.seework()
    if request.method=="GET":
        django_form=myforms.signupForm()
        return render(request, 'home.html', {'data':prodlist,'f':django_form,'loggedin':False,'work':w})

    elif request.method=="POST":
        django_form=myforms.signupForm(request.POST)
        if django_form.is_valid():
            name=django_form.cleaned_data['name']
            uname=django_form.cleaned_data['uname']
            email=django_form.cleaned_data['email']
            phone=django_form.cleaned_data['phone']
            pas=django_form.cleaned_data['pas']
            confpas=django_form.cleaned_data['confpas']

            userob=user.User(name,uname,email,phone,pas,confpas)
            userdao=userDAO.UserDAO()

            try:
                if (userdao.sameuname(userob)==True):
                    #print("fvsdvfsv")
                    return render(request, 'home.html', {'data':prodlist,'f':django_form,'work':w,'success':False,'successsame':True,'loggedin':False })

                userdao.insertUser(userob)
                django_form=myforms.signupForm()
                return render(request, 'home.html', {'data':prodlist,'f':django_form,'work':w, 'success':True,'loggedin':False})
            except:
                return render(request, 'home.html', {'data':prodlist,'f':django_form,'work':w, 'success':False,'loggedin':False })
        else:
            return render(request, 'home.html', {'data':prodlist,'f':django_form})
def suggestion(request):
    dao=productDAO.ProductDAO()
    prodlist=dao.showall()
    udao=userDAO.UserDAO()
    w=udao.seework()
    if request.method=="GET":

        return render(request, 'home.html',{'work':w})
    if request.method=="POST":
        django_form=myforms.suggForm(request.POST)
        if django_form.is_valid():
            sugg=django_form.cleaned_data['suggestion']

            sdao=userDAO.UserDAO()
            try:
                sdao.insertSugg(sugg)
                django_form=myforms.suggForm()
                return render(request, 'home.html', {'data':prodlist,'f':django_form,'work':w, 'successsug':True,'loggedin':True})
            except:
                return render(request, 'home.html', {'data':prodlist,'f':django_form,'work':w, 'successsug':False,'loggedin':True})
def login(request):
    dao=productDAO.ProductDAO()
    prodlist=dao.showall()
    udao=userDAO.UserDAO()
    w=udao.seework()
    if request.method=="GET":
        django_form=myforms.loginForm()
        return render(request, 'home.html', {'fl':django_form,'work':w})
    if request.method=="POST":

        django_form=myforms.loginForm(request.POST)
        if django_form.is_valid():

            name=django_form.cleaned_data['loginname']
            pas=django_form.cleaned_data['loginpass']

            userob=user.User('',name,'','',pas,'')

            userdao=userDAO.UserDAO()

            try:
                is_valid=userdao.authenticate_user(userob)
                if is_valid is True:
                    request.session['username']=name

                    print(request.session['username'])

                    return render(request, 'home.html', {'data':prodlist,'work':w,'isvalid':True,'loggedin':True} )
                else:
                    return render(request, 'home.html', {'data':prodlist,'fl':django_form,'work':w, 'isvalid':False,'loggedin':False})
            except:
                return render(request, 'home.html', {'data':prodlist,'fl':django_form, 'work':w,'isvalid':False,'loggedin':False})

        else:
            print("oeoeooeoe")
            return render(request, 'home.html', {'data':prodlist,'fl':django_form,'work':w})
def logout(request):
    del request.session['username']
    return redirect('homeview')
    #return render(request, 'home.html',{'loggedin':False})
def upworks(request):
    dao=productDAO.ProductDAO()
    prodlist=dao.showall()
    udao=userDAO.UserDAO()
    wo=udao.seework()
    if request.method=="POST":
        django_form=myforms.userworkForm(request.POST,request.FILES)

        django_form1=myforms.suggForm()
        if django_form.is_valid():
            image=django_form.cleaned_data['addphoto']
            fs=FileSystemStorage()
            newname=fs.save(image.name,image)
            imgurl=fs.url(newname)
            n=request.session['username']
            w=works.Works(-1,imgurl,n)
            #print(w.uname)
            udao=userDAO.UserDAO()
            try:

               udao.addwork(imgurl,n)

               return render(request, 'home.html', {'data':prodlist,'f':django_form,'f1':django_form1,'work':wo, 'successimg':True,'loggedin':True})
               #print("hello")

            except:
                return render(request, 'home.html', {'data':prodlist,'f':django_form,'f1':django_form1,'work':wo, 'successimg':False,'loggedin':True})
