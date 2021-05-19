from socket import *
from _thread import *
from tkinter import *
from tkinter import messagebox
import threading

def recvThread(C):
	global turn
	while True:
		x = C.recv(2048)
		if(x.decode('UTF-8') == 'a'):
			btn1["text"]="x"
			btn1["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'b'):
			btn2["text"]="x"
			btn2["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'c'):
			btn3["text"]="x"
			btn3["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'd'):
			btn4["text"]="x"
			btn4["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'e'):
			btn5["text"]="x"
			btn5["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'f'):
			btn6["text"]="x"
			btn6["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'g'):
			btn7["text"]="x"
			btn7["fg"]="blue"
			turn=1
			check()

		if(x.decode('UTF-8') == 'h'):
			btn8["text"]="x"
			btn8["fg"]="blue"
			turn=1
			check()

		if(x .decode('UTF-8')== 'i'):
			btn9["text"]="x"
			btn9["fg"]="blue"
			turn=1
			check()
		
def clientThread(C):
	receive = threading.Thread(target=recvThread, args=(C,))
	receive.start()

s = socket(AF_INET, SOCK_STREAM)
host = '127.0.0.1'
port = 7004

s.bind((host, port))
s.listen(5)

#Tic tac toe game..

def send(z):
	C.send(z.encode('UTF-8'))

W1 = Tk()
W1.title('Tic Tac Toe __ Server')
W1.geometry('400x300')
lb1 = Label(W1, text="Client: x ", font=('Helvetica','10'))
lb1.grid(row=1, column=0)
lb1 = Label(W1, text="Server: o ", font=('Helvetica','10'))
lb1.grid(row=2, column=0)

def Reset():
	global flag
	global turn
	btn1["text"]=' '
	btn2["text"]=' '
	btn3["text"]=' '
	btn4["text"]=' '
	btn5["text"]=' '
	btn6["text"]=' '
	btn7["text"]=' '
	btn8["text"]=' '
	btn9["text"]=' '
	flag=1
	turn=1

def win(a):
	if a=='x':
		messagebox.showinfo("Win" , "Congratulation Client")
	else:
		messagebox.showinfo("Win" , "Congratulation For You")
	Reset()

flag =1
def check():
	global flag
	flag = flag+1
	b1=btn1["text"]
	b2=btn2["text"]
	b3=btn3["text"]
	b4=btn4["text"]
	b5=btn5["text"]
	b6=btn6["text"]
	b7=btn7["text"]
	b8=btn8["text"]
	b9=btn9["text"]

	if (b1==b2 and b2==b3 and b1 == "x") or (b1==b2 and b2==b3 and b1 == "o") :
		win(b1)
	if (b4==b5 and b5==b6 and b4 == "x") or (b4==b5 and b5==b6 and b4 == "o") :
		win(b4)
	if (b7==b8 and b8==b9 and b7 == "x") or (b7==b8 and b8==b9 and b7 == "o") :
		win(b7)
	if (b1==b4 and b4==b7 and b1 == "x") or (b1==b4 and b4==b7 and b1 == "o") :
		win(b1)
	if (b2==b5 and b5==b8 and b2 == "x") or (b2==b5 and b5==b8 and b2 == "o") :
		win(b2)
	if (b3==b6 and b6==b9 and b3 == "x") or (b3==b6 and b6==b9 and b3 == "o") :
		win(b3)
	if (b1==b5 and b5==b9 and b1 == "x") or (b1==b5 and b5==b9 and b1 == "o") :
		win(b1)
	if (b3==b5 and b5==b7 and b3 == "x") or (b3==b5 and b5==b7 and b3 == "o") :
		win(b3)
	
	if flag == 10:
		messagebox.showinfo("Display" , "Game Over, No Winner")
		Reset()

turn=1
def click1():
	global turn
	if btn1["text"]== ' ':
		if turn ==1:
			turn =2
			btn1["text"]="o"
			send('a')
			check()
			
def click2():
	global turn
	if btn2["text"]== ' ':
		if turn ==1:
			turn =2
			btn2["text"]="o"
			send('b')
			check()

def click3():
	global turn
	if btn3["text"]== ' ':
		if turn ==1:
			turn =2
			btn3["text"]="o"
			send('c')
			check()

def click4():
	global turn
	if btn4["text"]== ' ':
		if turn ==1:
			turn =2
			btn4["text"]="o"
			send('d')
			check()

def click5():
	global turn
	if btn5["text"]== ' ':
		if turn ==1:
			turn =2
			btn5["text"]="o"
			send('e')
			check()

def click6():
	global turn
	if btn6["text"]== ' ':
		if turn ==1:
			turn =2
			btn6["text"]="o"
			send('f')
			check()

def click7():
	global turn
	if btn7["text"]== ' ':
		if turn ==1:
			turn =2
			btn7["text"]="o"
			send('g')
			check()

def click8():
	global turn
	if btn8["text"]== ' ':
		if turn ==1:
			turn =2
			btn8["text"]="o"
			send('h')
			check()

def click9():
	global turn
	if btn9["text"]== ' ':
		if turn ==1:
			turn =2
			btn9["text"]="o"
			send('i')
			check()


btn1 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click1)
btn1.grid(row=5, column=8)
btn2 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click2)
btn2.grid(row=5, column=9)
btn3 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click3)
btn3.grid(row=5, column=10)
btn4 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click4)
btn4.grid(row=6, column=8)
btn5 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click5)
btn5.grid(row=6, column=9)
btn6 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click6)
btn6.grid(row=6, column=10)
btn7 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click7)
btn7.grid(row=7, column=8)
btn8 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click8)
btn8.grid(row=7, column=9)
btn9 = Button(W1, text=' ',bg="#ccc", fg="red", width=4, height=2, font =('Helvetica','10'), command=click9)
btn9.grid(row=7, column=10)

def End():
	W1.destroy()

btn = Button(W1, text='End Game',bg="#ddd", width=20, height=2,  command=End)
btn.place(relx=0.5, rely=0.8, anchor=CENTER)

while True:
	C, ad = s.accept()
	print("Connection form ", ad[0])
	start_new_thread(clientThread,(C,))

	W1.mainloop()
C.close()