data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # 快速計數
		if count % 10000 == 0: #除1000餘0時數一次
		# %是指餘數，譬如10 % 6 = 4(10除6餘4)；15 % 15 = 0
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data: # 清單data裡有d個字串(d篇留言)
	sum_len = sum_len + len(d) # 每篇字數加總
print('平均每筆留言長度為', sum_len/len(data)) 
#後面除以data篇留言(100萬筆)

# 篩選留言長度
new =[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100字')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])
