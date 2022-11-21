def bin(num):
	if (num == 0):
		return
	x = num % 3
	num //= 3
	if (x < 0):
		num += 1
	bin(num)

	if (x < 0):
		print(x + (3 * -1),end="")
	else:
		print(x,end="")


def check(Decimal):

	if Decimal != 0:
		bin(Decimal)
	else:
		print("0")


check(int(input("enter Decimal:  ")))
