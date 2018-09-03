import re
# str1 = 'zdg # 12344321 # zdg@csdn.net'
# pattern =  re.compile(" # ")
# m = re.split(pattern,str1)
# print(m)
# # count = str1.count('#')
# # print(count)
# # str2=(''.join(str1.split())).split('#')

# # print(str2)

f = open('csdn.txt','r',encoding='utf-8')
if not f:
    print("打开失败")

count = 0
while True:
    count += 1
    print(count)
    string = f.readline()
    print(string)
    if not string:
        print("文件读取到末尾")
        break
print("关闭文件")
f.close()