from tkinter import *
import time
logins=['log123','loger']
passwords=['oleg2005','123']
def zahod():
	global auth
	def si():
		global logins
		global passwords
		global auth
		def ok():
			global auth
			conf_log = entry_nick.get()
			conf_pass = entry_pass.get()
			if conf_log in logins:
				entry_nick.delete(0, END)
				entry_pass.delete(0, END)
				lbl_problem=Label(window,text='Такий логін вже існує, спробуйте інший!',font=('Arial', 8))
				lbl_problem.grid(column=0,row=5)
			elif conf_log=='' or None:
				entry_nick.delete(0, END)
				entry_pass.delete(0, END)
				lbl_problem=Label(window,text='Треба ввести щось...',font=('Arial', 8))
				lbl_problem.grid(column=0,row=5)
			else:
				logins.append(entry_nick)
				passwords.append(entry_pass)
				entry_nick.grid_remove()
				entry_pass.grid_remove()
				btn_ok.grid_remove()
				lbl1.grid_remove()
				lbl2.grid_remove()
				auth=True
				return None
		lbl.grid_remove()
		btn_li.grid_remove()
		btn_si.grid_remove()
		entry_nick=Entry(window, width=70, borderwidth=7)
		entry_pass=Entry(window, width=70, borderwidth=7)
		lbl1 = Label(window, text="Придумайте логін:", font=("Roboto Bold", 10))  
		lbl1.grid(column=0, row=0)  
		entry_nick.grid(row=1, column=0, columnspan=1, padx=10, pady=5)
		lbl2 = Label(window, text="Придумайте пароль:", font=("Roboto Bold", 10))  
		lbl2.grid(column=0, row=2)
		entry_pass.grid(row=3, column=0, columnspan=1, padx=10, pady=5)
		btn_ok=Button(window,text='Зареєструватись!',padx=20,pady=10,command=lambda:ok())
		btn_ok.grid(column=0,row=4)
		return None
	lbl=Label(window,text='Вам необхідно авторизуватись або зареєструватись!',font=('Arial',10))
	lbl.grid(column=0,row=0)
	btn_si=Button(window, text='Регістрація.',padx=20,pady=10, command=lambda:si())
	btn_li=Button(window, text='Авторизація',padx=20,pady=10, command=lambda:auth())
	btn_si.grid(column=1, row=0)
	btn_li.grid(column=2, row=0)
auth=False
window=Tk()
window.title('Program')
zahod()
print(auth)
window.mainloop()