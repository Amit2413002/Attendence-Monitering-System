from tkinter import *
window =Tk()  #creating root window from tk() constructor
window.geometry("500x300") #setting the dimensions of window 
window.title("Attendence Monitering System")  # setting the title 
lb1 = Label(window, text = "Attendence Monitering", bg = "white", fg="black", font=20)  #inserting the label 
lb1.place(x=150, y=10) # setting the cordinates of label 

lb2_u = Label(window, text = "Student Name ", bg="white", fg="black", font=15)
lb2_u2 = Entry(window,font=15) # entry is ysed to create the textbox 
lb2_u.place(x=10, y=90)
lb2_u2.place(x=180, y=90)

lb2_id = Label(window, text = "Student ID", bg="white", fg="black", font=15)
lb2_id2 = Entry(window,font=15)
lb2_id.place(x=10, y=150)
lb2_id2.place(x=180, y=150)

bt_Take_Images = Button(window, text="Take Images",font=15,bg="green",fg="black",activeforeground="red",activebackground="red")
bt_Take_Images.place(x=80,y=210) 

bt_Train_Images = Button(window, text="Train Images",font=15,bg="green",fg="black")
bt_Train_Images.place(x=270,y=210)

window.mainloop()
# setting an infinite loop to run the program which ends when the window is closed 
