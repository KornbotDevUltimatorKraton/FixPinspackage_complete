from audioop import reverse
from numbers import Complex
import os 
import math
import json
from tabnanny import check 
import pandas as pd
import subprocess 
import psycopg2 # Getting the data from the postgres database and insert the json file into the list of the data
from PyPDF2.generic import FloatObject 
import difflib
username = str(subprocess.check_output("uname -a",shell=True)) # Get the the username of the computer reading from the client computer 
Getusername = username.split("-")[0].split(" ")[1]  #Get the username
EXTRACT  = "/home/"+str(Getusername)+"/Automaticsoftware/tempolarydocextract" #Tempolary read the file extraction from the pdf specification function
CONFIG   = "/home/"+str(Getusername)+"/Automaticsoftware/Configuresearch" # Config file

inputcomp = "bq25616" #Testlist={'drv8873','drv8846','bq25616','bq25731','drv8320','tps62750'}

getpage = 5  #'3'
#Getting the csv file and dataframe 
df = pd.read_csv(EXTRACT+"/"+inputcomp+"/"+inputcomp+"_"+str(getpage)+".csv")
print(df) #Getting the data frame before extracting the name from the columns into the list and starte to running the editor in xml file
#Getting the pins name data 
PinsNamepack = []
PinsNumpack  = []
IONamepack = [] # Getting the io name pack 
Packagingdata = {} 
PackagewithIO = {} 
completepack = {} 
completeioname = {} 
check_datatype = {}
Check_Packagename = []  # Checking the list of the package name inside the list 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
#For multipackages
Generate_Pinspack = []
Generate_Numpack = [] 
Generate_iopack = [] 
completeNumpack = {} # Getting the new pins name append into the dictionary 
completePinspack = {} #Getting the complete pins pack data  
n = 1
n1 = 0
n2 = 2
n3 = 3

Classified_package = {'Multipackage':['NAME', 'NO.', 'nan', 'nan', 'nan'],'Singlepackage':['NAME', 'NO.', 'nan', 'nan']}
False_package_check = {'True':'Singlepackage','False':'Multiplepackage'} # Getting the True Single package data ad false multipackage
print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
print(df.columns.values[n1]) #Getting the the columns 0 of the data frame testing getting name from the detected dataframe 
for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])
listConfig = os.listdir(CONFIG)
def Configure(configfile): 
     try: 
       data = open(CONFIG+"/"+str(configfile),'r') #Open the configuretion file for the path 
       datas = data.readline()
       transfer = json.loads(datas)
       return transfer
     except:
        print("Not found the configure file please check again")
def intersection(lst1, lst2):   # Fidning the intersection of 2 list 
    lst3 = [value for value in lst1 if value in lst2]
    return lst3 

config_data = Configure(listConfig[0])
print(config_data.get('pinsconfig').get('Pins')) # Finding the matching of the list in percentage using sequence matcher
print("Header name",df.values.tolist()[0])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
print("Second name",df.values.tolist()[1])  # Specify the 2 difference package from component using second row of first column you will found nan on the list
headerpackage = df.values.tolist()[0] 
Secondpackage = df.values.tolist()[1]

def Matchingdata_cal(checkpackage,listheader): 
                percent=difflib.SequenceMatcher(None,checkpackage,listheader)
                print("Match found:"+str(percent.ratio()*100)+"%") #Getting the percent matching 
                prob = percent.ratio()*100 # Calculate the percentage inside the list to find the max value in possibility detection 
                return  prob

#Checking if the package is only one package in the datasheet in the list  devices 

for i in list(Classified_package):
               probdata = Matchingdata_cal(Classified_package.get(i),headerpackage) 
               check_datatype[i] =  int(probdata) # 
               print(check_datatype)
print(check_datatype)
cal_max = list(check_datatype.values())
keys_cal_max = list(check_datatype.keys())
max_index = max(cal_max)
print(max_index,'Choosing',keys_cal_max[cal_max.index(max_index)])
#Decision making from the search package data 
search_type = keys_cal_max[cal_max.index(max_index)] # Getting the search type data to make the dicision of package selection 
def SinglePackagecomponent(): 
                 for il in range(1,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              PinsNamepack.append(df[df.columns.values[n1]].values[il])
                 for il in range(1,len(df[df.columns.values[n]])):
                              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
                              PinsNumpack.append(df[df.columns.values[n]].values[il])

                 for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])

                 print(PinsNamepack)
                 print(PinsNumpack)
                 print(IONamepack)
                 for match in range(0,len(PinsNamepack)):
                           Packagingdata[PinsNamepack[match]] = PinsNumpack[match]
                 for re in range(0,len(PinsNamepack)):
                           PackagewithIO[PinsNamepack[re]] = IONamepack[re] # Mapping the gpio name  
                 completepack[inputcomp] = Packagingdata 
                 completeioname[inputcomp] =  PackagewithIO 
                 print(completepack)
                 print(completeioname) 
