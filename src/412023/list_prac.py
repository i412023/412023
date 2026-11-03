list = ["AA", "BB", "CC"]
print(list)

list.append(50)
print(list)

list.remove(50)
print(list)

list[0] = "aa"
print(list)
print(list[-1])

print(f"list內有{len(list)}個元素")

for value in list:
    print(f"{value}，你好")

if "aa" not in list:
    print("不存在")
else:
    print("有存在")

print(f"aa在編號{list.index('aa')}的位置")