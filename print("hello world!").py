subject_name = ["国語","算数","理科","社会"]
print(subject_name)
print(type(subject_name))

print(subject_name[1])
print(subject_name[0:2])

subject_name.append("追加")
print(subject_name)

subject_name.extend(["追加A","追加B"])
print(subject_name)

subject_name.insert(2, "割り込み")
print(subject_name)

subject_name.remove("割り込み")
print(subject_name)

subject_name[0] = "Japanese"
print(subject_name)

subject_dict = {"国語":70, "算数":80, "理科":100}
print(subject_dict)

print(subject_dict["算数"])

subject_dict["英語"] = 90
print(subject_dict)

subject_dict.pop("算数")
print(subject_dict)

sample_set = {10,100,"hello"}
print(sample_set)

sato_dict = {"height":1.5,"weight":45}
sato_bmi = sato_dict["weight"] / (sato_dict["height"] * sato_dict["height"])

print(sato_bmi)

for i in [1,2,3]:
	print(i)

count = 1
while count <= 3:
	print(count)
	count = count + 1

score = 95
if score >= 90:
	print("優")
elif 90 > score and score >= 70:
	print("良")
elif 70 > score and score >= 60:
	print("可")
else:
	print("不可")


print(2**10)

ans = 1
for x in [1,2,3,4,5,6,7,8,9,10]:
	ans = ans * 2
print(ans)

count = 1
uns = 1
while count <= 10:
	uns = uns * 2
	count = count + 1
print(uns)