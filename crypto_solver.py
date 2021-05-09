import random


def same_number(a, b, thresh=10e-6):
	if abs(a - b) < thresh:
		return True
	else:
		return False


def possible_results_two(a, b):
	res = dict()
	res[a + b] = f'({a}+{b})'
	res[a - b] = f'({a}-{b})'
	res[a * b] = f'({a}*{b})'
	if b != 0:
		res[a / b] = f'({a}/{b})'

	# dicc result: [used numbers] , [used operations]
	# If a key was already in the dicc, it overwrites it.
	return res


def possible_results_three(a, b, c):
	res = dict()
	numbers = [a, b, c]
	for x in numbers:
		numbers_temp = numbers.copy()
		numbers_temp.remove(x)
		for y in possible_results_two(numbers_temp[0], numbers_temp[1]).keys():
			y_ops = possible_results_two(numbers_temp[0], numbers_temp[1])[y]
			for z in possible_results_two(y, x).keys():
				z_ops_1 = possible_results_two(y, x)[z]

				z_ops_final = z_ops_1.replace(f'{y}', y_ops, 1)

				res[z] = z_ops_final

		for y in possible_results_two(numbers_temp[1], numbers_temp[0]).keys():
			y_ops = possible_results_two(numbers_temp[1], numbers_temp[0])[y]
			for z in possible_results_two(y, x).keys():
				z_ops_1 = possible_results_two(y, x)[z]

				z_ops_final = z_ops_1.replace(f'{y}', y_ops, 1)

				res[z] = z_ops_final

	return res


def possible_results_four(a, b, c, d):
	res = dict()
	numbers = [a, b, c, d]
	for x in numbers:
		numbers_temp = numbers.copy()
		numbers_temp.remove(x)
		for y in possible_results_three(numbers_temp[0], numbers_temp[1], numbers_temp[2]).keys():
			y_ops = possible_results_three(numbers_temp[0], numbers_temp[1], numbers_temp[2])[y]
			for z in possible_results_two(y, x).keys():
				z_ops_1 = possible_results_two(y, x)[z]

				z_ops_final = z_ops_1.replace(f'{y}', y_ops, 1)

				res[z] = z_ops_final

	return res


def solve_game(a, b, c, d, target=24):

	for result in possible_results_four(a, b, c, d).keys():
		if same_number(result, target):
			return possible_results_four(a, b, c, d)[result]

	return None


def possible_natural_outcomes(a, b, c, d):
	dic = possible_results_four(a, b, c, d)
	outcomes_temp = list(dic.keys())
	outcomes = []
	for outcome in outcomes_temp:
		if isinstance(outcome, int) and outcome >= 0:
			outcomes.append(outcome)
	outcomes.sort()

	return outcomes


def possible_integer_outcomes(a, b, c, d):
	dic = possible_results_four(a, b, c, d)
	outcomes_temp = list(dic.keys())
	outcomes = []
	for outcome in outcomes_temp:
		if isinstance(outcome, int):
			outcomes.append(outcome)
	outcomes.sort()

	return outcomes


def shuffle(upper_bound=12):
	a, b, c, d, e = (random.randint(1, upper_bound) for _ in range(5))
	return a, b, c, d, e



