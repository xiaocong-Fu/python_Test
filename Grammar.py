# 数据类型：Number,String,Tuple,    List,Dictionary,Set
# a,b,c,d = 1000,3.14,"dadad",'y'
#
# print(type(a),type(b),type(c),type(d))
# print(isinstance(a,int))

# 字符串变大小,合并拼接使用+号
# testChar = 'david  beikehanmu'
# print(testChar.title())
# print(testChar.upper() + 'is got UP')
# print(testChar.lower() + 'is got low')

# 空白格\t，换行符\n
# print("\txixix")
# print('language:\n\tChinese\n\tEnglish\n\tSpain')

# 删除空白格
# message = '       Talents come from diligence, and knowledge is gained by accumulation        '
# print(message)
# message = message.rstrip()    #删除末尾的空白格
# print(message)
# message = message.lstrip()    #删除前头的空白格
# print(message)
# message = message.strip()       #同时删除两端的空白格
# print(message)
#
# print(message.replace(" ",""))  #删除全部空格
# ########-----删除全部空格-----
# message_1 = message.split()
# print(message_1)
# message_2 = "".join(message_1)
# print(message_2)

# ####----------快捷使用--------
# print("".join(message.split()))

# # 函数str()----非字符串转变为字符串
# age = 23
# print("dasdsada"+ str(age) + 'dasdasda ')


# ---------列表----------
list_1 = ['das', 123, "dasdasd", [899, 'dasdad']]
# print(list_1[-1])                                   #访问最后一个元素
# print(list_1 [3])
# print(list_1[-2] + "   "+list_1[2])
# print(str(list_1[-3])  + "   " +str(list_1[1]))
# print(list_1[-4] + "   " + list_1[0])
# list_1[-1] = 2*3
# list_1.append(75*10)                               #最后增加
# list_1.append(['dasada',456])
# list_2 = ['jhgjghj',580]
# list_1.append(list_2)
# list_1.insert(-1,'bbbbbb')                         #指定索引处插入
# del list_1[-1]                                      #删除元素
# print(list_1.pop(1))                                #pop（）删除列表最后一个元素,把最后一个元素储存起来，pop(index)删除列表指定元素,把指定储存起来
# list_1.remove(123)                                    #remove()删除指定的值
# print(list_1())

list_3 = [10, 20, 30, 50, 100, 57, 555]
# list_4 = ['abc','kkk','ooo','bbb']
# #list_5 = [[111,'llll'],['wwww',"ccccc"],[222,666]]
# list_3.sort()                                         #sort()永久性改变列表的排列顺序
# list_4.sort()
# #list_5.sort()                                        #列表之间排序失败
# print(list_3)
# list_3.sort(reverse=True)                             #反向排列，reverse = True
# list_3.sort()
# print(list_3)
# print(sorted(list_3))                                 #sorted（）临时改变列表的排序
# list_4.sort()
# print(list_4)
# print(sorted(list_4))
# #print(list_5)
# list_3.reverse()                                       #永久性反向显示

# print(list_3[len(list_3) - 1])
# print(list_3[list_3.__len__() - 2])

# print("test commit to Git")

# -------------------遍历列表---------------------
# -----for循环------
# list_7 = ["fxc", "dc", "lcl", "lw", "gql"]
# for list_index_item in list_7:
#     print(list_index_item,end = '\t')
# ----数值列表----函数range()----包括左边界不包括右边界
for value in range(5,10):
    print(value,end='\t')

