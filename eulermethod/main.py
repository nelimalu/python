initial_x = 0
initial_y = 1
h = 0.0005


def fprime(x, y):
	return y


def euler(prev_x, prev_y, goal):
	if prev_x < goal:
		return euler(prev_x + h, prev_y + h * fprime(prev_x, prev_y), goal)
	return prev_y


print(euler(initial_x, initial_y, 0.4))
	