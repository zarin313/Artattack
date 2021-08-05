class Works:
    def __init__(self,id,url,uname):
        self.id=id
        self.url=url
        self.uname=uname


    def getID(self):
        return self.id
    def setID(self,id):
        self.id=id

    def geturl(self):
        return self.url

    def seturl(self,url):
        self.url=url

    def getuname(self):
        return self.uname
    def setuname(self,uname):
        self.uname=uname
