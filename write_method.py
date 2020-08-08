# "w"只写，会覆盖原有内容
# “a”只写，追加方式
file = open("README", "a")
file.write("\n123Hello")
file.close()
print("_"*50)
file = open("README")
while True:
    text = file.readline()
    if not text:
        break
    print(text)
file.close()
