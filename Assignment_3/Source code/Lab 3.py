########################################################################
##
## CS 101 Lab
## Program #3
## Name:Austin Souphanh
## Email: ajs2dz@umkc.edu
##
## PROBLEM : 
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
print("Welcome to Flarsheim Guesser!")


while(True):
    print("\nPlease think of a number between and including 1 and 100.")
  
    t_remainder=0
    f_remainder=0
    s_remainder=0
  
    t_remainder = int(input("\nWhat is the remainder when your number is divided by 3 ?"))
    while t_remainder < 0 or t_remainder >= 3 :
        if t_remainder < 0 :    
            print("The value entered must be 0 or greater")
        elif t_remainder >= 3 :
            print("The value entered must be less than 3")

        t_remainder = int(input("What is the remainder when your number is divided by 3 ?"))

    f_remainder = int(input("\nWhat is the remainder when your number is divided by 5 ?"))
    while(f_remainder < 0 or f_remainder >= 5):
        if f_remainder < 0 :
            print("The value entered must be 0 or greater")
        elif f_remainder >= 5 :
            print("The value entered must be less than 5")
  
        f_remainder = int(input("What is the remainder when your number is divided by 5 ?"))
  

    s_remainder = int(input("\nWhat is the remainder when your number is divided by 7 ?"))
    while(s_remainder < 0 or s_remainder >= 7 ):
        if s_remainder < 0 :
            print("The value entered must be 0 or greater")
        elif s_remainder >= 7 :
            print("The value entered must be less than 7")
        
        s_remainder = int(input("What is the remainder when your number is divided by 7 ?"))
  
  
    for i in range(1,101):
        if(i%3 == t_remainder and i%5 == f_remainder and i%7 == s_remainder):
            print("Your number was",i)
            print("How amazing is that?\n")
    
    while True:
        choice=input("Do you want to play again?Y to continue, N for quit ==>")
        if(choice =='Y' or choice =='y'):
            break
        elif(choice == 'n' or choice == 'n'):
            exit()
            

