from utils import db_read, db_write
import datetime

def checkjoin(userId):
    data = db_read("""SELECT `accno` FROM joinaccounts WHERE `user_id` = %s""",(userId,))
    # print(data)
    if data:
        return True
    return False

def loginaccount(userId,regdata):
    # data1 = db_read("""SELECT accno FROM accountdet WHERE accno = %s AND name = %s AND nic = %s""",(regdata['number'], regdata['name'], regdata['nic']))
    data1 = db_read("""SELECT accno FROM accountdet WHERE accno = %s AND nic = %s""",(regdata['number'], regdata['nic']))
    if data1:
        data2 = db_write("""INSERT into joinaccounts (user_id, accno) VALUES (%s, %s)""",(userId,regdata['number']))
        if data2:
            return True, "Now, you jave joined with your bank account!\nEnjoy our service..", 0
        return False, "Error has occured with the Banking server. Sorry about that!", 1
    return False, "Some details may be invalid. Please re-enter Holding account number !", 2

def getname(userId):
    data = db_read("""SELECT `name` FROM accountdet NATURAL JOIN joinaccounts WHERE `user_id` = %s""", (userId,))
    # print(data[0]['name'])
    return data[0]['name']

def getpersonal(userId):
    data = db_read("""SELECT `first_name`, `email`, `name`, `accno`, `nic`, `branch` FROM users NATURAL JOIN joinaccounts JOIN accountdet USING (`accno`) WHERE `user_id` = %s""", (userId,))
    # print(data[0])
    return data[0]
    
def getAccBalance(userId):
    data = db_read("""SELECT `balance` FROM transactions NATURAL JOIN accountdet JOIN joinaccounts USING (`accno`) JOIN users USING (`user_id`) WHERE `user_id` = %s ORDER BY `date` DESC LIMIT 1""", (userId,))
    # print(data[0]['balance'])
    return data[0]['balance']
    
def getTransactions(userId):
    data = db_read("""SELECT `description`, `debit`, `credit`, `balance`, `date` FROM transactions NATURAL JOIN accountdet JOIN joinaccounts USING (`accno`) JOIN users USING (`user_id`) WHERE `user_id` = %s ORDER BY `date` ASC LIMIT 10""", (userId,))
    # print(data)
    return data

def dotransfer(userId, transdet):
    data1 = db_read("""SELECT `balance` FROM accountdet NATURAL JOIN transactions WHERE accno = %s AND name = %s ORDER BY `date` DESC LIMIT 1""", (transdet['number'], transdet['name'])) 
    if data1:
        benefBalance = data1[0]['balance']
        senderdet = getpersonal(userId)
        data2 = db_write("""INSERT INTO transactions (`accno`, `description`, `debit`, `balance`) VALUES (%s, %s, %s, %s)""", (transdet['number'], "transfered from "+ senderdet['name'], transdet['amount'], (transdet['amount'] + benefBalance) ) )
        if data2:
            data3 = db_write ("""INSERT INTO transactions (`accno`, `description`, `credit`, `balance`) VALUES (%s, %s, %s, %s)""", (senderdet['accno'], "transfered to "+transdet['name'], transdet['amount'], getAccBalance(userId) - transdet['amount'] ) )
            if data3:
                    return True, "Congratulations! Money transfer is completed to "+ str(transdet['number'])+ " account by Rs."+ str(transdet['amount']), 0
            return False, "Error has occured with the Banking server. Sorry about that!", 1
        return False, "Error has occured with the Banking server. Sorry about that!", 1
    return False, "There is no bank account for entered account number and name. Please re-enter the beneficiary's account number", 2

def dopayment(userId,paydata):
    data1 = db_read("""SELECT nic FROM consumers WHERE name = %s AND address = %s""", (paydata['name'],paydata['address']))
    if data1:
        data2 = db_read("""SELECT accno FROM fields WHERE fieldname = %s""", (paydata['field'],))
        if data2 and str(data2[0]['accno']) == str(paydata['number']):
            # print(data1)
            consumernic = data1[0]['nic']
            fieldaccno = data2[0]['accno']
            # print(consumernic, fieldaccno)

            data3 = db_read("""SELECT `balance` FROM billpaymenttransactions WHERE `accno` = %s AND nic = %s ORDER BY `date` DESC LIMIT 1""", (fieldaccno, consumernic))
            if data3:
                billbalance = data3[0]['balance']

                data4 = db_write("""INSERT INTO billpaymenttransactions (`accno`, `nic`, `credit`, `balance`) VALUES (%s, %s, %s, %s)""", ( fieldaccno, consumernic, paydata['amount'], billbalance - paydata['amount'] ))
                if data4:
                    dealer = getpersonal(userId)
                    data5 = db_write("""INSERT INTO transactions (`accno`, `description`, `credit`, `balance`) VALUES (%s, %s, %s, %s)""", (dealer['accno'], (paydata['name']+"'s " + paydata['field'] + "bill paid ") , paydata['amount'], getAccBalance(userId) - paydata['amount'] ))
                    if data5:
                        return True, "Congratulations! "+paydata['field']+" Bill payment is completed to "+ str(fieldaccno)+ " account by Rs."+ str(paydata['amount']), 0
                    return False, "Error has occured with the Banking server. Sorry about that!", 1
                return False, "Error has occured with the Banking server. Sorry about that!", 1
            return False, "Seems like "+paydata['name']+" does not have balance to be pay", 2
        return False, "There is a no such field registerd in our service. Please enter the field name", 3
    return False, "There is a no such name or address in our service. Please enter the name ", 4

def reportcomplain(complaindet):
    data1 = db_read("""SELECT `id` FROM branches WHERE `branchname` = %s""", (complaindet['branch'],))
    if data1:
        brID = data1[0]['id']
        type = complaindet['type']
        data2 = False

        if type == 'complain_behaviour':
            data2 = db_write("""INSERT INTO banking_complaints (`brid`, `complain_behaviour`) VALUES (%s, %s)""", (brID, complaindet['description']))
        elif type == 'complain_management':
            data2 = db_write("""INSERT INTO banking_complaints (`brid`, `complain_management`) VALUES (%s, %s)""", (brID, complaindet['description']))
        elif type == 'complain_facility':
            data2 = db_write("""INSERT INTO banking_complaints (`brid`, `complain_facility`) VALUES (%s, %s)""", (brID, complaindet['description']))
        else:
            data2 = db_write("""INSERT INTO banking_complaints (`brid`, `complain_wasting`) VALUES (%s, %s)""", (brID, complaindet['description']))

        if data2:
            return True, "Sorry for the inconvenience !.We'll report the complaint", 0
        return False, "Error has occured with the Banking server. Sorry about that!", 1
    return False, "There is a no such branch in our service. Please enter the branch name", 2

# print(getTransactions(3))
# print(getpersonal('1'))
# print(dopayment(1,{'model': 'payment', 'field': 'Electricity', 'number': 11111, 'name': "K.W.Saranga", 'address': '170/A, dobagahawatta, norway', 'amount': 200.0, 'code': 182172}))
# print(reportcomplain({'model':'complain', 'type':'complain_wasting', 'branch':'galle', 'description':'billing counter accountant is not familiar with people'}))
# print(dotransfer(1,{'model': 'transfer', 'number': 456123789, 'name': 'Jorge Washinton', 'amount': 500.0, 'code': 431435}))
# print(loginaccount(5,{'number':'895623125','name':'S.C.Dhavinchi','nic':'5588124722V'}))
# print(checkjoin('6 or 1=1'))
# print(getAccBalance(2))
# print(getname("sadakan OR 1=1"))