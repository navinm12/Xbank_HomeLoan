from django.shortcuts import render
from django.http import HttpResponseRedirect
from web3 import Web3

from pyzbar.pyzbar import decode
from PIL import Image

import json
import os


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount=web3.eth.accounts[0] 


abi=json.loads('[{"constant":true,"inputs":[],"name":"civiladvisoraccess","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"bankadvisoraccess","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"},{"name":"_message","type":"string"},{"name":"_salary","type":"uint256"},{"name":"_documentid","type":"uint256"},{"name":"_estimation","type":"uint256"}],"name":"Customer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"}],"name":"Civil_advisor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_recipient","type":"address"}],"name":"BankAdvisor","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_bankforestimation","type":"address"}],"name":"mest","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"Bankacess","outputs":[{"name":"","type":"string"},{"name":"","type":"uint256"},{"name":"","type":"bool"},{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_bankaddress","type":"address"}],"name":"documentver","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
address= "0x2b17bC19a8c1Bee860a252F9Ae7034BBE4A53Fde"
contract= web3.eth.contract(address=address, abi=abi)


valuetoview={}

def home(request):
     return render(request,'home.html')


def about(request):
     return render(request,'about.html')


def reset(request):
    return render(request,'index.html')

def adminAccount(request):
    return render(request,'adminaccount.html')


def User(request):
    return render(request,'user.html')

def startEthereum(request):
    return render(request,'homeloan.html')

def successfull(request):
    
    Name= request.session['Name']
    Salary= request.session['Salary']
    Documentid= request.session['Documentid']
    Estimation= request.session['Estimation']
    PanDOB = request.session['PanDOB']
    PanID =  request.session['PanID']
    submitbutton= request.POST.get("Submit")
    Hashid = request.session['Hashid']
    
        

    print(Hashid)
    # print(PanID)
    # print(Name,Salary,Documentid,Estimation,PanDOB,PanID)
    details={'Name':Name,'Salary': Salary, 'Documentid': Documentid, 'Estimation':Estimation,'PanDOB':PanDOB,'PanID':PanID,'Hashid':Hashid,'submitbutton':submitbutton,}
    return render(request,'successfull.html',details)





def homeloan(request):
    verify=[]
    verifys=''
    try:
        submitbutton= request.POST.get("Submit")
        if (request.method == 'POST'):
            Name = request.POST.get('name')
            Salary = request.POST.get('Salary')
            Documentid = request.POST.get('Documentid')
            Estimation = request.POST.get('Estimation')
            DOB = request.POST.get('DOB')
            Pannumber = request.POST.get('Pannumber')

            myFile=request.POST.get('myFile')
            path=os.path.abspath(myFile)

            a=decode(Image.open(path))
            d=a[0].data
          
            f=d.decode('utf-8') 
            # print(f)
            PanDOB = f[96:107]
            PanID =f[120:]
            print(PanDOB,PanID)
            print(DOB,Pannumber)
            # print(PanID)

         

            Salary=int(Salary)
            Documentid=int(Documentid)
            Estimation=int(Estimation)

            request.session['Name'] =  Name
            request.session['Salary'] =  Salary
            request.session['Documentid'] =  Documentid
            request.session['Estimation'] =  Estimation
            request.session['PanDOB'] =  PanDOB
            request.session['PanID'] =  PanID

            # valuetoview={'Name':Name,'Salary':Salary,'Documentid':Documentid,'Estimation':Estimation,}



     
            
            
            def transfer(account_1,account_2,private_key):
                nonce = web3.eth.getTransactionCount(account_1)

                tx = {
                    'nonce': nonce,
                    'to': account_2,
                    'value': web3.toWei(1, 'ether'),
                    'gas': 2000000,
                    'gasPrice': web3.toWei('50', 'gwei'),
                }


                signed_tx = web3.eth.account.signTransaction(tx, private_key)
                tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
                Hashid = web3.toHex(tx_hash)
                request.session['Hashid'] = Hashid
                return(web3.toHex(tx_hash))
        
            

            a=[]
            contract.functions.Customer(web3.eth.accounts[1],Name,Salary,Documentid,Estimation).transact()
            # contract.functions.Customer(web3.eth.accounts[1],Name,123456789,123456789,450000).transact()
            web3.eth.defaultAccount=web3.eth.accounts[1] 
            # print(contract.functions.Bankacess().call())

            # bankadvisortransaction
            web3.eth.defaultAccount=web3.eth.accounts[1] 
            contract.functions.BankAdvisor(web3.eth.accounts[2]).transact()

            # //bankadvisoraccess
            # web3.eth.defaultAccount=web3.eth.accounts[2] 
            # print(contract.functions.bankadvisoraccess().call())


            # //Civiladvisor_transcation
            # web3.eth.defaultAccount=web3.eth.accounts[1] 
            contract.functions.Civil_advisor(web3.eth.accounts[3]).transact()

            # //civiladvisoraccess
            # web3.eth.defaultAccount=web3.eth.accounts[3] 
            # print(contract.functions.civiladvisoraccess().call())

            #documetid_trans
            web3.eth.defaultAccount=web3.eth.accounts[2]
            contract.functions.documentver(web3.eth.accounts[1]).transact()


            #document_verified
            # web3.eth.defaultAccount=web3.eth.accounts[1]


            #civilad
            web3.eth.defaultAccount=web3.eth.accounts[3]
            contract.functions.mest(web3.eth.accounts[1]).transact()

            #civil_verification
            web3.eth.defaultAccount=web3.eth.accounts[1]
            
            a=(contract.functions.Bankacess().call())

            print(a)
        


            account_1=web3.eth.accounts[1]
            account_2=web3.eth.accounts[0]

            privatekeysender="d4ba0fea4f8cbbb4cd8a22d4fdfddb679bd21ed80e1db13484c92bda2ec8ea21"
        


            # ethertransfer
            # and Pannumber == PanID and DOB == PanDOB
            if(a[2]==True and a[3]==True):
                print(transfer(account_1,account_2,privatekeysender))
                b="Your transcation is successful"
                verifys = "Approved"
                c=1
                verify.append(c)


            else:
                print("Your transcation has been denied")
                b="our transcation has been denied"
                verifys = "Your not eligible for Loan"
                c=0
                verify.append(c)
            
            print(verify)
            print(verifys)
            print(b)
    except:
        verifys='Invalid credentials'

# 'PanNumber':PanID,'Date of Birth':PanDOB,
    return render(request,'homeloan.html',{'submitbutton':submitbutton,'verifys':verifys,'verify':verify,})



intarr=[]
emiarr=[]
principlearr=[]
closingbalancearr=[]
openingbalancearr=[]


def emi_calculator(p, r, t):
    r= float(r)
    p=float(p)
    t=float(t)
   
    
    r = r / (12 * 100) # one month interest
    # t = t * 12 # one month period
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    interest=(r)*p
    intarr.append("%.2f" % interest)
    # print( "%.2f" % interest)
    prin = emi - interest
    principlearr.append("%.2f" %prin)
    # print( "%.2f" %prin)
    emiarr.append("%.2f" % emi)
    remaining = p - prin
    openbal = p - emi +interest
    openingbalancearr.append(round(openbal))
    # print(round(openbal))
    closingbalancearr.append(round(remaining))
    # print ("%.2f" % emi)
    
    return (round(remaining))



 


def index(request):
    submitbutton= request.POST.get("Submit")
    context={}
    valid=''
    invalids=''
    months=12
    condition=200000
    months=['1', '2', '3',' 4', '5', '6', '7', '8', '9', '10', '11', '12']
   
    if (request.method == 'POST'):
        # Rows = request.POST.get('row')
        # Column = request.POST.get('col')
        LoanAmount = request.POST.get('loanamt')

        if int(LoanAmount) >= 200000:
            # submitbuttonV =request.POST.get("")
            valid = "valided"
            print(valid ,LoanAmount)
            principal = LoanAmount
            rate = 8
            i=12
            
            # print(openingbalancearr)
            
            while(i>0):
                principal = emi_calculator(principal, rate, i)
                # print("Monthly EMI is= ", principal )
                i=i-1
        
        
        else:
            invalids ='Entered Loan amount is not valid for providing loan'
            print(invalids)
        
        

    
       
      
        # print(Rows)
        # print(Column)
        # print(intarr)
        # print(principlearr)
        # print(closingbalancearr)
        openingbalancearr.insert(0,int(LoanAmount))
        openingbalancearr.pop(12)

        print(openingbalancearr)
        zipped = zip(months,openingbalancearr,emiarr,intarr,principlearr,closingbalancearr)


        context= {'condition':condition,'LoanAmount':LoanAmount,'submitbutton': submitbutton,'valid': valid,'invalids': invalids,'intarr':intarr,'emiarr':emiarr,'principlearr':principlearr,'closingbalancearr':closingbalancearr,'zipped':zipped,}
        
    return render(request,'index.html',context)




