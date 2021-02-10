class Crypto():

	def __init__(self):
		self.umbral = 10e-6

	def _possible_results_two(self,a,b):
		res = dict()
		res[a+b] =  f'({a}+{b})'
		res[a-b] = f'({a}-{b})'
		res[a*b] = f'({a}*{b})'
		if b != 0:
			res[a / b] = f'({a}/{b})'

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

			for y in self._possible_results_two(numbers_temp[1],numbers_temp[0]).keys():
				y_ops = self._possible_results_two(numbers_temp[1],numbers_temp[0])[y]
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


	def solveGame(self, card1, card2, card3, card4, target=24):
		
		for result in self._possible_results_four(card1, card2, card3, card4).keys():
			if self._same_number(result, target):
				return(self._possible_results_four(card1, card2, card3, card4)[result])

		return None

	def possibleNaturalOutcomes(self, card1, card2, card3, card4):
		dic = self._possible_results_four(card1, card2, card3, card4)
		outcomes_temp = list(dic.keys())
		outcomes = []
		for outcome in outcomes_temp:
			if isinstance(outcome, int) and outcome >= 0:
				outcomes.append(outcome)
		outcomes.sort()

		return outcomes

	def possibleIntegerOutcomes(self, card1, card2, card3, card4):
		dic = self._possible_results_four(card1, card2, card3, card4)
		outcomes_temp = list(dic.keys())
		outcomes = []
		for outcome in outcomes_temp:
			if isinstance(outcome, int):
				outcomes.append(outcome)
		outcomes.sort()

		return outcomes

if __name__ == '__main__':
	
	cryptogame = Crypto()
	print(cryptogame.possibleNaturalOutcomes(1,2,3,4))


