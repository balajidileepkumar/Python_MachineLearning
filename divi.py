from nsetools import Nse
from pprint import pprint
from datetime import datetime
import pandas as pd
import re
import os, sys
import csv
start_time = datetime.now()
nse = Nse()
FileName = "Stocks.csv"
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)
print(os.getcwd())
print(os.path.abspath(FileName))

if(os.path.exists(FileName)):
    DF_Stocks = pd.read_csv(FileName)
    DF_Stocks.describe()
    print(DF_Stocks.head(5))
    Column_Symbol = DF_Stocks.SYMBOL
    i = 0
    All_Divs = []
    for x in Column_Symbol:
        i=i+1
        try:
            q = nse.get_quote(x)	
            CurrentDate = datetime.now()
            if(q['exDate'] is not None and q['recordDate'] is not None):
                Record_Date = datetime.strptime(q['recordDate'], "%d-%b-%y")
                ExDividendDate = datetime.strptime(q['exDate'], "%d-%b-%y")
            else: 
                continue
            #Getting Face Value and LTP
            FaceValue = q['faceValue']
            LTP = q['lastPrice']
            #Validating Dividend Dates
            if((ExDividendDate-CurrentDate).days >=0):
                print("###############################################################")
                print("S.No : ", i)
                print("Ex Dividend Days Left: ", (ExDividendDate-CurrentDate).days)
                print("Script :", q["companyName"], "Record Date : ", q['recordDate'], "Ex Dividend Date : ", q['exDate'])
                print("Ex Dividend Date : ", ExDividendDate ,"Record Date : ",Record_Date, "FaceValue : ", FaceValue,"Current Price : ", LTP, "Purpose : ", q["purpose"])
                match = re.search("[\d\.]{1,6}",q["purpose"])
                dividend_yield_amount = 0
                if match:
                    dividend_yield_amount = (float(match[0])/float(LTP))*100  
                else: 
                    dividend_yield_amount = 0
                print("DIVIDEND AMOUNT ", dividend_yield_amount)
                div_data = {"Company Name":q["companyName"],"Symbol":x,"Ex_Div_Date":ExDividendDate ,"Rec_Date":Record_Date, "FaceValue":FaceValue, "CMP":LTP, "Div":q["purpose"], "Div_Percent": dividend_yield_amount}
                All_Divs.append(div_data)
                pprint(q)
        except Exception as x: 
            print("Error : ", x)
            #pprint(q)
            continue   
    print("\n\n ###############################################################")
    print(All_Divs)
    keys = All_Divs[0].keys()
    OutFile= 'dividends_'+datetime.now().strftime("%M_%H_%d-%m-%y")+".csv"
    with open(OutFile, 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(All_Divs)
    print("File Generated : ", OutFile)
else:
    print("File Not exists")
end_time = datetime.now()
print("Total Duration : ", ((end_time-start_time).seconds)/60)