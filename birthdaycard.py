print("Recipent's name?")
name= input ("Recipent's name?")

print ("sender's name")
senders_name = input("sender's name")

print("Personalized message")
message =input("Personalized message")

print("recipent's birthday age")
age = int(input ("recipent's birthday age"))



print (f"""{name}, 

Leeeets celebrate your {age} years of awesomeness !!!!!!!
       Wishing you a day filled with joy and laughter as your turn {age} !

       {message}
       
       With love and best wishes,
       {senders_name}""")