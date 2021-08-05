from django.db import connection
from . import product
from . import dbfactory


class ProductDAO:

    def getCursor(self):
        return dbfactory.DBFactory.getInstance().getDBCursor()



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
    
