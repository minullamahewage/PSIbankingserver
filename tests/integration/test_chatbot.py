import sys
from unittest import TestCase
sys.path.append('./')
import Bankingchatbot


class TestBankingChatbot(TestCase):

    def test_response(self): 
        self.assertIn(Bankingchatbot.response('hi',1),["Hello", "Good to see you", "Hi there, how can I help?"])
        self.assertIn(Bankingchatbot.response('hi there',1),["Hello", "Good to see you", "Hi there, how can I help?"])
        self.assertNotIn(Bankingchatbot.response('how are you',1),["Hello", "Good to see you", "Hi there, how can I help?"])
        self.assertNotIn(Bankingchatbot.response("I agree",1),["Hello", "Good to see you", "Hi there, how can I help?"])

        self.assertIn(Bankingchatbot.response('by bye',1),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])
        self.assertIn(Bankingchatbot.response('see you soon',1),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])
        self.assertNotIn(Bankingchatbot.response('hi',1),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])
        self.assertNotIn(Bankingchatbot.response('call to bank',1),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])

        self.assertIn(Bankingchatbot.response('thanks',1),["Happy to help!", "Any time!", "Thank you!"])
        self.assertIn(Bankingchatbot.response('thank you very much',1),["Happy to help!", "Any time!", "Thank you!"])
        self.assertNotIn(Bankingchatbot.response('adfadfa',1),["Happy to help!", "Any time!", "Thank you!"])
        self.assertNotIn(Bankingchatbot.response('what you can do',1),["Happy to help!", "Any time!", "Thank you!"])

        self.assertEqual(Bankingchatbot.response("actually I don't know",1),"that's fine !")
        self.assertEqual(Bankingchatbot.response('no,absolutely not',1),"that's fine !")
        self.assertNotEqual(Bankingchatbot.response("thank you",1),"that's fine !")
        self.assertNotEqual(Bankingchatbot.response("I hate you",1),"that's fine !")

        self.assertEqual(Bankingchatbot.response('okay',1),"Is there anything to help with ?")
        self.assertEqual(Bankingchatbot.response("it is fine",1),"Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.response('ooookaaay',1),"Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.response("how are you",1),"Is there anything to help with ?")

        self.assertIn(Bankingchatbot.response('accept',1),["let's move forward", "we can carry on..","you are right! Lets continue.."])
        self.assertIn(Bankingchatbot.response('I agree',1),["let's move forward", "we can carry on..","you are right! Lets continue.."])
        self.assertNotIn(Bankingchatbot.response('i want to dance',1),["let's move forward", "we can carry on..","you are right! Lets continue.."])
        self.assertNotIn(Bankingchatbot.response('no thanks',1),["let's move forward", "we can carry on..","you are right! Lets continue.."])

        self.assertEqual(Bankingchatbot.response('just stop it',1),"okay! Is there anything to help with ?")
        self.assertEqual(Bankingchatbot.response("i'm quit",1),"okay! Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.response('asdfadf',1),"okay! Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.response('hi there',1),"okay! Is there anything to help with ?")

        self.assertIn(Bankingchatbot.response('I want to do a job soon',1),["Sorry, can't understand you", "Not sure I understand"])
        self.assertIn(Bankingchatbot.response('asdfdafdf',1),["Sorry, can't understand you", "Not sure I understand"])
        self.assertNotIn(Bankingchatbot.response('what you can do',1),["Sorry, can't understand you", "Not sure I understand"])
        self.assertNotIn(Bankingchatbot.response('thanks',1),["Sorry, can't understand you", "Not sure I understand"])
       
        self.assertIn(Bankingchatbot.response('what are the options you have',1),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])
        self.assertIn(Bankingchatbot.response('What you can do',1),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])
        self.assertNotIn(Bankingchatbot.response('what is my account number',1),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])
        self.assertNotIn(Bankingchatbot.response('what is my name',1),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])

    def test_get_response(self):
        self.assertIn(Bankingchatbot.get_response('greeting'),["Hello", "Good to see you", "Hi there, how can I help?"])
        self.assertNotIn(Bankingchatbot.get_response('options'),["Hello", "Good to see you", "Hi there, how can I help?"])
        self.assertNotIn(Bankingchatbot.get_response("history"),["Hello", "Good to see you", "Hi there, how can I help?"])

        self.assertIn(Bankingchatbot.get_response('goodbye'),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])
        self.assertNotIn(Bankingchatbot.get_response('complain_wasting'),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])
        self.assertNotIn(Bankingchatbot.get_response('name'),["See you!", "Have a nice day", "Bye! Come back again soon.","Great chatting with you"])

        self.assertIn(Bankingchatbot.get_response('thanks'),["Happy to help!", "Any time!", "Thank you!"])
        self.assertNotIn(Bankingchatbot.get_response('account'),["Happy to help!", "Any time!", "Thank you!"])
        self.assertNotIn(Bankingchatbot.get_response('payment'),["Happy to help!", "Any time!", "Thank you!"])

        self.assertEqual(Bankingchatbot.get_response("no"),"that's fine !")
        self.assertNotEqual(Bankingchatbot.get_response("complain_management"),"that's fine !")
        self.assertNotEqual(Bankingchatbot.get_response("okay"),"that's fine !")

        self.assertEqual(Bankingchatbot.get_response('okay'),"Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.get_response('complain_facility',),"Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.get_response("personal"),"Is there anything to help with ?")

        self.assertIn(Bankingchatbot.get_response('select'),["let's move forward", "we can carry on..","you are right! Lets continue.."])
        self.assertNotIn(Bankingchatbot.get_response('account'),["let's move forward", "we can carry on..","you are right! Lets continue.."])
        self.assertNotIn(Bankingchatbot.get_response('complain_management'),["let's move forward", "we can carry on..","you are right! Lets continue.."])

        self.assertEqual(Bankingchatbot.get_response('quit'),"okay! Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.get_response('history'),"okay! Is there anything to help with ?")
        self.assertNotEqual(Bankingchatbot.get_response('personal'),"okay! Is there anything to help with ?")

        self.assertIn(Bankingchatbot.get_response('noanswer'),["Sorry, can't understand you", "Not sure I understand"])
        self.assertNotIn(Bankingchatbot.get_response('okay'),["Sorry, can't understand you", "Not sure I understand"])
        self.assertNotIn(Bankingchatbot.get_response('payment'),["Sorry, can't understand you", "Not sure I understand"])
       
        self.assertIn(Bankingchatbot.get_response('options'),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])
        self.assertNotIn(Bankingchatbot.get_response('account'),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])
        self.assertNotIn(Bankingchatbot.get_response('complain_facility'),["I can guide you to do money transferring, online bill payments, show your account details as well as report a complaint", "Offering support for do money transferring, online bill payments, show your account details as well as report a complaint"])

        self.assertEqual(Bankingchatbot.get_response('history'),"No problem, here is your account transaction history\n")
        self.assertNotEqual(Bankingchatbot.get_response('complain_wasting'),"No problem, here is your account transaction history\n")
        self.assertNotEqual(Bankingchatbot.get_response('goodbye'),"No problem, here is your account transaction history\n")

        self.assertIn(Bankingchatbot.get_response('balance'),["Sure, Total account asset is ","Total available balance is "])
        self.assertNotIn(Bankingchatbot.get_response('okay'),["Sure, Total account asset is ","Total available balance is "])
        self.assertNotIn(Bankingchatbot.get_response('greeting'),["Sure, Total account asset is ","Total available balance is "])

        self.assertIn(Bankingchatbot.get_response('personal'),["Here's your profile..", "Okay, Sure\n"])
        self.assertNotIn(Bankingchatbot.get_response('complain_management'),["Here's your profile..", "Okay, Sure\n"])
        self.assertNotIn(Bankingchatbot.get_response('account'),["Here's your profile..", "Okay, Sure\n"])

        self.assertEqual(Bankingchatbot.get_response('transfer'),"So, Let me guide you the money transferring to be easier")
        self.assertNotEqual(Bankingchatbot.get_response('history'),"So, Let me guide you the money transferring to be easier")
        self.assertNotEqual(Bankingchatbot.get_response('personal'),"So, Let me guide you the money transferring to be easier")

        self.assertEqual(Bankingchatbot.get_response("payment"),"Okay, Let me guide you for your bill payment to be easier..\nChoose the biller catagory\n1. Electricity\n3. Insuarance\n4. Telephone\n5. Television\n6. Water")
        self.assertNotEqual(Bankingchatbot.get_response("complain_management"),"Okay, Let me guide you for your bill payment to be easier..\nChoose the biller catagory\n1. Electricity\n3. Insuarance\n4. Telephone\n5. Television\n6. Water")
        self.assertNotEqual(Bankingchatbot.get_response("noanswer"),"Okay, Let me guide you for your bill payment to be easier..\nChoose the biller catagory\n1. Electricity\n3. Insuarance\n4. Telephone\n5. Television\n6. Water")

        self.assertEqual(Bankingchatbot.get_response("complain_behaviour"),"okay !.Which branch do you want to complain ?")
        self.assertEqual(Bankingchatbot.get_response("complain_management"),"okay !.Which branch do you want to complain ?")
        self.assertEqual(Bankingchatbot.get_response("complain_facility"),"okay !.Which branch do you want to complain ?")
        self.assertEqual(Bankingchatbot.get_response("complain_wasting"),"okay !.Which branch do you want to complain ?")
        self.assertNotEqual(Bankingchatbot.get_response("payment"),"okay !.Which branch do you want to complain ?")
        self.assertNotEqual(Bankingchatbot.get_response("options"),"okay !.Which branch do you want to complain ?")

    def test_get_results(self):
        self.assertEqual(Bankingchatbot.get_results('hi there')[0][0],'greeting')
        self.assertEqual(Bankingchatbot.get_results('hi')[0][0],'greeting')
        self.assertNotEqual(Bankingchatbot.get_results('how are you')[0][0],'greeting')
        self.assertNotEqual(Bankingchatbot.get_results("I agree")[0][0],'greeting')

        self.assertEqual(Bankingchatbot.get_results('by bye')[0][0],'goodbye')
        self.assertEqual(Bankingchatbot.get_results('see you soon')[0][0],'goodbye')
        self.assertNotEqual(Bankingchatbot.get_results('hi')[0][0],'goodbye')
        self.assertNotEqual(Bankingchatbot.get_results('call to bank')[0][0],'goodbye')

        self.assertEqual(Bankingchatbot.get_results('thanks')[0][0],'thanks')
        self.assertEqual(Bankingchatbot.get_results('thank you very much')[0][0],'thanks')
        self.assertNotEqual(Bankingchatbot.get_results('adfadfa')[0][0],'thanks')
        self.assertNotEqual(Bankingchatbot.get_results('what you can do')[0][0],'thanks')

        self.assertEqual(Bankingchatbot.get_results("actually I don't know")[0][0],'no')
        self.assertEqual(Bankingchatbot.get_results('no,absolutely not')[0][0],'no')
        self.assertNotEqual(Bankingchatbot.get_results('thank you')[0][0],'no')
        self.assertNotEqual(Bankingchatbot.get_results("I hate you")[0][0],'no')

        self.assertEqual(Bankingchatbot.get_results('okay')[0][0],'okay')
        self.assertEqual(Bankingchatbot.get_results("it is fine")[0][0],'okay')
        self.assertNotEqual(Bankingchatbot.get_results('ooookaaay')[0][0],'okay')
        self.assertNotEqual(Bankingchatbot.get_results("how are you")[0][0],'okay')

        self.assertEqual(Bankingchatbot.get_results('accept')[0][0],'select')
        self.assertEqual(Bankingchatbot.get_results('I agree')[0][0],'select')
        self.assertNotEqual(Bankingchatbot.get_results('i want to dance')[0][0],'select')
        self.assertNotEqual(Bankingchatbot.get_results('no thanks')[0][0],'select')

        self.assertEqual(Bankingchatbot.get_results('just stop it')[0][0],'quit')
        self.assertEqual(Bankingchatbot.get_results("i'm quit")[0][0],'quit')
        self.assertNotEqual(Bankingchatbot.get_results('asdfadf')[0][0],'quit')
        self.assertNotEqual(Bankingchatbot.get_results('hi there')[0][0],'quit')

        self.assertEqual(Bankingchatbot.get_results('I want to do a job soon')[0][0],'noanswer')
        self.assertEqual(Bankingchatbot.get_results('asdfdafdf')[0][0],'noanswer')
        self.assertNotEqual(Bankingchatbot.get_results('what you can do')[0][0],'noanswer')
        self.assertNotEqual(Bankingchatbot.get_results('thanks')[0][0],'noanswer')

        self.assertEqual(Bankingchatbot.get_results('what are the options you have')[0][0],'options')
        self.assertEqual(Bankingchatbot.get_results('What you can do')[0][0],'options')
        self.assertNotEqual(Bankingchatbot.get_results('what is my account number')[0][0],'options')
        self.assertNotEqual(Bankingchatbot.get_results('what is my name')[0][0],'options')

        self.assertEqual(Bankingchatbot.get_results('I want to know account transaction history')[0][0],'history')
        self.assertEqual(Bankingchatbot.get_results('show transaction details')[0][0],'history')
        self.assertNotEqual(Bankingchatbot.get_results('want to make a complain about agents behaviour')[0][0],'history')
        self.assertNotEqual(Bankingchatbot.get_results('i accept it')[0][0],'history')

        self.assertEqual(Bankingchatbot.get_results('show account balance')[0][0],'balance')
        self.assertEqual(Bankingchatbot.get_results('show updates about account asserts')[0][0],'balance')
        self.assertNotEqual(Bankingchatbot.get_results('see you again')[0][0],'balance')
        self.assertNotEqual(Bankingchatbot.get_results('show my transaction history')[0][0],'balance')

        self.assertEqual(Bankingchatbot.get_results('show personal information')[0][0],'personal')
        self.assertEqual(Bankingchatbot.get_results('view profile')[0][0],'personal')
        self.assertNotEqual(Bankingchatbot.get_results('hi')[0][0],'personal')
        self.assertNotEqual(Bankingchatbot.get_results('adfdg')[0][0],'personal')

        self.assertEqual(Bankingchatbot.get_results('what is my username')[0][0],'name')
        self.assertEqual(Bankingchatbot.get_results('my name')[0][0],'name')
        self.assertNotEqual(Bankingchatbot.get_results('account balance')[0][0],'name')
        self.assertNotEqual(Bankingchatbot.get_results('complain about time wasting')[0][0],'name')

        self.assertEqual(Bankingchatbot.get_results('show my account number')[0][0],'account')
        self.assertEqual(Bankingchatbot.get_results('what is my account number')[0][0],'account')
        self.assertNotEqual(Bankingchatbot.get_results('bye')[0][0],'account')
        self.assertNotEqual(Bankingchatbot.get_results('what can you do')[0][0],'account')

        self.assertEqual(Bankingchatbot.get_results('want to do money transfer')[0][0],'transfer')
        self.assertEqual(Bankingchatbot.get_results('share money with a friend')[0][0],'transfer')
        self.assertNotEqual(Bankingchatbot.get_results('account balance')[0][0],'transfer')
        self.assertNotEqual(Bankingchatbot.get_results('daadf')[0][0],'transfer')

        self.assertEqual(Bankingchatbot.get_results('pay a bill')[0][0],'payment')
        self.assertEqual(Bankingchatbot.get_results('i have a bill to pay')[0][0],'payment')
        self.assertNotEqual(Bankingchatbot.get_results('share money with a friend')[0][0],'payment')
        self.assertNotEqual(Bankingchatbot.get_results('I agree')[0][0],'payment')

        self.assertEqual(Bankingchatbot.get_results('comlain for behaviour about service providers')[0][0],'complain_behaviour')
        self.assertEqual(Bankingchatbot.get_results('complain about account management')[0][0],'complain_management')
        self.assertEqual(Bankingchatbot.get_results('complain about low facility')[0][0],'complain_facility')
        self.assertEqual(Bankingchatbot.get_results('report for wasting time')[0][0],'complain_wasting')
        self.assertNotEqual(Bankingchatbot.get_results('hi')[0][0],'complain_behaviour')
        self.assertNotEqual(Bankingchatbot.get_results('find a job')[0][0],'complain_management')
        self.assertNotEqual(Bankingchatbot.get_results('how can i login to the system')[0][0],'complain_facility')
        self.assertNotEqual(Bankingchatbot.get_results('dagadgg')[0][0],'complain_wasting')
