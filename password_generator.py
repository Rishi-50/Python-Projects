import random
import string

ch = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_pass():
    password_length = int(input("Enter the length of your password:"))
    random.shuffle(ch)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(ch))
        
    random.shuffle(password)
    
    password = ''.join(password)
    
    print(password)
    
generate_pass()
    


