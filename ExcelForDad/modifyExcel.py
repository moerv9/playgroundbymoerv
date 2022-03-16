import openpyxl
import pandas as pd

wbPath= "ExcelForDad/Aderfarben.xlsx"

""" 
wb = openpyxl.load_workbook(wbPath) #workbook
sh = wb["Fertig"] #sheet
r1c1 = sh.cell(1,4).value  """
firstsheet = pd.read_excel(wbPath,sheet_name=0)
col4=pd.read_excel(wbPath,sheet_name=0,usecols="D")

def subst(i):
    if i == "schwarz":
        return i.replace("schwarz","bk")
    if i == "weiß":
        return i.replace("weiß","wh")
    if i == "blau":
        return i.replace("blau","bu")
    if i == "braun":
        return i.replace("braun","bn")
    if i == "rot":
        return i.replace("rot","rd")
    if i == "orange":
        return i.replace("orange","or")
    if i == "violett":
        return i.replace("violett","vio")
    if i == "rosa":
        return i.replace("rosa","rs")
    if i == "grün":
        return i.replace("grün","gn")
    if i == "dunkelblau":
        return i.replace("dunkelblau","dbu")
    if i == "grüngelb":
        return i.replace("grüngelb","gn/ye")
    if i == "braunschwarz":
        return i.replace("braunschwarz","bn/bk")
    if i == "grau":
        return i.replace("grau","gy")
    else:
        return i
    
#df=col4["Ader 1"].to_numpy().tolist()
for i in range(1,100):
    col = firstsheet["Ader "+str(i)].to_numpy().tolist()
    result = map(subst,col)
    newdf = pd.DataFrame.from_dict(result)
    firstsheet["Ader "+str(i)] = newdf
    


newlist = []
resultList = []

for i in range(len(firstsheet.index)):
    for j in range(3,102):
        addthis = firstsheet.loc[i][j]
        
        if str(addthis) != 'nan':
            newlist.append(addthis)
        newstringfromList=''.join(str(newlist)[1:-1])
    newlist=[]
    resultList.append(newstringfromList)

print("\n".join(resultList))


firstsheet.insert(3,"Anschlüsse",resultList)
print(firstsheet.iloc[[6000]])

with pd.ExcelWriter("ExcelForDad/Modifizierte_Aderfarben.xlsx") as writer:
    firstsheet.to_excel(writer,sheet_name="Fertig",index=False)



