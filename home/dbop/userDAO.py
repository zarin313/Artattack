from django.db import connection
from . import user
from . import dbfactory
from . import works
#for password hash
from django.contrib.auth.hashers import *

class UserDAO:

    def getCursor(self):

        return dbfactory.DBFactory.getInstance().getDBCursor()

    def addwork(self,im,nm):
         c=self.getCursor()
         try:
             c.execute("INSERT INTO userwork VALUES (Null,%s,%s)",[im,nm])
         except:
             return False
         finally:
             c.close()
    def seework(self):
        dbcursor=self.getCursor()
        dbcursor.execute("SELECT * from userwork")
        s=dbcursor.fetchall()
        li=[]
        for row in s:
            w=works.Works(row[0],row[1],row[2])
            li.append(w)

        return li



    def sameuname(self,u):
        c=self.getCursor()
        # print("daggadg")
        # print(u.getPas())
        # print(u.getConfpas())
        c.execute("SELECT uname FROM user")
        result=c.fetchall()
        print(result)
        same=0
        for i in result:
            print(i)
            print(u.getUname())
            if (u.getUname()==(i)):
                print(i)
                #print(u.getUname())
                return True
        return False

    def insertUser(self, u):

        c=self.getCursor()
        # print("daggadg")
        # print(u.getPas())
        # print(u.getConfpas())


        try:
            if u.getPas()==u.getConfpas():
                c.execute("INSERT INTO user VALUES(%s,%s,%s,%s,%s)",[u.getName(),u.getUname(),u.getEmail(),u.getPhone(),make_password(u.getPas())]) #security SQL injection block
                return True

        except:
            return False
        finally:
            c.close()
    def insertSugg(self,s):
         c=self.getCursor()
         try:
             c.execute("INSERT INTO suggestion VALUES(Null,%s)",[s])
         except:
             return False
         finally:
             c.close()
    def authenticate_user(self, u):

        c=self.getCursor()
        try:

            c.execute("SELECT password FROM user WHERE uname=%s",[u.getUname()])
             #security SQL injection block
            ret=c.fetchall() #list of tuple
            if len(ret)==1:
                print("yes")
                row=ret[0]

                auth=check_password(u.getPas(), row[0])

                if auth is True:

                    return True
                else:

                    return False
            else:
                return False
        except:
            return False
        finally:
            c.close()
