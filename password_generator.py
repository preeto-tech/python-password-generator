# password generator 
import random # This is a built in module, used to generate random numbers and select random items 
upper_case="WERTYUIOPASDFGHJKLZXCVBNM"
lower_case="qwertyuiopasdfghjklxcvvbnm"
digits="234567890"
symbols="!@#$%^&*()<>/?|"

password_length=int(input("Enter password length: "))

if password_length<6:
    print("\nWeak password!, password should at least 6 character long.\n")
else:
    password=[random.choice(upper_case),
     random.choice(lower_case),
     random.choice(digits),
     random.choice(symbols),
     ]
    
    chars = upper_case + lower_case + digits + symbols
    password+= random.choices(chars,k=password_length-4)

    random.shuffle(password)
    print("\nYour generated password:","".join(password))
