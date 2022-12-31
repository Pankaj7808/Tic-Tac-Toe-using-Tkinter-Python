from tkinter import *
import random

class ticTacToe:
    def __init__(self):
        self.root=Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("441x487")
        self.root.resizable(0,0)

        #Mainmenu interface
        Label(self.root,text="Tic Tac Toe",font="Algerian 30",fg="#551A8B").pack(pady=25)
        self.btn1 = Button(self.root,text="1. You v/s Other Player",bg="#00CED1",relief="sunken",command=lambda : self.vars())
        self.btn1.pack(pady=15) 
        self.btn2=Button(self.root,text='2. You v/s Computer     ',bg="#00CED1",relief="sunken",bd=2,command=self.level)
        self.btn2.pack(pady=15)
        self.btn3=Button(self.root,text="Exit",bg="red",fg="white",padx=15,pady=10,font="Times 15",relief=RAISED,command=exit).place(x=180,y=370)
        #
        self.level="No"
        self.xscore=0
        self.oscore=0
    
    #computer v/s human levels
    def level(self):
        btn1 = Button(self.root,text=" Easy ",bg="#00CED1",relief="sunken",width=15,command=self.easy)
        btn2=Button(self.root,text=' Hard ',bg="#00CED1",relief="sunken",bd=2,width=15,command=self.hard)
        btn1.pack(pady=5)
        btn2.pack(pady=5)
        self.btn2.config(state=DISABLED)
    
    #set level to Easy
    def easy(self):
        self.level="Easy"
        self.vars()
    
    def hard(self):
        self.level="Hard"
        self.vars()
        
    #initializing global variables
    def vars(self):
        #to clear screen
        for widgets in self.root.winfo_children():
            widgets.destroy()
        #to count number of button invoked 
        self.i=0
        #TO determine win or loose
        self.l=[[None for i in range(3)] for i in range(3)]
        #to keep reference of buttons
        self.btns=[]
        #to invoke random button
        self.keys=[(0, 0),(0, 1),(0, 2), (1, 0), (1, 1), (1, 2),(2, 0), (2, 1),  (2, 2)]
        self.good=[(0,0),(2,2),(0,2),(2,0)]
        self.god=[(1,0),(0,1),(2,1),(1,2)]

        self.interface()   
    
    #Invoke when player1 click
    def player1(self,r,c):
    #so that computer will not invoke the repeated button
        self.keys.remove((r,c))
        if (r,c) in self.good:
            self.good.remove((r,c))
        if (r,c) in self.god:
            self.god.remove((r,c))
    # if it is player1 turns
        if self.i%2==0:
            l=Label(self.root,text="X",font=("Calibiri",100, "bold"),bg="#00FF00",fg="#FFFF00",padx=20)
            l.grid(row=r,column=c)
            self.btns[r][c].config(state=DISABLED)
            self.l[r][c]=1
            self.column_l=[[self.l[j][i] for j in range(3)] for i in range(3)]
            self.diagonal_l=[([self.l[i][i] for i in range(3)])]
            self.diagonal_l.append([self.l[i][3-i-1] for i in range(3)])
            self.diagonal_l.append([None,None,None])
            self.winner()
            self.i+=1

            #If Computer v/s human easy level--------#if result=win or draw widgets will destroy then how AI will ivoke any random button
            if self.level=="Easy" and  result=="No":
                num=random.choice(self.keys)
                ro,col=num
                self.btns[ro][col].invoke()

            #IF compter v/s human hard level
            elif self.level=="Hard" and result=="No":
                if self.winning()!=None:
                    ro,col=self.winning()
                    self.btns[ro][col].invoke()
                elif self.loosing()!=None:
                    ro,col=self.loosing()
                    self.btns[ro][col].invoke()
                elif self.l[1][1]==None:
                    self.btns[1][1].invoke()
                elif (self.l[0][0]==1 and self.l[2][2]==1) or (self.l[0][2]==1 and self.l[2][0]==1):
                    ro,col=random.choice(self.god)
                    self.btns[ro][col].invoke()
                elif self.l[0][0]==None or self.l[2][0]==None or self.l[0][2]==None or self.l[2][2]==None:
                    ro,col=random.choice(self.good)
                    self.btns[ro][col].invoke()   
                else:
                    ro,col=random.choice(self.keys)
                    self.btns[ro][col].invoke()  
        else:
            self.player2(r,c)

    
    #if it is player2 turns
    def player2(self,r,c):
        l=Label(self.root,text="O",font=("Calibiri",100, "bold"),bg="#00FF00",fg="#68228B")
        l.grid(row=r,column=c)
        self.btns[r][c].config(state=DISABLED)
        self.l[r][c]=0
        self.column_l=[[self.l[j][i] for j in range(3)] for i in range(3)]
        self.diagonal_l=[([self.l[i][i] for i in range(3)])]
        self.diagonal_l.append([self.l[i][3-i-1] for i in range(3)])
        self.winner()
        self.i+=1 


    def winning(self):
        for i in range(3):
            if self.l[i].count(0)==2 and None in self.l[i]:
                return (i,self.l[i].index(None))
            elif self.column_l[i].count(0)==2 and None in self.column_l[i]:
                return (self.column_l[i].index(None),i)
        if  self.diagonal_l[0].count(0)==2 and None in self.diagonal_l[0]:
                return (self.diagonal_l[0].index(None),self.diagonal_l[0].index(None))
        elif self.diagonal_l[1].count(0)==2 and None in self.diagonal_l[1]:
                i=self.diagonal_l[1].index(None)
                if i==0:
                    return (0,2)
                elif i==1:
                    return (1,1)
                elif i==2:
                    return (2,0)

    def loosing(self):
        for i in range(3):
            if self.l[i].count(1)==2 and None in self.l[i]:
                return (i,self.l[i].index(None))
            elif self.column_l[i].count(1)==2 and None in self.column_l[i]:
                return (self.column_l[i].index(None),i)
        if  self.diagonal_l[0].count(1)==2 and None in self.diagonal_l[0]:
                return (self.diagonal_l[0].index(None),self.diagonal_l[0].index(None))
        elif self.diagonal_l[1].count(0)==2 and None in self.diagonal_l[1]:
                i=self.diagonal_l[1].index(None)
                if i==0:
                    return (0,2)
                elif i==1:
                    return (1,1)
                elif i==2:
                    return (2,0)
          
    #To display startinterface and append button to list
    def interface(self):
        for i in range(3):
            row_btn=[]
            for j in range(3):
                btn = Button(self.root,padx=68,pady=68,bg="#00FF00",command=lambda r=i,c=j:self.player1(r,c),bd=3)
                row_btn.append(btn)
                btn.grid(row=i,column=j)
            self.btns.append(row_btn)
        
    #To detemine winner looser and draw
    def winner(self):
        global result
        result="No"
        if self.i==8:
            result="draw"
        if all(self.l[0]) or all(self.l[1]) or all(self.l[2]):
            result="win"
            self.xscore+=1
        elif (self.l[0].count(0)==3) or(self.l[1].count(0)==3) or (self.l[2].count(0)==3):
            result="loose"
            self.oscore+=1
        elif all(self.column_l[0]) or all(self.column_l[1]) or all(self.column_l[2]):
            result="win"
            self.xscore+=1
        elif (self.column_l[0].count(0)==3) or(self.column_l[1].count(0)==3) or (self.column_l[2].count(0)==3):
            result="loose"
            self.oscore+=1
        elif all(self.diagonal_l[0]) or all(self.diagonal_l[1]):
            result="win"
            self.xscore+=1
        elif (self.diagonal_l[0].count(0)==3) or(self.diagonal_l[1].count(0)==3):
            result="loose"
            self.oscore+=1
        
        self.win()

