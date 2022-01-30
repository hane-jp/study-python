def calc_bmi(x,y):
	ans = y/(x*x)
	return ans

x = 2
y = 80

if ans < 18:
	print("痩せ気味")
elif 18 <= ans < 25:
	print("普通")
elif ans >= 25:
	print("太り気味")