def MultiplePackagecomponent():
        pass
if Secondpackage[1].isnumeric() == True: 
                 print('Check package Single package') 
                 print('Checking the number of pins to calculate the page protocol ........')
                 for il in range(1,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              PinsNamepack.append(df[df.columns.values[n1]].values[il])
                 for il in range(1,len(df[df.columns.values[n]])):
                              print(str(il),df[df.columns.values[n]].values[il]) #Getting the list if the pins testing 
                              PinsNumpack.append(df[df.columns.values[n]].values[il])

                 for il in range(1,len(df[df.columns.values[n2]])):
                              print(str(il),df[df.columns.values[n2]].values[il]) #Getting the list if the pins testing 
                              IONamepack.append(df[df.columns.values[n2]].values[il])

                 print(PinsNamepack)
                 print(PinsNumpack)
                 print(IONamepack)
                 for match in range(0,len(PinsNamepack)):
                           Packagingdata[PinsNamepack[match]] = PinsNumpack[match]
                 for re in range(0,len(PinsNamepack)):
                           PackagewithIO[PinsNamepack[re]] = IONamepack[re] # Mapping the gpio name  
                 completepack[inputcomp] = Packagingdata 
                 completeioname[inputcomp] =  PackagewithIO 
                 print(completepack)
                 print(completeioname) 

elif Secondpackage[1].isnumeric() == False: 
                 print('Check package Multi package')
                 print('Checking the number of pins to calculate the page protocol ........') #This function will be running before calculate the page number of the list function 
                 #Checking the number of package inside 
                 for ir in Secondpackage:
                           if str(ir).isalpha() == True: 
                                 print("Nan package name")
                           elif str(ir).isalpha() == False: 
                                 Check_Packagename.append(ir)

                 print(Check_Packagename)
                 sortcheck = sorted(Check_Packagename,reverse=True)
                 Package_number = len(Check_Packagename)
                 Num_data = len(Check_Packagename) +1 #Getting the pins number 
                 io_data = len(Check_Packagename)+2 #Getting the package for the io data  
                 for il in range(2,len(df[df.columns.values[n1]])):
                              print(str(il),df[df.columns.values[n1]].values[il]) #Getting the list if the pins testing 
                              Generate_Pinspack.append(df[df.columns.values[n1]].values[il])
                 
                 for re in range(0,len(Check_Packagename)): 
                                print("Create array for pins",re)  
                                Generate_Numpack.append([])

                 for re in range(1,len(sortcheck)):
                              try: 
                                 for il in range(2,len(df[df.columns.values[re]])):
                                              print(str(il),df[df.columns.values[re]].values[il]) #Getting the list if the pins testing 
                                              Generate_Numpack[re].append(df[df.columns.values[re]].values[il])
                              except:
                                    print("Out of range")
                 print(Generate_Numpack) 
                 for checknumgpio in range(0,len(Generate_Numpack)):
                        if Generate_Numpack[checknumgpio] != []:
                                 GPIOnumlist = [s for s in Generate_Numpack[checknumgpio] if s.isdigit()]
                                 if GPIOnumlist != []:
                                               Generate_Numpack.clear()
                                               print(GPIOnumlist) 
                                               Generate_Numpack.append(GPIOnumlist) # Getting the new list found  inside the data 
                                               print(Generate_Numpack)
                                               for match_num in range(0,len(Generate_Numpack)): 
                                                          print(Generate_Numpack[match_num],Check_Packagename[match_num])

                                                          completeNumpack[Check_Packagename[match_num]] = Generate_Numpack[match_num] # Getting the complete gpio data reference 
               
                 #Matching pins with the number of pins in the data 
                 print(completeNumpack) 
                 print(Generate_Pinspack)
                 for packname in completeNumpack:
                      for rew in range(0,len(Generate_Pinspack)):
                              completePinspack[Generate_Pinspack[rew]] = completeNumpack.get(packname)[rew] # Getting all the pins and package name al together in one package
                              completepack[packname] = completePinspack 

                 print(completePinspack)
                 print(completepack) # Getting the complete pins pack          
                 #checkioinlist = list(completepack.get(list(completepack)).values()) # Getting the io list of data if found not the digit
                 #print(checkioinlist)
                 #realio  = [s for s in Generate_Numpack[checkioinlist] if s.isdigit()]
                 #print(realio)