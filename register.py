from tkinter import *
import os
def delete1():
  screen1.destroy()
def delete2():
  screen3.destroy() 
def delete3():
  screen4.destroy() 
def delete4():
  screen5.destroy() 
def login_success():
  global screen3
  screen3 = Toplevel(screen)
  screen3.title("Success")
  screen3.geometry("150x100")
  Label(screen3, text = "Login success").pack()
  Button(screen3, text = "OK", command =delete2).pack() 
def password_not_recognised():
  global screen4
  screen4 = Toplevel(screen)
  screen4.title("Invalid Password")
  screen4.geometry("150x100")
  Label(screen4, text = "Password Error").pack()
  Button(screen4, text = "OK", command =delete3).pack()
def user_not_found():
  global screen5
  screen5 = Toplevel(screen)
  screen5.title("Invalid User")
  screen5.geometry("150x100")
  Label(screen5, text = "User Not Found").pack()
  Button(screen5, text = "OK", command =delete4).pack()   
def register_user():
  print("working") 
  username_info = username.get()
  password_info = password.get()
  file=open(username_info, "w")
  file.write(username_info+"\n")
  file.write(password_info)
  file.close()
  username_entry.delete(0, END)
  password_entry.delete(0, END)
  Label(screen1, text = "Registration success", fg = "green" ,font = ("calibri", 11)).pack()
def login_verify():  
  username1 = username_verify.get()
  password1 = password_verify.get()
  username_entry1.delete(0, END)
  password_entry1.delete(0, END)
  list_of_files = os.listdir()
  if username1 in list_of_files:
    file1 = open(username1, "r")
    verify = file1.read().splitlines()
    if password1 in verify:
        login_success()
    else:
        password_not_recognised()
  else:
        user_not_found()
def register():
  global screen1
  screen1 = Toplevel(screen)
  screen1.title("Register")
  screen1.geometry("300x350") 
  global username
  global password
  global username_entry
  global password_entry
  username = StringVar()
  password = StringVar()
  Label(screen1, text = "Registration Page", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(screen1, text = "").pack()
  Label(screen1, text = "Username").pack()
  username_entry = Entry(screen1, textvariable = username)
  username_entry.pack()
  Label(screen1, text = "Password").pack()
  password_entry =  Entry(screen1, textvariable = password)
  password_entry.pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()
  Label(screen1, text = "").pack()
  Button(screen1, text = "Back to Login", width = 10, height = 1, command =delete1 ).pack()
  Label(screen1, text = "").pack()
def main_screen():
  global screen
  screen = Tk()
  screen.geometry("300x350")
  screen.title("Python Project")
  Label(text = "Login Page", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "").pack()
  global username_verify
  global password_verify
  username_verify = StringVar()
  password_verify = StringVar()
 
  global username_entry1
  global password_entry1
   
  Label(text = "Username").pack()
  username_entry1 = Entry(textvariable = username_verify)
  username_entry1.pack()
  Label( text = "").pack()
  Label(text = "Password").pack()
  password_entry1 = Entry(textvariable = password_verify)
  password_entry1.pack()
  Label(text = "").pack()
  Button(text = "Login", width = 10, height = 1, command = login_verify).pack()
  Label(text = "").pack()
  Button(text = "Register Here",height = 1, width = 10, command = register).pack() 
  screen.mainloop()
main_screen()

