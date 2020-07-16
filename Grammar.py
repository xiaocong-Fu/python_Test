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

# # while中列表之间的移动
# unconfirmed_users = ['fxc','fxz','fc','gl']
# confired_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()                              # pop()每次一个从列表末尾删除元素,并返回该元素，永久删除
#     confired_users.append(current_user)
# for confired_user in confired_users:
#     print(confired_user)
# print(unconfirmed_users)

# # 用户输入填充字典
# responses = {}
# polling_active = True
# while polling_active:
#     name = input('What is you name?\n')
#     response = input('which would you tell me ?\n')
#     responses[name] = response
#     repeat = input('Will you Stop???\n(YES OR NO)\n')
#     if repeat == 'YES':
#         polling_active = False
# print(responses)

# -----------------------------------------------------函数----------------------------------------------------
# # 关键字实参
# def describe_pet(animal_type,pet_name):
#     print('My ' + animal_type + ' name is ' + pet_name + ' !!!!!!!!!!')
# describe_pet(animal_type='Dog',pet_name='yayaya')                               # 关键字实参就是赋予参数值时指定参数

# 参数默认值
# def describe_pet(pet_name,animal_type = 'Dog'):
#     animal_type = 'pig'
#     print('My ' + animal_type + ' name is ' + pet_name + ' !!!!!!!!!!')
# describe_pet(animal_type='Dog',pet_name='yayaya')

# # 返回值
# def get_formatted_name(first_name,last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name
# print(get_formatted_name('fu','xiaocong'))

# # 实参可选
# def get_formatted_name(first_name,last_name,middle_name = ''):                  # 默认参数必须放在最后
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name
#
# print(get_formatted_name('FU','xiaocong'))
# print(get_formatted_name('fu','xiaocong','GGGGGG'))

# # 返回字典
# def build_person(first_name,last_name,age = ''):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# print(build_person('FU','xiaocong'))
# print(build_person('FU','xiaocong',25))

# # 函数中修改列表
# unprited_designs = ['iphone','robot','case']
# completed_models = []
# def print_modles(unprited_designs,completed_models):                            # unprited_designs列表中的元素已经被修改
#     while unprited_designs:
#         current_design = unprited_designs.pop()
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     for completed_model in completed_models:
#         print(completed_model,end='\t')
# #
# # print_modles(unprited_designs,completed_models)
# # show_completed_models(completed_models)
#
# # 禁止函数修改列表
# print_modles(unprited_designs[:],completed_models)                              # unprited_designs列表中的元素没有被修改。  传递的是列表副本unprited_designs[:]
# show_completed_models(completed_models)

# # 传递任意数量实参
# def make_pizza(*toppings):
#     print(type(toppings))                                                          # 输出结果：<class 'tuple'>，(123, 'dasdasda', [1222, 'dasdas'])
#     print(toppings)                                                                # 参数储存在一个元组中
# make_pizza(123,'dasdasda',[1222,'dasdas'])


# # 任意数量关键字实参
# def build_profile(first,last,**user_info):
#     print(type(user_info))                                                          # 输出结果<class 'dict'>，任意数量关键字参数存在字典中
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key , value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('FU','xiaocong',age = 25,sex = 'male')                 # 注意：任意数量 关键字 参数的赋值方式：age = 25,sex = 'male'
# print(user_profile)


# 导入函数
# 方法一：import 模块名    导入模块中所有的函数，可使用该模块任意一个函数
#       调用方法：模块名.函数名（）
# 方法二：导入特定函数： from 模块名 import 函数名1，函数名2，函数名3
#       调用方法：直接使用函数名调用
# 方法三：使用as给函数指定别名：from 模块名 import 函数名1 as 别名1，函数名2 as 别名2，函数名3 as 别名3
#       调用方法：直接使用别名调用
# 方法四：使用as给模块指定别名：import 模块名 as 别名
#       调用方法：别名.函数名（）
# 方法五：导入模块中所有函数：from 模块名 import *               （不建议使用此方法，调用第三方库时会出现函数名重名的情况，导致结果未知）
#       调用方法：直接使用函数名调用

# # ------------------------------------------------------类--------------------------------------------------
# class Battery():
#     def __init__(self,battery_siaze):
#         self.battery_size = battery_siaze
#
#     def describe_battery(self):
#         print('from GGGGG This car has a ' + str(self.battery_size) + ' -kwh battery')
#
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 500
#         elif self.battery_size == 85:
#             range = 1000
#         else:
#             range = 500000
#         message = 'This car can go xxxxxxxxxxxx ' + str(range) + ' miles on a full charge!!!!'
#         print(message)

