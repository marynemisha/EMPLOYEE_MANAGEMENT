import mysql.connector
import datetime
class DbConnect:
    def get_connect(self):
        try:
            self.connection=mysql.connector.connect(
                host="localhost",
                user="root",
                password="Nemisha@10",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None
class EmployeeManager(DbConnect):
    def get_object(self,id=None):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            return records
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect= super().get_connect()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(records)
        except Exception as e:
            print(e)
    def post(self,id=None,**kwargs):
        try:
            self.connect = super().get_connect()
            self.cursor = self.connect.cursor()
            query = "insert into employee(name,place,mobile,email,department,salary,joining_date)values(%s,%s,%s,%s,%s,%s,%s)"
            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("Employee added successfully...!")
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            records = self.get_object(id=id)
            if records == None:
                print("Employee not found...!")
            else:
                print(records)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            records = self.get_object(id=id)
            if records==None:
                print("Employee not found...!")
            else:
                query="delete from employee where id=%s"
                values=(id,)
                self.cursor.execute(query,values)
                self.connect.commit()
                print("Employee deleted successfully...!")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            records = self.get_object(id=id)
            if records == None:
                print("Employee not found...!")
            else:
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                placeholder=placeholder.rstrip(",")
                query = f"update employee set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Employee updated successfully...!")
        except Exception as e:
            print(e)

emp=DbConnect()
print(emp.get_connect())

emp_instance=EmployeeManager()
# emp_instance.get()
# emp_instance.post(name="Anjana",place="EKM",mobile="9876543210",email="anjana23@gmail.com",department="IT",salary="30000",joining_date=datetime.datetime.today())
# emp_instance.post(name="Mariya",place="TVM",mobile="9876043210",email="mariya@gmail.com",department="HR",salary="50000",joining_date=datetime.datetime.today())
# emp_instance.get()
# emp_instance.retrieve(id=1)
# emp_instance.get_object(id=1)
emp_instance.retrieve(id=1)
emp_instance.delete(id=3)
emp_instance.put(id=1,name="Anju",place="EKM",mobile="9876543210",email="anju23@gmail.com",department="IT",salary="30000",joining_date=datetime.datetime.today())
emp_instance.get()