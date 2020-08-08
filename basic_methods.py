# open打开文件，并且返回文件操作对象
# read将文件读取到内存
# write将指定内容写入文件
# close关闭文件
file = open("README")  # 不指定参数则为只读
text = file.read()
print(text)
print(len(text))
print("-"*50)
text = file.read()
print(text)
file.close()
print(len(text))

# 文件指针
# 第一次打开文件，通常指针会指向文件的开始位置
# 当执行read后，指针会移动到读取内容末尾
