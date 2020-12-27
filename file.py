import acsscode as x
from threading import*

x.create("rollno",25)

x.create("marks",70,3600) 

x.read("rollno")
#it returns the value of the respective key in Jasonobject format 'key_name:value'

x.read("marks")
#it returns the value of the respective key in Jasonobject format 

x.create("rollno",50)
x.modify("rollno",55)

x.delete("rollno")

t1=Thread(target=(x.create or x.read or x.delete),args=('rollno',50,0))
t1.start()

t2=Thread(target=(x.create or x.read or x.delete),args=('marks',30,0)) 
t2.start()

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB

