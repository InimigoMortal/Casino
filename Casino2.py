import tkinter as tk
from random import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.msg = tk.Label(self,text="Quantidade de dinheiro apostado:")
        self.msg.pack()
        self.en = tk.Entry(self)
        self.en.pack()
        self.banco = float(500)
        self.valban = tk.Label(self,text="Saldo: " + str(self.banco), bg = "green")
        self.valban.pack()
        self.lb = tk.Label(self,text="O dado vai cair em um valor maior ou menor que 3?")
        self.lb2 = tk.Label(self,text="")
        self.bmaior = tk.Button(self,text = "Maior", command = self.jogaDadoMaior)
        self.bmenor = tk.Button(self,text = "Menor", command = self.jogaDadoMenor)
        
        
        self.lb.pack()
        
        self.bmaior.pack()
        
        self.bmenor.pack()
        
        self.lb2.pack()
        
        
    

    def jogaDadoMaior(self):
        self.valorap = self.en.get()

        

        if float(self.valorap) > self.banco:
           
           if self.banco == 0:
                self.gameOver()
           else:
                self.lb2['text'] = "Aposta maior do que Saldo!" 
        else:
            self.numero = randint(1,6)
            if self.numero > 3:
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Você Ganhou!"
                self.banco += float(self.valorap)*2
                self.valban['text'] = str(self.banco)
                
            if self.numero < 3 :
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Você Perdeu!"
                self.banco -= float(self.valorap)
                self.valban['text'] = str(self.banco)

            if self.numero == 3:
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Empate!"
    
    
    
    def jogaDadoMenor(self):
        self.valorap = self.en.get() 


        if float(self.valorap) > self.banco: 
            if self.banco == 0:
                self.gameOver()
            else:
                self.lb2['text'] = "Aposta maior do que Saldo!" 
        else:      
            self.numero = randint(1,6)

            if self.numero < 3:
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Você Ganhou!"
                self.banco += float(self.valorap)*2
                self.valban['text'] = str(self.banco)
            if self.numero > 3:
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Você Perdeu!"
                self.banco -= float(self.valorap)
                self.valban['text'] = str(self.banco)
            if self.numero == 3:
                self.lb2['text'] = "Caiu: " + str(self.numero) + "\n Empate!"


    def gameOver(self):      
        self.msg.pack_forget()
        self.lb.pack_forget()
        self.en.pack_forget()
        self.valban.pack_forget()
        self.lb.pack_forget()
        self.bmaior.pack_forget()
        self.bmenor.pack_forget()
        self.lb2['text'] = "Você perdeu todo o seu dinheiro e foi expulso do Casino!"


casino2 = App()
casino2.geometry("350x200")
casino2.title("Casino")
casino2.mainloop()
