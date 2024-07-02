# -*- coding: utf-8 -*-

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "Error! Division by zero."
    return x/y

while True:
    print("Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice=input("Enter your choice (1/2/3/4/5): ")
    
    if choice=='5':
        print("Exiting the calculator.")
        break
    if choice not in ('1','2','3','4'):
        print("Invalid choice. Please enter a valid option. ")
        continue
    
    number1=float(input("Enter your first number: "))
    number2=float(input("Enter your second number: "))
    
    if choice=='1':
        print("Result: "+str(add(number1, number2)))
        break
    elif choice=='2':
        print("Result: "+str(subtract(number1, number2)))
        break
    elif choice=='3':
        print("Result: "+str(multiply(number1, number2)))
        break
    elif choice=='4':
        print("Result: "+str(divide(number1,number2)))
        break
        
        
        
        
        

