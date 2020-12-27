import threading
from threading import*
import time

d={} # to store data

#create operation 
def create(key,value,timeout=0):
    if key in d:
        print("error: this key already exists") #error message
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#error message
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

#read operation
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparision of present time with expiry time
                stri= str(key)+":"+str(b[0]) #returns the value in json object.
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#delete operation
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            del d[key]
            print("key is successfully deleted")



#modify operation
            
def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
