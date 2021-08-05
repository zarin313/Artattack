class Product:
    def __init__(self,id,name,brand,descr,price,available,catagory,image):
        self.id=id
        self.name=name
        self.brand=brand
        self.descr=descr
        self.price=price
        self.available=available
        self.catagory=catagory

        self.image=image
    def getID(self):
        return self.id
    def setID(self,id):
        self.id=id

    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name

    def getBrand(self):
        return self.brand
    def setBrand(self,brand):
        self.brand=brand

    def getDescr(self):
        return self.descr
    def setDescr(self,descr):
        self.descr=descr

    def getAvailable(self):
        return self.available
    def setAvailable(self,available):
        self.available=available



    def getCat(self):
        return self.catagory
    def setCat(self,catagory):
        self.catagory=catagory

    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price

    def getImage(self):
        return self.image
    def setImage(self,image):
        self.image=image
