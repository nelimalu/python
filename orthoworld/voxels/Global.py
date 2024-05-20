WIDTH = 800
HEIGHT = 600

def add(tuple1: tuple[int, int, int], tuple2: tuple[int, int, int]):
	assert len(tuple1) == len(tuple2)
	output = list(tuple1)
	for i in range(len(tuple2)):
		output[i] += tuple2[i]
	return tuple(output)

