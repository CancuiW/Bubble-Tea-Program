#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 19:16:45 2022
@Python version: 3.7x
@Purpose: create an order program for customers to order and calculate fees.
@author: Can Cui
"""
#import database
import sqlite3
# import sys module which stores the "Module"
import sys
sys.path.append('./Bubble_Tea_Project')
#import my Module file
import Module

#check the step for importing database 
try:
    conn=sqlite3.connect('T.db')
    print("Connectting to the database successfully!")
except Exception as e:
    print("Error during connection: ",str(e))
    
c=conn.cursor()
#create tables and input relative data

#c.execute("""CREATE TABLE TOPPING(
#  add_name text,
#  add_price decimal)
#          """)

#c.execute("INSERT INTO TOPPING VALUES('sesame',0.50)")

#import the data as  a type of dictionary
c.execute("SELECT * FROM BASE")
base=c.fetchall()
tea_baseDict=dict(base)


c.execute("SELECT * FROM TOPPING")
top=c.fetchall()
add_onsDict=dict(top)

                  
conn.commit()   
conn.close()



# store members in a list
memberList=["can","rachel","manroop","mohammad"]

# print all information at the end of this program
Items={}




    
    
def errorMsg(text):
   
    Module.newLine()
    print("\tERROR: " + text)
    Module.newLine()
    


def exitMsg():
   
    Module.newLine()
    print("Thank you for ordering.")
    Module.newLine() 
    

def Instructions():
    Module.Line()
    print("Welcome to the online food ordering system.")
    Module.newLine()
    print("The menu is as follows:")
    #list all products for customer to choose
    Module.Lines(20)
    print("\t\tTeas:")
    print("Items","\t\t","Price($)")
    for key,value in tea_baseDict.items():
        print(key,"\t\t",value)
    Module.newLine()
    Module.Lines(20)
    print("Add toppings to your drinks:")
    print("Items","\t\t","Price($)")
    for k,v in add_onsDict.items():
        print(k,"\t\t",v)
    Module.newLine()
    print("Please follow the steps below to select a product.")
    print("You can quit at any time by typing 'q' to QUIT (without quotes)")
    Module.Line()
    Module.newLine()

# discount for members  
def membership():
    while True:
        try:
            ask_forMember=input("Are you a member of our store?(Yes or No)")
            # Remove whitespace from the input we received
            # and lowercase the input
            ask_forMember=ask_forMember.strip().lower()
            if ask_forMember=="q":
                exitMsg() 
                return False
                
            
            elif ask_forMember=="yes":
                ask_Name=input("Please enter your Firstname: ")
                ask_Name=ask_Name.strip().lower()
                if ask_Name in memberList:
                    #discount for members
                    loyalty_discount=0.9
                    return loyalty_discount
                
                elif ask_Name=="q":
                    exitMsg() 
                    return False
                else:
                    Module.newLine()
                    print("\t\tSorry, we can not find your information.")
                    print("Please check your name carefully.")
                    Module.newLine()
                
            elif ask_forMember=="no":
                loyalty_discount=1
                return loyalty_discount
            else:
                raise ValueError    
                    
        except ValueError:
            errorMsg("0: You must supply a valid massage."
                     +"You can quit by typing 'q'. ")
    
        
def base_bubbleTea():
 
    while True:
       
        try:
            
            userBase = input("Please enter the type of base（only one choice): ")       
            userBase = userBase.strip().lower()
        
            if userBase in tea_baseDict:
                baseValue=tea_baseDict[userBase]
                Items[userBase]=baseValue
                return baseValue
                
            elif userBase=="q":
                exitMsg() 
                return False
                   
            else:
                raise ValueError
    
        except ValueError:
            errorMsg("1: You must supply a valid option.")

def askUserForTopping():
      
    while True:
        try:
            userOption= input("Please enter the name of topping \n" 
                             + "(separated by a comma)"
                             +"(if no topping, enter 'no'): ")
            
            # Remove whitespace from the input we received
            userOption = userOption.strip().lower()
            # split() is used here
            # It allows me to break apart input string by a comma
            userListOption = userOption.split(',')
           
            if userOption == "q":
                exitMsg() 
                return False
           
           
            elif userOption =="no":
                #when addValue=0,result(default) =False
                addValue="NONE"
                return addValue
                
            
            else:
                
                #nested For Loop 
                for x in userListOption:
                   
                    for y in add_onsDict:
                        if x==y:
                            addValue=add_onsDict[y]
                            Items[y]=addValue
                                       
                return addValue
                
           
                
        except:
            errorMsg("3: No corresponding item was found.")            
                 
def output():
    Module.newLine()
    Module.Line()
  
    print("\t\t\t XX BUBBLE TEA")
    Module.Lines()
    print("ITEM \t\t\t\t\t PRICE($)")
    Module.Lines()
    for p,q in Items.items():
        print(p,"\t\t\t\t\t",q)
    print("tax","\t\t\t\t\t\t","6%")
    # keep two significant digits
    print("Total_Price:","\t\t\t",str("%.2f" % total))
    Module.Lines()
    print("There is a 10% discount for members.")
    Module.Line()
    
    
    
if __name__=="__main__":
    while True:
        Instructions()
        discount=membership()
        total=0
        if discount==False:
            #out of while loop
            break
        else:
            base=base_bubbleTea()
            if base==False:
                break
            else:
               
                tops=askUserForTopping()
                if tops==False:
                    break
                elif tops=="NONE":
                    #tax=6%
                    total = float(discount) * base*1.06
                    output()
                    break
                else:
                    List=list(Items.values())  
                    total_item=float(sum(List))
                    total = float(discount) *total_item*1.06
                    output()
                    break




                   

            
        
    
  
    
    
    
       
        
