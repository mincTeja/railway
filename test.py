#importing libraries
from random import randint
import pickle
import time
import os

#class passenger
class passenger:
    def __init__(self,id,name):
        
        self.id=id
        self.name=name
        self.rid=randint(1111,9999)
    def show(self):
        print("id : "+str(self.id)+" name : "+self.name+" reserevation number : "+str(self.rid))



y=1
while y!=0:
    
    print("menu".center(60,"*"))
    print("1. reservation".center(60))
    print("2. chart list".center(60))
    print("3. cancellation".center(60))
    choice=int(input("enter your choice : "))





    if choice == 1:
    
        x=1
        while x!=0:
            i=int(input("enter you authentication id :"))
            n=input("enter your name :")
            p=passenger(i,n)
    
            with open("reserved.pickle","ab") as f:

                pickle.dump(p,f)
                print("successfully entered in the chart..!!")
            x=int(input("do you want to reserve more :(1/0):"))

        print("\n\n")

    if choice == 2 :
    

        with open("reserved.pickle","rb") as f:
            try:
        
                while f:
            


                    q=pickle.load(f)
                    q.show()
            except EOFError :
                print("end".center(40,'-'))

        print("\n")
    
    
    if choice == 3:
        cid=int(input("enter your reservation id : "))
        with open("reserved.pickle","rb") as fr:
            try:
                while fr:
                    z=pickle.load(fr)
                    if z.rid!=cid:
                        with open("temp.pickle","ab") as fw:
                            pickle.dump(z,fw)
                
            except EOFError:
                print("chart updated..!!")
        with open("temp.pickle","rb") as f:
            try:
                while f:
                    o=pickle.load(f)
                    o.show()
            except EOFError:
                print("end".center(50,"-"))
            
            os.remove("reserved.pickle")
            os.rename("temp.pickle","reserved.pickle")


   # else :
    #    print("invalid choice..!!")

    y=int(input("do you want to continue (1/0): "))
