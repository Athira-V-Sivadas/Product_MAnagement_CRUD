import pymysql
import datetime

class Dbconnect:

    def get_connected(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="Luminar@1234",
                database="ecommercedb"
            )

            return self.connection

        except Exception as e:
            print(e)
            return None

class ProductManager(Dbconnect):

    def get(self):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM product"

            self.cursor.execute(query)

            record = self.cursor.fetchall()

            for data in record:
                print(data)

        except Exception as e:
            print(e)

            

    def post(self, **kwargs):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = """INSERT INTO product
            (product_name, category_id, price, stock, description)
             VALUES (%s, %s, %s, %s, %s)"""

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)

            self.connect.commit()

            print("Product Added Successfully")

        except Exception as e:
            print(e)

    def get_object(self, id):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM product WHERE id=%s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)
            return None

    def retrieve(self, id):
        try:
            record = self.get_object(id)

            if record != None:
                  print(record)

            else:
                print("Product Not Found")

        except Exception as e:
            print(e)



    def put(self, id=None, **kwargs):
         try:
        record = self.get_object(id)

        if record != None:

            placeholder = ""

            for k in kwargs.keys():
                placeholder += k + "=%s, "

            placeholder = placeholder.rstrip(", ")

            query = f"UPDATE product SET {placeholder} WHERE id=%s"

            values = [v for v in kwargs.values()]

            values.append(id)

            self.cursor.execute(query, values)

            self.connect.commit()

            print("Product Updated Successfully")

        else:
            print("Product Not Found")

    except Exception as e:
        print(e)


    def delete(self, id=None):
    try:
        record = self.get_object(id)

        if record != None:

            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()

            query = "DELETE FROM product WHERE id=%s"
            values = (id,)

            self.cursor.execute(query, values)

            self.connect.commit()

            print("Product Deleted Successfully")

        else:
            print("Product Not Found")

    except Exception as e:
        print(e)






connection_instance = Dbconnect()

print(connection_instance.get_connected())


product_instance = ProductManager()

product_instance.get()

product_instance = ProductManager()

product_instance.post(
    product_name="HP Laptop",
    category_id=1,
    price=55000,
    stock=10,
    description="HP Pavilion Laptop"
)

product_instance.retrieve(id=1)

product_instance.put(id=1, price=45000, stock=15)

product_instance.delete(id=1)


