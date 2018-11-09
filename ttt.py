import random,os
class Tic_tac_toe:
	def __init__(self,user_1,user_2):
		self.user_1=user_1
		self.user_2=user_2
		self.winner_declared=False
		self.matrix=[[1,2,3],[4,5,6],[7,8,9]] #initial introduction
		self.new_matrix=[[' ',' ',' '] for empty in range(3)] #creating empty matrix
		self.numbers_data_base=[numbers for numbers in range(1,10)]#storing numbers from 1 to 9
	def pic_user(self):
		self.data_base=['X','O']
		self.user_1_choice=random.choice(self.data_base)#selecting random user
		self.data_base.remove(self.user_1_choice)
		self.user_2_choice=self.data_base[0]
		print("---------------------------")
		print(f"{self.user_1} represent's : {self.user_1_choice}\n")
		print(f"{self.user_2} represent's : {self.user_2_choice}")
		print("---------------------------\n")
	def draw_board(self):
		self.diagonal_result_1=[]#Main Logic and Brain of Tic_tac_toe in coming description
		self.diagonal_result_2=[]
		print("Please remember the following representation\n")#simple introduction
		print("Representing T-i-c T-a-c T-o-e Matrix \n")
		print("-------------------")
		for e1,e2,e3 in self.matrix:
			print(f"|  {e1}  |  {e2}  |  {e3}  |")
			print("-------------------")
		print()
		for select in range(1,10):# used mainly to provide equal opportunity to 2 user's
			if select%2!=0:
				self.user_select=self.user_1
				self.user_symbol=self.user_1_choice
				print(f"You have {len(self.numbers_data_base)} choice's {self.numbers_data_base}\n")
				print(f"{self.user_select} please choose a number to place : {self.user_symbol}\n")
				self.number=int(input("Enter the number : "))
				self.numbers_data_base.remove(self.number)
			else:
				self.user_select=self.user_2
				self.user_symbol=self.user_2_choice
				print(f"You have {len(self.numbers_data_base)} choice's {self.numbers_data_base}\n")
				print(f"{self.user_select} please choose a number to place : {self.user_symbol}\n")
				self.number=int(input("Enter the number : "))
				self.numbers_data_base.remove(self.number)	
			os.system("cls")
			print("-------------------")
			for first in range(0,3):#Real Brain of Tic_tac_toe
				for final in range(0,3):
					if self.matrix[first][final]==self.number:#placing the user symbol in given number
						self.new_matrix[first][final]=self.user_symbol#place the symbol at given number
						self.column_result=[entry[final] for entry in self.new_matrix]#column assignment
						self.diagonal_result_1=([self.new_matrix[i][i] for i in range(0,3)])#diagonal 1 assignment 
						self.diagonal_result_2=([self.new_matrix[i][~i] for i in range(0,3)])#diagonal 2  -;;-
						# (~) is a not operator (-x -1)
						for play in range (0,3):
								if self.new_matrix[play].count(self.user_symbol)==3:#if common symbol in row
									self.winner_declared=True
								elif self.column_result.count(self.user_symbol)==3:#-----::------- in column
									self.winner_declared=True	
								elif (self.diagonal_result_1.count(self.user_symbol))==3 or (self.diagonal_result_2.count(self.user_symbol))==3:#-------;;----- in diagonal
									self.winner_declared=True
						for e1,e2,e3 in self.new_matrix:#printing Tic_tac_toe matrix after each input
							print(f"|  {e1}  |  {e2}  |  {e3}  |")
							print("-------------------")
						if self.winner_declared==True:
							os.system('cls')
							print("-------------------")#printing Tic_tac_toe matrix after winning 
							for e1,e2,e3 in self.new_matrix:
								print(f"|  {e1}  |  {e2}  |  {e3}  |")
								print("-------------------")
							print(f"\nWinner : {self.user_select} with the symbol : {self.user_symbol}\n")
							user_final_request=input("Press Y to play again any other key to quit : ").upper()
							os.system("cls")
							return(user_final_request)
		if self.winner_declared==False:
			print("\nWow close moves but it's a draw :(\n")
			user_final_request=input("Press Y to play again any other key to quit : ").upper()
			os.system("cls")
			return(user_final_request)
#if __name__=="__main__":
#print("\nDesigned and developed by { Chaitanya Krishna VB }\n")
print("Welcome to T-i-c T-a-c T-o-e \n")
print("This is a multi player game\n")
user_choice=int(input("Enter 1-Play 2-Quit : "))
while True:
	if user_choice==1:
		user_1=input("\nEnter Name for user - 1 : ")
		user_2=input("\nEnter Name for user - 2 : ")
		os.system("cls")
		fun=Tic_tac_toe(user_1,user_2)
		fun.pic_user()
		user_final_request=fun.draw_board()
		if user_final_request=="Y":
			continue
		else:
			break
	elif user_choice==2:
		break
	else:
		print("Invalid choice")