# ---------------------------------------------------文件和异常-----------------------------------------------
# 读文件
# with open('pai.txt') as file_object:                                        # 在于Grammar.py同级目录中寻找pai.txt，，with：让Python负责妥善地打开和关闭文件,只能在with方法内使用
#     print(type(file_object))                                                # 输出结果：<class '_io.TextIOWrapper'>
#     contents = file_object.read()
#     # print(contents)
#     print(contents.rstrip())                                                # rstrip()删除字符串末尾的空白。

# file = r'test_file\day_note.txt'                                              # 开头单引号前加r，可使用windows系统的路径
# with open(file) as file_object:                                               # 使用相对路径在不同文件夹中寻找day_note.txt（也可使用绝对路径，注意要是用'/'）
#     print(type(file_object))                                                  # 输出结果：<class '_io.TextIOWrapper'>
#     # contents = file_object.read()
#     # print(contents.rstrip())
#     # for line in file_object:
#     #     print(line.rstrip())
#     lines = file_object.readlines()                                           # readlines()读取文件中每一行,并将其存储在列表中,这个列表可在with函数外使用
#     print(type(lines))
#
# print(lines)

# filename = 'pai.txt'
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string[:30] + '.......')
# print(len(pi_string))
#
# if '19941006' in pi_string:
#     print('YES')
# else:
#     print('NO')

# 写文件
# filename = r'test_file\day_note.txt'
# with open(filename,'w') as file_object:                                         # 四种模式：'r'读模式，‘w’写模式，‘a’附加模式，‘r+’读取和写入文件模式
#     file_object.write('明日复明日，明日何其多')                                     # write（）会清空该文件之前的内容，python只能将字符串写入文本文件。
                                                                                #                       要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

# 写入多行
# filename = r'test_file\day_note.txt'
# with open(filename,'w') as file_object:
#     file_object.write('明日复明日，明日何其多\n')
#     file_object.write('山不在高，有仙则名\n')

# 附加模式打开文件，给文件添加内容，而不是覆盖原有的内容，文件不存在会创建一个空文件
# filename = r'test_file\day_note.txt'
# with open(filename,'a') as file_object:
#     file_object.write('水不在深，有龙则灵\n')
#     file_object.write('斯是陋室，惟吾德馨\n')
#
# filename = r'test_file\day_note_2.txt'
# with open(filename,'a') as file_object:
#     file_object.write('可以调素琴，阅金经，\n')
#     file_object.write('无丝竹之乱耳，无案牍之劳形\n')


# # read(),readline(),readlines()的区别：
# # read()函数，返回整个文件的内容成一个字符串，read(size)标识返回多少个字符的字符串。
# # readline()函数，按行读取文件，返回一行的字符串
# # readlines()函数，按行读取文件，返回一个字符串列表


# ------------------------------------------------------异常--------------------------------------------------
# 异常使用try--except代码块处理
# try-except-else代码块的工作原理大致如下：Python尝试执行try代码块中的代码；只有可能引发异常的代码才需要放在try语句中。
#       有时候，有一些仅在try代码块成功执行时才需要运行的代码；这些代码应放在else代码块中。except代码块告诉Python，如果它尝试运行try代码块中的代码时引发了指定的异常，该怎么办。

# 1.处理ZeroDivisionError异常                       division：除法
# print(5/0)
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('you cant division by zero')

# print('give me two number and i wll division them \nenter q to quit')
# while True:
#     first_number = input('fierst number is ')
#     if first_number == 'q':
#         break
#     second_number = input('second number is ')
#     if second_number == 'q':
#         break
#     # answer = int(first_number) / int(second_number)
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:                                                           # except代码块：依赖于try代码块失败执行的代码放到except代码块中。
#         print('you cant divison by 0')
#         # answer = 99999
#     else:                                                                               # else代码块：依赖于try代码块成功执行的代码都应放到else代码块中。
#         print(answer)

# 2.处理FileNotFoundError异常
# # 分析文本
# filename = r'test_file\day_note.txt'
# try:
#     with open(filename) as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     print('this file does not exit ')
# else:
#     words = contents.split()                                                                # split():以空格为分隔符将字符串拆分成多个部分，并储存在列表中。
#     num_words = len(words)
#     print('this file has about ' + str(num_words) + ' words')

