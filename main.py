
import pandas as pd
import datetime
import pywhatkit
if __name__ == "__main__":
    df = pd.read_excel("data.xlsx")
    print(df)
    today = datetime.datetime.now().strftime("%d-%m")
    yearNow = datetime.datetime.now().strftime("%Y")
    # print(today)
    writeInd = []
    i=0
    for index, item in df.iterrows():
        bday = item['Birthday'].strftime("%d-%m")
        if(today == bday) and yearNow not in str(item['Year']):
            number= df["Number"][i]
            contact = '+91'+ str(number)
            

            pywhatkit.sendwhatmsg(contact, item["Wishes"]+" "+ df["Name"][i] , 13,47 )
             
            writeInd.append(index) 
        i=i+1  
