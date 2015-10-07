from __future__ import unicode_literals
import random,time
def mergesort(list):
	n = len(list)
	if ( n < 2 ):
		return
	half_size = n/2
	left_list = list[:half_size]
	right_list = list[half_size:]
	mergesort(left_list)
	mergesort(right_list)
	Merge(left_list,right_list,list)

def Merge(left_list,right_list,list):
	for left in left_list:
		for right in right_list:
			if left < right:
				list.append(left)
			else:
				list.append(right)

def main():
	list = [1,2,3,5,2,34,5]
	mergesort(list)
	print list

if __name__ == "__main__":
	main()
