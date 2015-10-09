from __future__ import unicode_literals
from decimal import *
import random, time,timeit,sys
sys.setrecursionlimit(10000)
def swap(list,a,b):
	temp = a
	a_index = list.index(a)
	b_index = list.index(b)
	list[a_index] =	b
	list[b_index] = temp

def partition(list,start,end):
	i = start - 1
	for j in xrange(start,end):
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
	pivot_index = random.randrange(start, end+1)
	swap(list,list[pivot_index],list[end])	
	i = start - 1
	for j in xrange(start,end):
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
	
# quicksort with median-of-three and cutoff for small arrays

def median_partition(list, start,end):
	middle = (start + end)/2
	pivot_index = median(list,start,end,middle)
	swap(list,list[pivot_index],list[end])	
	i = start - 1
	for j in xrange(start,end):
		if list[j] <= list[end]:
			i = i + 1
			swap(list,list[i],list[j])
	swap(list,list[i+1],list[end])	
	return i + 1

def median_quicksort(list,start,end):
	if start < end:
		q = median_partition(list,start,end)
		median_quicksort(list,start,q-1)
		median_quicksort(list,q+1,end)

def median( list, start, end, middle):
	if list[start] < list[end]:
		return end if list[end] < list[middle] else middle
	else:
		return start if list[start] < list[middle] else middle

########################################################################
	
		
def generate_input(size):
	list = []
	for element in xrange(0,size):
		list.append(element)
	sample_input = random.sample(list,size)
	return sample_input

def generate_worst_input(size):
	list = []
	reverse_list = []
	for element in xrange(0,size):
		list.append(element)
	for reverse in list:
		reverse_list.append(reverse)
	return reverse_list



def build_in_sort(list):
	start_time = time.time()
	end = len(list) - 1	
	sorted(list)
	end_time = time.time()
	time_spent = end_time - start_time
	return time_spent

def decorator_for_quicksort_time(func):
	def func_wrapper(*args,**kwargs):
		start_time = timeit.default_timer()
		func(args[0])	
		end_time = timeit.default_timer()
		time_spent = end_time - start_time
		return time_spent
	return func_wrapper	

@decorator_for_quicksort_time
def test_randomized_quicksort(list):
	return randomized_quicksort(list,0,len(list)-1)

@decorator_for_quicksort_time
def test_normal_quicksort(list):
	return quicksort(list,0,len(list)-1)

@decorator_for_quicksort_time
def test_median_quicksort(list):
	return median_quicksort(list,0,len(list)-1)


def decorator_for_average(func):
	def func_wrapper(*args,**kwargs):
		return 0
	return 0

def test_for_randomized_qsort():
	size_list = [1,10,100,1000]
	for	size in size_list:
		list = generate_worst_input(size)
		time_list = []	
		for count in xrange(1,5):
			time_list.append(test_randomized_quicksort(list))
		average = 1.0 * (sum(time_list)/len(time_list))
		print average
	return 0


def test_for_median_qsort():
	size_list = [1,10,100,1000]
	for	size in size_list:
		list = generate_worst_input(size)
		time_list = []	
		for count in xrange(1,5):
			time_list.append(test_median_quicksort(list))
		average = 1.0 * (sum(time_list)/len(time_list))
		print average
	return 0

def decorator_for_test(func):
	def func_wrapper(*args,**kwargs):
		time_list = []
		for count in xrange(1,5):
			time_list.append(func(args[0]))
			#time_list.append(func(list))	
		average = 1.0 * (sum(time_list)/len(time_list))
		return average	
	return func_wrapper

@decorator_for_test
def test_for_normal_qsort(list):
	return test_normal_quicksort(list)


def main():
	list_a = generate_input(10000)
	list_b = list_a
	list_c = list_a
	#print test_normal_quicksort(list_a)
	size_list = [1,10,100]
	for size in size_list:
		input = generate_input(size)	
		
		print test_for_normal_qsort(input)
	#print test_median_quicksort(list_c)
	print test_randomized_quicksort(generate_input(100),0,len(generate_input(100))-1)

if __name__ == "__main__":
	main()
#	test_for_normal_qsort()
#j	test_for_randomized_qsort()
#	test_for_median_qsort()





