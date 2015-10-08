from __future__ import unicode_literals
import random,time
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

def main():
	list = [112,3,5]
	a = mergesort(list)

	print a 
if __name__ == "__main__":
	main()
