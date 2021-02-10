class Crypto():

	def __init__(self, card1, card2, card3, card4, target):
		self.card1 = card1
		self.card2 = card2
		self.card3 = card3
		self.card4 = card4
		self.target = target
		self.umbral = 10e-6

	def _possible_results_two(self,a,b):
		res = dict()
		res[a+b] =  f'({a}+{b})'
		res[a-b] = f'({a}-{b})'
		res[b-a] = f'(-{a}+{b})'
		res[a*b] = f'({a}*{b})'
		if b != 0:
			res[a / b] = f'({a}/{b})'
		if a != 0:
			res[b / a] =  f'(1/{a}*{b})'

		#dicc result: [used numbers] , [used operations]
		#If a key was already in the dicc, it overwrites it.
		return res

	def _possible_results_three(self,a,b,c):
		res = dict()
		numbers = [a,b,c]
		for x in numbers:
			numbers_temp = numbers.copy()
			numbers_temp.remove(x)
			for y in self._possible_results_two(numbers_temp[0],numbers_temp[1]).keys():
				y_ops = self._possible_results_two(numbers_temp[0],numbers_temp[1])[y]
				for z in self._possible_results_two(y,x).keys():
					z_ops_1 = self._possible_results_two(y,x)[z]

					z_ops_final = z_ops_1.replace(f'{y}',y_ops,1)
					
					res[z] = z_ops_final

		return res

	def _possible_results_four(self,a,b,c,d):
		res = dict()
		numbers = [a,b,c,d]
		for x in numbers:
			numbers_temp = numbers.copy()
			numbers_temp.remove(x)
			for y in self._possible_results_three(numbers_temp[0],numbers_temp[1], numbers_temp[2]).keys():
				y_ops = self._possible_results_three(numbers_temp[0],numbers_temp[1], numbers_temp[2])[y]
				for z in self._possible_results_two(y,x).keys():
					z_ops_1 = self._possible_results_two(y,x)[z]

					z_ops_final = z_ops_1.replace(f'{y}',y_ops,1)
					
					res[z] = z_ops_final

		return res


	def _same_number(self,a,b):
		if abs(a-b) < self.umbral:
			return True
		else:
			return False


	def solveGame(self):
		
		for result in self._possible_results_four(self.card1, self.card2, self.card3, self.card4).keys():
			if self._same_number(result, self.target):
				return(self._possible_results_four(self.card1, self.card2, self.card3, self.card4)[result])

		return None


print('choose 4 card numbers: ')

card1 = int(input())
card2 = int(input())
card3 = int(input())
card4 = int(input())

print('choose a target card number: ')

target = int(input())

crypto_game = Crypto(card1, card2, card3, card4, target)

print(crypto_game.solveGame())
