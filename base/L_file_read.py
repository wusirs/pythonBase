# 读文件

# open(name, mode, encoding) 打开一个已经存在的文件或创建一个新文件
# 参数 mode: r（读，如果文件不存在抛异常） w（写，如果文件已经存在，删除文件的原有内容，如果不存在，新建文件）
# a（追加，如果有文件不存在，新建文件，如果文件已经存在，在原有文件之后追加文件）
f = open('test.txt', 'r', encoding='UTF-8')

#  read() 默认读取全部内容，可以传一个数字表示读取的字节数
# f.read()

# print(f.read(2))


# readLine() 读一行
# print(f.readline())

# readLines() 读取全部行到列表中

# 利用for循环逐行读取
for line in f:
    print(line.strip("\n"))

#  关闭文件
f.close()

with open('test.txt', 'r', encoding='UTF-8') as fa:
    for line in fa:
        print(line.strip("\n"))
    f.close()
