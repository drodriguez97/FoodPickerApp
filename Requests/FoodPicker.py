from YelpApi import names , address 
import random

#create new list by using zip that contains both name and 
new_list = zip(names, address)
user_choice = ""
keyword = "Yes"
n = "No"

locations = []
for name,address in new_list:
    locations.append((name , address))


while True:
    user_choice = input("Would like to drink coffee today? Yes or No? ") 
    
    if user_choice == n:
        print("Okay. No worries, come back later.")
        break
    if user_choice != keyword:
        print("Please enter either Yes or No. Thank you.")
        continue
    else: 
        location = random.choice(locations)
        location = ('. '.join(str(x) for x in location)) #add period after location name
        print(f'You should go to {location}. ')
        break  
    
    
   
    
    

         
