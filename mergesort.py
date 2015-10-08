from __future__ import unicode_literals
import random,time,timeit
def mergesort(list):
	n = len(list)
	if ( n < 2 ):
		return list
	half_size = n/2
	left_list = mergesort(list[:half_size])
	right_list = mergesort(list[half_size:])
	result = []
	while len(left_list) > 0 and len(right_list) >0:
		if left_list[0] > right_list[0]:
			result.append(right_list.pop(0))
		else:
			result.append(left_list.pop(0))
	if len(left_list) > 0:
		result.extend(mergesort(left_list))
	else:
		result.extend(mergesort(right_list))
	return result

def test_mergesort(list):
	start  = timeit.default_timer()
	mergesort(list)
	end = timeit.default_timer()
	return end-start

def generate_input(size):
	list = []
	for element in range(0,size):
		list.append(element)
	sample_input = random.sample(list,size)
	return sample_input
	#return list
def main():
	size_list = [1,10,100,1000,10000]
	for size in size_list:
		list = generate_input(size)
		print test_mergesort(list)
if __name__ == "__main__":
	main()
