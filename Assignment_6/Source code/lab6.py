##
## CS 101 Lab
## Program # 6
## Name:Austin Souphanh
## Email: ajs2dz@umkc.edu
##
## PROBLEM : Describe the problem
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
import string 

def Encrypt(string_text, int_key): 
    result = "" 
    for i in range(len(string_text)): 
        char = string_text[i] 
  
        if (char.isupper()): 
            result += chr((ord(char) + int_key-65) % 26 + 65) 
        elif(char.islower()): 
            result += chr((ord(char) + int_key - 97) % 26 + 97) 
        else:
            result+= char 
    return result  

def Decrypt(string_text, int_key): 
    result = "" 
    for i in range(len(string_text)): 
        char = string_text[i] 
        if (char.isupper()): 
            result += chr((ord(char) - int_key-65) % 26 + 65) 
        elif(char.islower()): 
            result += chr((ord(char) - int_key - 97) % 26 + 97)     
        else:
            result+= char     
    return result  

def Get_input():
    Print_menu() 
    num = input()
    return num
     
def Print_menu():
    print("\nMain Menu")
    print("1). Encode a String")
    print("2). Decode a String")
    print("Q).Quit")
    print("Enter your selection ==>",end='')
    

  
  
def main(): 
  Again = True 
  while Again: 
    Choice = Get_input() 
    if Choice == '1': 
      Plaintext = input("Enter (brief) text to encrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Ciphertext = Encrypt(Plaintext, Key)
      print("Encrypted:", Ciphertext) 
    elif Choice == '2': 
      Ciphertext = input("Enter (brief) text to decrypt: ").upper() 
      Key = int(input("Enter the number to shift letters by: "))
      Plaintext = Decrypt(Ciphertext, Key)
      print("Decrypted:", Plaintext) 
   
    else: 
      print("Have an ordinary day.") 
      Again = False 
      
      
# our entire program: 
main() 
