from __future__ import unicode_literals
import random,time
def mergesort(list,empty_list):
	n = len(list)
	if ( n < 2 ):
		return
	half_size = n/2
	left_list = list[:half_size]
	right_list = list[half_size:]
	mergesort(left_list,empty_list)
	mergesort(right_list,empty_list)
	Merge(left_list,right_list,empty_list)

def Merge(left_list,right_list,list):
	left_index = len(left_list) -1
	right_index = len(right_list) -1
	left_start = 0
	right_start = 0
	while left_start < left_inde
def main():
	list = [1,2,3,5]
	empty_list = []
	mergesort(list,empty_list)
	print empty_list

if __name__ == "__main__":
	main()
