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


# ------------------------------------------------------------------列表----------------------------------------------------------------
# list_1 = ['das', 123, "dasdasd", [899, 'dasdad']]
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

# list_3 = [10, 20, 30, 50, 100, 57, 555]
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
# for value in range(5,10):
#     print(value,end='\t')
# list()函数，可将range()数值列表直接转化成列表
# list_8 = list(range(0,11))
# print(list_8)
# print(type(list_8))
# print(list(range(1,6)))

# print(list(range(0,15,3)))                              #----跨数值取值
# print(list(range(5,100,11)))

# list_9 = []
# for value in range(1,11):
#     list_9.append(2 ** value)                             #  ** 表示乘方
# print(list_9)
# # 用于数值列表的函数
# print(max(list(range(0,100))))
# print(min(list(range(0,101))))
# print(sum(list(range(0,101))))
# list_9 = [3**value for value in range(1,11)]                # 生成数值列表
# print(list_9)

# -----列表切片-----
# print(list_7[0:2])
# print(list_7[1:4])
# print(list_7[2:])
# print(list_7[2:len(list_7)])
# print(list_7[-3:-1])

# # 遍历中使用切片
# for value in list_7[1:5]:
#     print(value.title(),end='\t')

# -----复制列表-----
# old_list = ['fxc','bh','cdj','lcl','dc','lw']
# new_list = old_list[1:4]                                  # 改变新的变量，旧的变量不会改变
# new_list.append('xiyang')
# print(new_list)

# new2_list = old_list                                        # 两个变量指向相同的列表地址，所以改变新的变量旧的变量也会改变
# new2_list.append(['xinyang','dz'])
# print(old_list)
# print(new2_list)

# ---------------------------------------------------------------------------元组（不可修改元素）---------------------------------------------------------------
# yuanzu_1 = ('sss',111,['dddd',3333],999)
# print(yuanzu_1[0])
# yuanzu_1[2].append('pppppp')
# print(yuanzu_1[2])
#
# # 整体修改元组元素                                              # 不可以单个修改元组的元素，可以整体修改元组
# yuanzu_2 = ('rrrrr',9999,'fffff',8888)
# yuanzu_2 = (111,222,333,444)
# print(yuanzu_2)

# -------------------------------------------------------------------------if语句---------------------------------------------------------------------------
# age = 100
# if age > 30 and age > 70 :
#     print('top')
# if age < 50 or age > 80 :
#     print('middle')
# elif age == 100:
#     print('100')
# else:
#     print('NONE')

# # 检查列表中的值
# list_10 = ['fxc','fc','fxz','gl','lw','jxq']
# print('fxc' in list_10)
# print('hhh' in list_10)
# if 'fxc' in list_10 :                                           # 存在于列表中
#     print('good')
# if 'haha' not in list_10:                                       # 不存在于列表中
#     list_10.append('haha')
#     print(list_10)

# if (1,2,3,4,5):
#     print('True')
# else:
#     print('False')

# # Test01-----序数筛选
# for value in range(1,10):
#     if value == 1:
#         print('1st')
#     elif value == 2:
#         print('2ed')
#     elif value == 3:
#         print('3rd')
#     else:
#         print(str(value)+'th')

# # Test02-----for-if使用
# # user_list = ['fxc','fc','fxz','gl','lw','admin']
# user_list = []
# if user_list:
#     for user_name in user_list:
#         if user_name == 'admin':
#             print(user_name+'\tgood')
#         else:
#             print(user_name+'\tunbelieveable')
# else:
#     print('list is null')

# # -----------------------------------------------------------------------------字典-----------------------------------------------------------------------
# user_imformation = {'name':'fxc','age':25,120:'heaviey','other':['other_1','other_2','other_3'],'another':{'another_1':11111,'another_2':22222}}
# # 添加键值对
# user_healthy = {}
# user_healthy['Heigh'] = 175
# user_healthy['heavey'] = 120
# user_healthy['3W'] = {'xw':50,'yw':40,'tw':10}
# # user_healthy['heavey'] = 115
# # 删除键值对
# del user_healthy['3W']
# print(user_healthy)

# 遍历字典
# user_0 = {
#     'username':'fxc',
#     'first_name':'f',
#     'last_name':'xc',
# }
# for key ,value in user_0.items():                                       # 注意for循环后字典的写法：user_0.items()
#     print('Key : ' + key)
#     print('value : ' + value)

# 遍历字典中所有的键
# for key in user_0.keys():                                                  # keys()实际返回一个列表，包含字典中所有的键
#     print(key)

# favorite_language = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python',
#     'aliex':'java',
# }
# for name in sorted(favorite_language.keys()):
#     print(name)

# 遍历字典中所有的值
# for language in favorite_language.values():                               #value()实际返回一个列表，包含字典中所有的值
#     print(language)
# for language in set(favorite_language.values()):                            # set()函数剔除重复的值
#     print(language,end='\t')

# 字典嵌套
# # 1.列表中储存字典
# # 2.字典中储存列表
# favorite_language_01 = {
#     'jen':['python','ruby'],
#     'sarch':['c'],
#     'edward':['ruby','go'],
#     'phil':['python','java'],
# }
# for name , language in favorite_language_01.items():
#     if len(language) > 1:
#         print(name.title() + '\tare')
#         for language_01 in language:
#             print('\t' + language_01)
#     else:
#         print(name.title() + '\tis\t' + language[0])
# # 3.字典中储存字典

# # 控制台输入函数：input()
# message = 'if you tell us who you are ......'
# message += '\nWhat is you name ? '
# name = input(message)
# print('\nhi ' + name)

# # int()转化数字
# height = input('how tall are you ?\n')
# height = int(height)
# if height > 180:
#     print('OK')
# else:
#     print('NO')
# # ----------------------------while循环---------------------------
# prompt = 'Tell me something ,and i will repeat it back to you '
# prompt += '\nEnter quit to end the program....\n'
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# # -----使用标志-----
# prompt = 'Tell me something ,and i will repeat it back to you '
# prompt += '\nEnter quit to end the program....\n'
# # message = ''
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     if message != 'quit':
#         print(message)
# -----使用break退出循环-----
# -----在循环中使用continue-----
# current_number = 0
# while current_number < 10 :
#     current_number += 1
#     if current_number% 2 == 0:
#         continue                                                            #执行完continue后再不执行此次循环的剩余语句。
#     print(current_number)
# # 不同年龄的电影票
# message = 'Please tell me how old are you \n'
# active = True
# while active:
#     age_str = input(message)
#     if age_str.isdigit():                                                     #age_str.isdigit():检测一个字符串是不是纯数字（不包含判断带浮点的数字）
#         age = int(age_str)
#         print(age)
#         if age <= 3 :
#             print('you are freefom')
#         if age > 3 and age <=12 :
#             print('you should pay 10$')
#         if age > 12:
#             print('you should pay 15$')
#         active = False
#     else:
#         continue

# #判断一个字符串是否是纯数字（包括浮点数）
# def is_number(str):
#     try:
#         float(str)
#         return True
#     except ValueError:
#         pass
#
#     try:
#         import unicodedata
#         unicodedata.numeric(str)
#         return True
#     except (TypeError,ValueError):
#         pass
#     return False
#
# print(is_number('fool'))
# print(is_number('100'))
# print(is_number(' '))
# print(is_number('1.555'))
# print(is_number('-2.666'))
# print(is_number('2e5'))
# print(is_number('3fxc'))

# while循环结束，函数结束，这主要有，参数传递，模块调用
