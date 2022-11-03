# 读文件

# open(name, mode, encoding) 打开一个已经存在的文件或创建一个新文件
# 参数 mode: r（读） w（写） a（追加）
f = open('test.txt', 'r', encoding='UTF-8')


#  read() 默认读取全部内容，可以传一个数字表示读取的字节数
f.read()

# print(f.read(2))


# readLine() 读一行
# print(f.readline())

# readLines() 读取全部行到列表中