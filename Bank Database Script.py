class Banking:
    def __init__(self):
        self.data = {'Account Number':[],
                   'Name':[],
                   'last_name':[],
                   'contact':[],
                   'Father Name':[], 
                   'Mother Name':[],
                   'Pincode':[],
                   'Aadhar Number':[],
                   'Amount':[]
                  }
        self.menu() 
        
    def menu(self): 
        while True:
            print('Press 1 to Create Account')
            print('Press 2 for Deposit The Amount')
            print('Press 3 to Withdrawl the Amount')
            print('Press 4 to Check Your Account Details')
            print('Press 5 to Exit The System')
            
            b=int(input('Enter Your Choice'))
            
            if b==1:
                self.account()
            elif b==2:
                self.deposit()
            elif b==3:
                self.withdrawl()
            elif b==4:
                self.check()
            elif b==5: 
                print('Exiting The Syetem, Thank You!')
                break
            else:
                print('Invalid Input')
        

    def account(a):
        acc_number=int(input('Enter the Account Number'))
        a.data['Account Number'].append(acc_number)
        print(a.data)
        
        cust_name=input('Enter Your First Name').title()
        a.data['Name'].append(cust_name)
        print(a.data)

        last=input('Enter Your Last Name').title()
        a.data['last_name'].append(last)
        print(a.data)
        
        father=input("Enter Your Father's Name").title()
        a.data['Father Name'].append(father)
        print(a.data)
        
        mother=input("Enter Your Mother's Name").title()
        a.data['Mother Name'].append(mother)
        print(a.data)

        def phone(): 
            ph=input('Enter Your 10 Digit Phone Number')
            if len(ph)==10:
                a.data['contact'].append(ph)
                print(a.data)
            else: 
                print('Please Enter Your 10 Digit Phone Number')
                
                phone()

        phone()

        
        def pin(): 
            pincode=int(input('Enter Your 6 Digit Area Pincode'))
            if len(str(pincode))==6:
                a.data['Pincode'].append(pincode)
                print(a.data)
            else:
                print('Wrong Pincode')
                pin()
        pin()
        
        def aadhar(): 
            aadhar_number=int(input('Enter Your 12 Digit Aadhar Number'))
            if len(str(aadhar_number))==12:
                a.data['Aadhar Number'].append(aadhar_number)
                print(a.data)
            else:
                print('Invalid Aadhar Number! Please Enter Your 12 Digit Aadhar Number')
                aadhar()
        aadhar() 
        
    
    def deposit(se):
        dp=int(input('Enter the Account Number to Deposit the Amount '))
        if dp in se.data['Account Number']:
            z=se.data['Account Number'].index(dp)
            
            amt=int(input('Enter The Amount You Want to Deposit'))
            se.data['Amount'].append(amt)
            print('You have Successfully Deposit the Amount',se.data['Amount'][z])
        
        else:
            print('Account No. Does Not Exist')
            
        
    def withdrawl(sel):
        ac=int(input('Enter The Account Number to Withdrawl'))
        if ac in sel.data['Account Number']:
            
            index_number=sel.data['Account Number'].index(ac)
            cash_amount=int(input('Enter The Amount You Want To Withdrawal'))
            
            # Check for sufficient balance before withdrawal
            if cash_amount <= sel.data['Amount'][index_number]:
                sel.data['Amount'][index_number] -= cash_amount
                print('You Have Successfully Withdrawn.', cash_amount,'Your Remaining Balance is', sel.data['Amount'][index_number])
            else:
                print('Insufficient Balance. Please enter a lower amount.')

        else:
            print('Account Does Not Exist')
       
            
    def check(c):
        x=int(input('Enter the Account Number to Check the Balance'))
        if x in c.data['Account Number']:
            ind=c.data['Account Number'].index(x)
            
            print('Account Number:',c.data['Account Number'][ind])
            print('First Name:',c.data['Name'][ind])
            print('Last Name:',c.data['last_name'][ind])
            print('Contact:',c.data['contact'][ind])
            print('Father Name:',c.data['Father Name'][ind])
            print('Mother Name:',c.data['Mother Name'][ind])
            print('Pincode',c.data['Pincode'][ind])
            print('Aadhar Number:',c.data['Aadhar Number'][ind])
            print('Account Balance',c.data['Amount'][ind])
    

        else:
            print('Account Does Not Exist')
            

y=Banking()