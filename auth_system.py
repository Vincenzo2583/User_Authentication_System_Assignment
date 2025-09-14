users = {
    304: {
        'email': "manonfire@gmail.com",
        'name' :"Abdulhamid Saka " ,
        'password': "abdul4life",
        'is_admin': False
    },
    513: {
        'email': "maryjane4@yahoo.com",
        'name' :"Mary Babajide" ,
        'password' : "8meorloveme",
        'is_admin': False
    },
    202: {
        'email': "emeka_josh@yahoo.com",
        'name' :"Joshua Emeka" ,
        'password': "boys2men",
        'is_admin': False
    },
    230: {
        'email': "agent_47@gmail.com",
        'name' :"Damilare Ayodele" ,
        'password': "dammy4real",
        'is_admin': False
    }
}

import random
user_id = random.randint(100, 999)
  
def register(user_id):
    name = input('Enter your name: ').lower()
    email = input('Enter email address: ')
    password = input('Enter your password: ')

    for user in users.items():
        if user["email"] == email:
            print("Error: User email already taken!")
            return
        
#To Register A New User
    users.update({
      random.randint(100, 999):{
            "name": name,
            "email": email,
            "password": password
      }
})
    print( f"User Registered Successfully!", {user_id})            

def login(): 
    email = input('Enter email address: ')
    password = input('Enter your password: ')

    for user_id, user in users.items():
        if user['email'] == email and user['password'] == password:
              print(f"Login Successful", {user_id})
              return
        else:
            print("Invalid email or password")

def remove_user(user_id):
    #To check if user exists
    if user_id in users:
        deleted_user = users.pop(user_id)
        return{"status": "success", "message": f"User {deleted_user['name']} removed successfully"}

 #Bonus Challenge   
def list_users(users):
    user_list = []
    for user_id, user in users.items():
        user_list.append({
            "id": user_id,
            "name": user['name'],
            "email": user['email']
        })
    return user_list

print(list_users(users))
  
def update_password(users, user_id: int, old_password: str, new_password: str ):
    if user_id not in users:
        return{"status": "error", "message": "User ID not found!"}
    
    user = users[user_id]

    if user["password"] != old_password:
        return{"status": "error", "message": "Password is incorrect!"}
    
    if old_password == new_password:
        return{"status": "error", "message": "New password cannot be the same as old password!"}
    
    users[user_id]['password'] = new_password
    return{"status": "error", "message": "Successfully updated password!"}