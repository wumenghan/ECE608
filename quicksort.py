from __future__ import unicode_literals
import random, time,timeit,sys
def swap(list,a,b):
	temp = a
	a_index = list.index(a)
	b_index = list.index(b)
	list[a_index] =	b
	list[b_index] = temp
# original quicksort

def partition(list,start,end):
	i = start - 1
	for j in range(start,end):
		if list[j] <= list[end]:
			i = i + 1
			swap(list,list[i],list[j])
	swap(list,list[i+1],list[end])	
	return i + 1

def quicksort(list,start,end):
	if start < end:
		q = partition(list, start, end)
		quicksort(list, start, q - 1)
		quicksort(list, q + 1 ,end)
	
# quicksort with randomized pivot value

def randomized_partition(list,start,end):
	pivot = random.choice(list)
	pivot_index = list.index(pivot)
	swap(list,list[pivot_index],list[end])	
	i = start - 1
	for j in range(start,end):
		if list[j] <= list[end]:
			i = i + 1
			swap(list,list[i],list[j])
	swap(list,list[i+1],list[end])	
	return i + 1

def randomized_quicksort(list,start,end):
	if start < end:
		q = randomized_partition(list,start,end)
		randomized_quicksort(list, start, q-1)
		randomized_quicksort(list, q+1 , end)
########################################################################
def generate_input(size):
	list = []
	for element in range(0,size):
		list.append(element)
	sample_input = random.sample(list,size)
	return sample_input

def test_randomized_quicksort(list):
	start_time = time.time()
	end = len(list) - 1	
	randomized_quicksort(list,0,end)
	end_time = time.time()
	time_spent = end_time - start_time
	return time_spent

def test_normal_quicksort(list):
	start_time = time.time()
	end = len(list) - 1	
	quicksort(list,0,end)
	end_time = time.time()
	time_spent = end_time - start_time
	return time_spent

def main():
	size = 10000
	list = generate_input(size)
	normal_time = test_normal_quicksort(list)
	randomized_time = test_randomized_quicksort(list)
	print normal_time
	print randomized_time
if __name__ == "__main__":
	main()