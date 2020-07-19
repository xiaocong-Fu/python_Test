# -----------------------------------测试代码-------------------------------------
import unittest
# from Grammar import get_formatted_name
# class NameTestCase(unittest.TestCase):
#     '''测试Grammar.get_formatted_name'''
#     def test_first_last_name(self):
#         '''能够处理janis Joplin的姓名'''
#         formatted_name = get_formatted_name('janis','joplin')
#         self.assertEqual(formatted_name,'Janis Joplin')                             # 断言方法：用来核实得到的结果与期望的结果一致
#
#     def test_first_last_middle_name(self):
#         '''能够正确的处理wolfgang amadeus mozart的姓名'''
#         formatted_name = get_formatted_name('wolfgang','amadeus','mozart')
#         self.assertEqual(formatted_name,'Wolfgang Mozart Amadeus')
#
# unittest.main()



# -------------------------------------各种断言方法-----------------------------------
# 方法1：assertEqual(a,b)                  核实a==b
# 方法2：assertNotEqual(a,b)               核实a!=b
# 方法3：assertTrue(x)                     核实x为True
# 方法4：assertFalse(x)                    核实x为False
# 方法5：assertIn(item,list)               核实item在list中
# 方法6：assertNotIn(item,list)            核实item不在list中


# -----------------------------测试survey.py中的AnonymousSurvey类--------------------------------
from class_base.survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):                                                                # unittest.TestCase类包含方法setUp(),只需创建对象一次
        '''创建一个调查对象和一组答案，供测试方法使用'''
        question = 'What language did you first learn to speak ?'
        self.my_survey = AnonymousSurvey(question)                                  # 储存两样东西的变量名包含前缀self
        self.responses = ['English', '西班牙语', 'Chinese', '日本话']

    '''针对AnonymousSurvey类的测试'''
    def test_store_single_respense(self):
        '''单个输入测试'''
        # question = 'What language did you first learn to speak ?'
        # my_survey = AnonymousSurvey(question)
        self.my_survey.store_response(self.responses[0])
        self.assertIn('English',self.my_survey.responses)

    def test_store_three_respense(self):
        '''多个输入测试'''
        # question = 'What language did you first learn to speak ?'
        # my_survey = AnonymousSurvey(question)
        # responses = ['English','西班牙语','Chinese','日本话']
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

unittest.main()