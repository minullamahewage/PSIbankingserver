import sys
sys.path.append('./')

import unittest
import package_management

class TestPackageManagement(unittest.TestCase):

    def test_checkjoin(self):
        self.assertTrue(package_management.checkjoin(1)) #userid = 1 already exist in database
        self.assertTrue(package_management.checkjoin('1')) #userid = 1 already exist in database
        self.assertTrue(package_management.checkjoin(3))  #userid = 3 already exist in database
        self.assertFalse(package_management.checkjoin(7))  #userid = 7 doesn't exist in database
    
    def test_loginaccount(self):
        self.assertEqual(package_management.loginaccount(4,{'number':'895623124','name':'S.C.Dhavinchi','nic':'5588124722V'})[1],"Some details may be invalid. Please re-enter Holding account number !") #number is wrong
        self.assertEqual(package_management.loginaccount(4,{'number':'8956231245','name':'S.C.Dhavinchi','nic':'558812472'})[1],"Some details may be invalid. Please re-enter Holding account number !") #nic is wrong

    def test_getname(self):
        self.assertEqual(package_management.getname(1),"K.G.Siriwardhana")
        self.assertEqual(package_management.getname(2),"Jorge Washinton")
        self.assertNotEqual(package_management.getname(3),"Jorge Washinton")

    def test_getpersonal(self):
        self.assertEqual(package_management.getpersonal(1),{'first_name': 'Test', 'email': 'test@gmail.com', 'name': 'K.G.Siriwardhana', 'accno': '987654321', 'nic': '784512963V', 'branch': 'Colombo'})
        self.assertEqual(package_management.getpersonal('1'),{'first_name': 'Test', 'email': 'test@gmail.com', 'name': 'K.G.Siriwardhana', 'accno': '987654321', 'nic': '784512963V', 'branch': 'Colombo'})
        self.assertEqual(package_management.getpersonal(3),{'first_name': 'rashmika', 'email': 'rashnanayakkara.17@cse.mrt.ac.lk', 'name': 'N.G.L.R.Lakshan', 'accno': '123456789', 'nic': '364512785V', 'branch': 'Galle'})
        self.assertNotEqual(package_management.getpersonal(3),{'first_name': 'Test', 'email': 'test@gmail.com', 'name': 'K.G.Siriwardhana', 'accno': '987654321', 'nic': '784512963V', 'branch': 'Colombo'})

    def test_dotransfer(self):
        self.assertEqual(package_management.dotransfer(1,{'model': 'transfer', 'number': 121, 'name': 'lklk', 'amount': 500.0, 'code': 431435})[1],"There is no bank account for entered account number and name. Please re-enter the beneficiary's account number") #both number and name are wrong
        self.assertEqual(package_management.dotransfer(1,{'model': 'transfer', 'number': 456123789, 'name': 'lklk', 'amount': 500.0, 'code': 431435})[1],"There is no bank account for entered account number and name. Please re-enter the beneficiary's account number") #name is wrong
        self.assertEqual(package_management.dotransfer(1,{'model': 'transfer', 'number': 4561237, 'name': 'Jorge Washinton', 'amount': 500.0, 'code': 431435})[1],"There is no bank account for entered account number and name. Please re-enter the beneficiary's account number") #number is wrong

    def test_dopayment(self):
        self.assertEqual(package_management.dopayment(1,{'model': 'payment', 'field': 'Electricity', 'number': 11111, 'name': "K.W.Saran", 'address': '170/A, dobagahawatta, norway', 'amount': 200.0, 'code': 182172})[1],"There is a no such name or address in our service. Please enter the name ") #name is wrong
        self.assertEqual(package_management.dopayment(1,{'model': 'payment', 'field': 'Electricity', 'number': 11111, 'name': "K.W.Saranga", 'address': '170/A, dobagahawatta', 'amount': 200.0, 'code': 182172})[1],"There is a no such name or address in our service. Please enter the name ") #address is wrong
        self.assertEqual(package_management.dopayment(1,{'model': 'payment', 'field': 'Electricity', 'number': 11111, 'name': "K.W.Saran", 'address': '170/A, dobagahawatta', 'amount': 200.0, 'code': 182172})[1],"There is a no such name or address in our service. Please enter the name ") #name and address is wrong
        self.assertEqual(package_management.dopayment(1,{'model': 'payment', 'field': 'Elec', 'number': 11111, 'name': "K.W.Saranga", 'address': '170/A, dobagahawatta, norway', 'amount': 200.0, 'code': 182172})[1],"There is a no such field registerd in our service. Please enter the field name") #field is wrong

    def test_reportcomplain(self):
        self.assertEqual(package_management.reportcomplain({'model':'complain', 'type':'complain_wasting', 'branch':'gae', 'description':'billing counter accountant is not familiar with people'})[1],"There is a no such branch in our service. Please enter the branch name") #branch is wrong


if __name__ == '__main__':
    unittest.main()