# # 使用多个文件
# def count_words(filename):
#     try:
#         with open(filename) as fileobject:
#             contents = fileobject.read()
#     except FileNotFoundError:
#         pass                                                                                # pass语句，可在pass后将错误信息写入日志，不用输出到控制台。
#         print(filename + ' --This file is not exit ,Please check!!!!')
#     else:
#         words = contents.split()
#         print(filename + ' --This file has about ' + str(len(words)) + ' words')
# filenames = [r'test_file\day_note.txt',r'test_file\day_note_2.txt','pai.txt','gg.txt']
#
# for filename in filenames:
#     count_words(filename)


# ------------------------------------------------练习--------------------------------------------
# # 1.10.6.提示用户提供数值输入,而不是输入文本
# isquit = True
# while isquit:
#     try:
#         num_1 = input('please input the first number : ')
#         num_2 = input('please input the second number : ')
#         value = float(num_1) + float(num_2)
#     except ValueError:
#         print('Please check you number ,and , input the real number !! NOT TXT!!!!!')
#     else:
#         isquit = False
#         print('the sum is ' + str(value))

# # 2.10.8.读取文件
# def readFile(filename):
#     try:
#         with open(filename,encoding = 'utf-8') as fileobject:
#             contents = fileobject.read()
#     except FileNotFoundError:
#         pass
#         print(filename + ' this file not exit,Please check the file!!!!!!!')
#     else:
#         print(contents)
#
# file_1 = r'test_file\cat.txt'
# file_2 = r'test_file\dog.txt'
# readFile(file_1)
# readFile(file_2)
#
# # 3.10.10.文件中词语的计数
# def count_file(filename):
#     try:
#         with open(filename,encoding = 'utf-8') as fileobject:
#             contents = fileobject.read()
#     except FileNotFoundError:
#         pass
#     else:
#         if filename[-7:-4] == 'cat':
#             print('this file has ' + str(contents.count('猫')) + ' counts ')
#         if filename[-7:-4] == 'dog':
#             print('this file has ' + str(contents.count('狗')) + ' counts ')
#
# count_file(file_1)
# count_file(file_2)

# -------------------------------------------------存储数据----------------------------------------------
# import json
# list = ['fxc','fxz',7758,'吼吼吼吼']
# dic = {'name':'fxc','age':20,'sex':'male'}
# filename = r'test_file\imformation.json'
# with open(filename,'w',encoding = 'utf-8') as fileobject:
#     # json.dump(list,fileobject,ensure_ascii = False)                                       # json.dump()将数据存储到文件中。
#     json.dump(dic,fileobject)
#
# with open(filename,'r',encoding = 'utf-8') as fileobject_read:                              # json.load()读取文本中的信息。
#     contents = json.load(fileobject_read)                                                   # 这步报错，报错原因:json标准只允许一个顶级值（json中所有的数据都在一个数据结构中存储，不能出现多个数据结构）
#     contents_1 = fileobject_read.read()
#     print(type(contents))                                                                   # 输出结果：<class 'list'>，输出结果：<class 'dict'>
# print(contents)
# print(contents_1)

# username = input('Please input you name ')
# filename = r'test_file\username.json'
# with open(filename,'w') as file_object:
#     json.dump(username,file_object)
#     print('we will remenber you when you back ,' + username + '!!')
#
# with open(filename) as f_obj:
#     contents = json.load(f_obj)
#     # print(type(contents))                                                                   # 输出结果：<class 'str'>
#     print('welcome back ' + contents)

# # 改用try-except写法
# try:
#     with open(filename) as f_obj:
#         contents = json.load(f_obj)
# except FileNotFoundError:
#     username = input('Please input you name ')
#     with open(filename,'w') as f_obj_2:
#         json.dump(username,f_obj_2)
#         print('we will remenber you when you back ,' + username + '!!')
# else:
#     print('welcome back, ' + contents)

# # ----------------------------------------------练习--------------------------------------
# # 1.10.12.储存数字
# filename = r'test_file\username.json'
# try:
#     num_1 = input('Please input you favorite number : ')
#     value = float(num_1)
# except ValueError:
#     print('Please input a corrent nummber!!!')
# else:
#     with open(filename,'w') as f_obj:
#         json.dump(num_1,f_obj)
#     try:
#         with open(filename, 'r') as f_obj_2:
#             contents = json.load(f_obj_2)
#     except FileNotFoundError:
#         print('Please check the file name!!!')
#     else:
#         print('we remenber you favorite number is :' + str(contents))

# ------------------------------------------------测试代码---------------------------------------------
# 测试函数
def get_formatted_name(first,last,middle = ''):
    if middle:
        full_name = first + ' ' + middle + ' '+ last
    else:
        full_name = first + ' ' + last
    return full_name.title()