data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # 快速計數
		if count % 1000 == 0: #除1000餘0時數一次
		# %是指餘數，譬如10 % 6 = 4(10除6餘4)；15 % 15 = 0
		print(len(data))
print(len(data))

print(data[0])
print('-----------------')
print(data[1])