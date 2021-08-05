from django.shortcuts import *
from django.http import HttpResponse
from . import myform
from django.core.files.storage import FileSystemStorage
from .dbop import product
from .dbop import productDAO
# Create your views here.
def adminview(request):
          django_form=myform.addForm()
          dao=productDAO.ProductDAO()
          prodlist=dao.showall() #list of product objects
          print(prodlist)
          s=dao.sugg()
          print(s)
          return render(request,'adminpage.html', {'data':prodlist,'f':django_form,'su':s})

def adddata(request):

   if request.method=="GET":
        django_form=myform.addForm()
        return render(request, 'adminpage.html', {'f':django_form})
   elif request.method=="POST":
       django_form=myform.addForm(request.POST,request.FILES)
       if django_form.is_valid():
           name=django_form.cleaned_data['addname']
           brand=django_form.cleaned_data['addbrand']
           desc=django_form.cleaned_data['adddesc']
           price=django_form.cleaned_data['addprice']
           available=django_form.cleaned_data['addavail']
           catagory=django_form.cleaned_data['addcat']



           image=django_form.cleaned_data['addpic']
           fs=FileSystemStorage()
           newname=fs.save(image.name,image)
           imgurl=fs.url(newname)

           p=product.Product(-1,name,brand,desc,price,available,catagory,imgurl)
           dao=productDAO.ProductDAO()

           try:

              dao.addproduct(p)
              django_form=myform.addForm()
              print("hello")
              prodlist=dao.showall()
              return render(request,'adminpage.html',{'data':prodlist,'f':django_form,'success':True})
           except:
               django_form=myform.addForm()
               prodlist=dao.showall()
               return render(request,'adminpage.html',{'data':prodlist,'f':django_form,'success':False})
       else:
           return render(request,'adminpage.html',{'f':django_form})

   else:
       django_form=myform.addForm()
       return render(request,'adminpage.html',{'f':django_form})
def delete(request):
    django_form=myform.addForm()
    if request.method=='POST':
        pid=request.POST['pid']

        print(pid)
        dao=productDAO.ProductDAO()
        try:
            p=dao.delete(pid)
            print("sdfsdfvsd")
            prodlist=dao.showall() #list of product objects

            return render(request, 'adminpage.html', {'data':prodlist,'successd':True,'f':django_form})
        except:
            prodlist=dao.showall() #list of product objects
            return render(request,'adminpage.html',{'data':prodlist,'successd':False,'f':django_form})



def update(request, pid):
    if request.method=='GET':
        dao=productDAO.ProductDAO()
        p=dao.findprod(pid)

        print(p.getName())
        django_form=myform.UpdateForm(initial={'pid':p.getID(), 'upname':p.getName(),'upbrand':p.getBrand(),'updesc':p.getDescr(),'upprice':p.getPrice(),'upavail':p.getAvailable(),'upcat':p.getCat() })
        return render(request, 'update.html',{'f':django_form})

    elif request.method=='POST':
        django_form=myform.UpdateForm(request.POST)
        if django_form.is_valid():
             id=django_form.cleaned_data['pid']
             name=django_form.cleaned_data['upname']
             brand=django_form.cleaned_data['upbrand']
             desc=django_form.cleaned_data['updesc']
             price=django_form.cleaned_data['upprice']
             available=django_form.cleaned_data['upavail']
             catagory=django_form.cleaned_data['upcat']

             # image=django_form.cleaned_data['uppic']
             # fs=FileSystemStorage()
             # newname=fs.save(image.name,image)
             # imgurl=fs.url(newname)
             #
             #
             #
             #
             #
             #

             print(catagory)
             print(name)
             print(brand)
             print(desc)
             print(price)
             print(available)

             p1=product.Product(id,name,brand,desc,price,available,catagory,'')
             print(p1.getName())
             dao=productDAO.ProductDAO()

             try:
                print("oro")
                dao.update(p1)
                return render(request,'update.html',{'f':django_form,'successu':True})
             except:
                return render(request,'update.html',{'f':django_form,'successu':False})
        else:
            return render(request, 'update.html',{'f':django_form})
