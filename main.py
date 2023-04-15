from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import json

#Function

def Save():
    website = website_Entry.get()
    Email = Email_Entry.get()
    Password = Password_Entry.get()
    new_data = {
       website : {
            "email" :Email ,
            "password" : Password
        }
    }
    
    # is_ok = messagebox.askokcancel(title='Website',message=f"There are the details entered: \n Email:{Email}"
    #                          f"\n Password:{Password} \n it is ok to save?")
    
    if len(website) == 0 or len(Password) == 0:
        messagebox.showinfo(title="oh nn!!!!!!!!!!!!!!!!",message="you don't enter password and email!!!")
    else:
        with open("data.json","w") as data :
            json.dump(new_data, data,indent=4)
            website_Entry.delete(0,END)
            Password_Entry.delete(0,END)
    

def GeneratePass():
    Password_Entry.delete(0,END)
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 
    't', 'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols= ['{','}','(',')','[',']','+','/','*','/','&','|']

    pasword_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    pasword_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_List = pasword_letters + password_symbols + pasword_numbers
    shuffle(password_List)

    password = "".join(password_List)

    Password_Entry.insert(0,password)


window = Tk()
window.title('Password Generator')
window.config(padx=20,pady=20)
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#label

websiteLabel = Label(text='Website')
websiteLabel.grid(row=1,column=0)
EmailLabel =  Label(text='Email/Username')
EmailLabel.grid(row=2,column=0)
PasswordLabel = Label(text='Password')
PasswordLabel.grid(row=3,column=0)

#Entries

website_Entry = Entry(width=45 )
website_Entry.grid(row=1 ,column=1,columnspan=2)
website_Entry.focus()
Email_Entry = Entry(width=45 )
Email_Entry.grid(row=2 ,column=1,columnspan=2)
Email_Entry.insert(0, "amirhosseine13579@gmail.com")
Password_Entry = Entry(width=26)
Password_Entry.grid(row=3 ,column=1)



#Button
PassBT = Button(text='Generate Password',width=15,command=GeneratePass) 
PassBT.grid(row=3,column=2)
AddBT = Button(text='Add',width=36,command=Save)
AddBT.grid(row=4,column=1,columnspan=2)

window.mainloop()