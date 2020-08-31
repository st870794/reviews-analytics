## 讀取檔案
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

print(data[0])

## 留言單字查詢功能
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典
for word in wc:
	if wc[word] >100:
		print(word,wc[word]) # key跟出現次數

print(len(wc)) # 總共單字量
print(wc['Allen']) # 找尋特定單字

while True:
	word = input('請問您想查找的字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過的次數為： ', wc[word])
	else:
		print('此單字並不在清單內')

print('感謝使用本查尋功能')

## 計算留言平均長度
sum_len = 0
for d in data: # 清單data裡有d個字串(d篇留言)
	sum_len = sum_len + len(d) # 每篇字數加總
print('平均每筆留言長度為', sum_len/len(data)) 
# 後面除以data篇留言(100萬筆)

## 篩選留言長度、內容
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


