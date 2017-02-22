from math import sin , cos , pi , fabs

equals = []
num = 0;
while num < 100000:
	if fabs(sin(num) - sin(pi*num/180)) < 0.000001:  # 10^-6
		equals.append(num)
	num = num + 1

print equals
print sin(72385)
print sin(pi*72385/180)