#Winner Looser or Draw interface    
    def win(self):
        if result=="win" or result=="loose" or result=="draw":
            for widgets in self.root.winfo_children():
                widgets.destroy()
            result_label=Label(self.root,text="X Win!",font="Times 30",fg="green")
            result_label.pack(pady=40)
            Label(self.root,text="X score : "+str(self.xscore), font = "Calibiri 23",fg="#33A1C9").place(x=25,y=130)
            Label(self.root,text="O score : "+str(self.oscore), font = "Calibiri 23",fg="#33A1C9").place(x=260,y=130)
            Button(self.root,text="Play again",bg="blue",fg="white",padx=15,pady=10,font="Times 15",relief=RAISED,command=self.vars).pack(pady=100)
            Button(self.root,text="Exit",bg="red",fg="white",padx=15,pady=10,font="Times 15",relief=RAISED,command=exit).pack(pady=15)
            if result=="loose" and self.level=="No":
                 result_label.config(text="O Win!")
            elif result=="win" and (self.level!="No"):
                result_label.config(text="You win!")
            elif result=="loose" and (self.level!="No"):
                result_label.config(text="You loose!",fg="red")
            elif result=="draw":
                result_label.config(text="Match draw!",fg="#C76114") 
    
    def mainloop(self):
        self.root.mainloop()

t = ticTacToe()
t.mainloop()