
file = open("numbers.txt" , 'r')
numbers = []

n = file.read(1)
while n != "":
	numbers.append(n)
	n = file.read(1)

print numbers
print ""

"""
This loop does a bubble sort to order all the numbers in the array from file numbers.txt

"""

i = 0
temp = 0
while i < len(numbers):
	j = 0
	while j < len(numbers)-1:
		if numbers[j] > numbers[j+1]:
			temp = numbers[j+1]
			numbers[j+1] = numbers[j]
			numbers[j] = temp
		j = j + 1
	i = i + 1

print numbers
print ""

"""
Finds the number that is repeated the most and prints it out + the number of 
times it is present in the list of numbers. If 2 numbers are repeated the same 
number of times, the lower number is mentioned.
"""
max_count = 0
max_num = -1
count = 1
k = 0
while k < len(numbers)-1:
	if numbers[k] == numbers[k+1]:
		count = count + 1
	else:
		if max_count < count:
			#print "new max assigned"
			max_num = numbers[k]
			max_count = count
			count = 0
		else:
			#print "nothing"
			count = 0
	k = k + 1

print "the number %s is repeated the most. It was repeated %s times" % (max_num , max_count)
print ""









