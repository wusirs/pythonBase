# 文件写入
f = open('test.txt', 'w', encoding='UTF-8')
f.write("hello world\n")
f.write("你好世界\n")
f.flush()
f.close()  # close 方法内置flush方法的功能


f = open('test.txt', 'a', encoding='UTF-8')
f.write("hi,how are you?\n")
f.write("I'm fine\n")
f.flush()
f.close()
