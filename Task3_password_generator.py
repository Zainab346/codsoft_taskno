from tkinter import *
import random

root =Tk()
root.title("<<<<PASSWORD GENERATOR>>>>" )
root.geometry("520x320")

def rand_pass():
    rt_pw .delete(0 , END)
    pass_length = (E1.get())
    
    try:
          pass_length = int(pass_length)

          password=""
          for i in range(pass_length):
               password += chr(random.randint(33,126))

          rt_pw.insert(0 , password)
          success.config(text="Password generated successfully!", fg="green" )

    except ValueError:
         success.config(text="Please enter a valid integer for password length!", fg="red" )

 
#LabelFrame
l1 = LabelFrame(root , text="Specify the desired length of the password?" , fg="red")
l1.pack(pady=20)

#Entry box for designating number of characters
E1 = Entry(l1 , font=("Times New Roman" , 20 , "bold" ,"italic" ) , bg="antiquewhite")
E1.pack(padx=20 , pady=20)

#Entry box for our returned password
rt_pw = Entry(root , text="" , font=("Times New Roman" , 20 , "bold" , "italic") ,bg="lavender" )
rt_pw.pack(pady=20)

#Frame for Button
F1= Frame(root)
F1.pack(pady= 20)

#Button
B1 = Button(F1 , text="Generate Password" ,font=("bold" ,10) , fg="white" ,bg="darkslategray4" ,command=rand_pass)
B1.grid(row=0 , column=0 , padx=10)

# Success message label
success = Label(root, text="", font=("bold", 14 , "italic" ), fg="green")
success.pack(pady=10)
root.mainloop()

