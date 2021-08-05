from django.db import connection
from . import product
from . import dbfactory


class ProductDAO:

    def getCursor(self):
        return dbfactory.DBFactory.getInstance().getDBCursor()


    def addproduct(self,p):
        try:
            c=self.getCursor()

            c.execute("INSERT INTO product VALUES(Null, %s, %s, %s, %s, %s, %s, %s)", [p.getName(),p.getBrand(),p.getDescr(),p.getPrice(), p.getAvailable(), p.getCat(), p.getImage()])

            print("uploaded")

        except:
            print("error in db")
            raise Error('Database upload query error')
    def showall(self):
        dbcursor=self.getCursor()
        try:
            dbcursor.execute("SELECT * FROM product")
            result=dbcursor.fetchall()
            productlist=[]
            for row in result:
                print(row[7])
                prod=product.Product(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
                productlist.append(prod)
            return productlist
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()
    def delete(self, pid):
        dbcursor=self.getCursor()
        try:
            dbcursor.execute("DELETE FROM product WHERE id=%s", [pid])
        except:
            raise Exception('data deletion error')
        finally:
            dbcursor.close()


    def findprod(self, id):
        dbcursor=self.getCursor()

        print(id)
        try:
            dbcursor.execute("SELECT * FROM product WHERE id=%s",[id])
            item=dbcursor.fetchall()
            print(item[0][0])
            prodobj=product.Product(item[0][0],item[0][1],item[0][2],item[0][3],item[0][4],item[0][5],item[0][6],item[0][7])
            return prodobj
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()



    def update(self, p):

        try:
            dbcursor=self.getCursor()
            print(p.getName())
            print(p.getBrand())
            print(p.getPrice())
            print(p.getAvailable())
            print(p.getCat())
            print(p.getDescr())


            dbcursor.execute("UPDATE product SET Name=%s, Brand=%s, Description=%s, Price=%s, Available=%s, Catagory=%s  WHERE id=%s",[p.getName(),p.getBrand(),p.getDescr(),p.getPrice(),p.getAvailable(),p.getCat(),p.getID()])

            print("iririirriidvdskfjvsdj")
        except:
            raise Exception('data insertion error')
        finally:
            dbcursor.close()
    def sugg(self):
        dbcursor=self.getCursor()
        dbcursor.execute("SELECT * from suggestion")
        s=dbcursor.fetchall()
        li=[]
        for i in range(0,len(s)):
            li.append(s[i][1])
        return li
