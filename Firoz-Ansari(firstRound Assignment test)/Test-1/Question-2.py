
def myMax(list):
	# ------ Assume first number in list is largest----------
	max = list[0]
# Now traverse through the list and compare--------
	for x in list:
		if x > max:
			max = x

	# return the "max" value-------------------
	return max


# Driver code---------------
list = [10, 20, 10, 4, 45, 99]
print("Largest element is:", myMax(list))
