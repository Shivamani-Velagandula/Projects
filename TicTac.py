import tkinter as tk
from tkinter import messagebox

class game:
    def __init__(self):
        self.currentplayer="X"
        self.board=[["","",""],["","",""],["","",""]]
        self.window=tk.Tk()
        self.window.title("Tictac game")

        self.buttongrid=[]
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.window,text="",width=10,height=10,command=lambda i=i,j=j:self.make_move(i,j))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttongrid.append(row)


    def make_move(self,row,col):
        if self.board[row][col]=="":
            self.board[row][col]=self.currentplayer
            self.buttongrid[row][col].config(text=self.currentplayer)
            if(self.check_winner(self.currentplayer)):
                 messagebox.showinfo("game over",  "the winner is"+self.currentplayer)
                 self.window.quit()
            elif self.is_draw():
                 messagebox.showinfo("game over","its a draw")
                 self.window.quit()

            self.currentplayer="O" if self.currentplayer=="X" else "X"

    def check_winner(self,player):
        for i in range(3):
            if player==self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return True
            if player==self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return True
        if player==self.board[0][0]==self.board[1][1]==self.board[2][2]:
                return True
        if player==self.board[0][2]==self.board[1][1]==self.board[2][0]:
                return True
        return False
                        

    def is_draw(self):
        for row in self.board:
             if "" in row:
                return False            
             return True



    def run(self):
        self.window.mainloop()

g=game()
g.run()