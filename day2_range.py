print("①")
for i in range(5):
	print(i)
print("②")
for i in range(2,5):
	print(i)

def calc_hypotenuse(x,y):
	ans = (x**2 + y**2)**(1/2)
	return ans

ans = calc_hypotenuse(5,12)
print(ans)

print("斜辺の長さは{:.2f}".format(ans))
