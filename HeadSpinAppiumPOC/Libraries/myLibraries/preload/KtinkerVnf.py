#import enum

import tkinter as tk
import fileinput
import re
import sys
import restartModule as rsm
from tkinter import Listbox, StringVar, Checkbutton
window=tk.Tk()
window.title("VNF spinup Data")
window.geometry("1280x720")
sdc_data_file='C:\\robot_framework\\robotsolution\\robot\\resources\\SDC\\SDC_DATA.robot'
VID_data_file='C:\\robot_framework\\robotsolution\\robot\\resources\\vid\\vid_data.robot'
setcount=1
#numVidNetworks=4

def replace_vnf_data(file,old,new):
            print("old value is" + old)
            print("New Value is " + new)
            for line in fileinput.FileInput(file,inplace=1):
                line = re.sub(old,new, line)
                sys.stdout.write(line)
def get_entry(entryValue):
       print(entryValue.get())
       return entryValue.get()

def Search_String(file,StringValue):

            for line in fileinput.FileInput(file,inplace=0):
                #print(line)
                if(re.search(StringValue,line)):
                    value = re.findall(StringValue, line)
                    return  value
                #sys.stdout.write(line) 
            #return  value     
def  extract_fields(file,StringValue):
        for line in fileinput.FileInput(file,inplace=1):
              vnfDataList=re.split(" ",line)
              
testCases=['TC#02_OVS_Network_Model_Creation','TC#03_SRIOV_Network_Model_Creation','TC#04_Network_Preload_upload','TC#05_OVS_Network_SpinUp','TC#06_SRIOV_Network_SpinUp','TC#08_VNF_Model_Creation','TC#09_VNF_Preload_Upload',
           'TC#12_Deletion','TC#13_Deletionof_VNFComponents ']
def create_TestCasesCheckBox(testCases):
    i=1
    for test in testCases:
        var+i=tk.IntVar()
        Checkbutton(window,text='first',variable="var"+i).grid(column=0,row=23+i)              
# def Select_TestCases(parent=None, picks=[], side="LEFT", anchor="W"):
#    vars = []
#    for pick in picks:
#       var = IntVar()
#       chk = Checkbutton(self, text=pick, variable=var)
#       chk.pack(side=side, anchor=anchor, expand=YES)
#       vars.append(var)              
               
def  create_Variables_Mobility(vnfName,numModules):
        vnfVariables=['vlm_name_','la_name_','fg_name_','vsp_name_','vf_name_','service_name_','service_name_Run_','model_UUID_','model_IUUID_','vsp_name_flexware_','service_name_Flexware_',
                  'InvariantUUIDVnf_','UUIDVnf_']
        modelVariables=['serviceNameNetwork_','UUIDFinal_','InvariantUUID_']
                 
        print("for mobility vnfs")
        #opening data file

        with open(sdc_data_file, "a+") as dataFile:
                #iterating over list variables
                for term in vnfVariables:
                    #print(term)
                    searchText="{"+term+vnfName 
                    print(searchText)
                    #iterating over lines in file
                    dataFile.seek(0)
                    #fileData=dataFile.readlines()
                     
                    for line in dataFile:
                            if searchText in line:
                                print(searchText)
                                print(searchText+' is already present')
                    #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                    else:
                         dataFile.write('$'+searchText+'}                         '+'dummyVnfValueOfVariable\n')
                                 #
                for Modelterm in modelVariables:
                                #print(term)
                                modelSearchText="{"+Modelterm+vnfName 
                                #iterating over lines in file
                                dataFile.seek(0)
                                #fileData=dataFile.readlines()
                                  
                                for line2 in dataFile:
                                        if modelSearchText in line2:
                                            print(modelSearchText)
                                            print(modelSearchText+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                                else:
                                    for  netItr in range  (1,int(numModules)+1):
                                         dataFile.write('$'+modelSearchText+'_'+str(netItr)+'}'+'                         '+'dummyMOdelValueOfVariable\n')

 
def  create_variavles_NC(vnfName,OVSModels,SRIOVModels):  
      
        vnfFabricVariables=['vlm_name_Fabric_','la_name_Fabric_','fg_name_Fabric_','vsp_name_Fabric_','vf_name_Fabric_','service_name_Fabric_','service_name_Run_','model_UUID_Fabric_','model_IUUID_Fabric_','InvariantUUIDVnf_Fabric_','UUIDVnf_Fabric_']           
        modelOVSVariables=['UUIDFinal_OVS','InvariantUUID_OVS_','service_name_OVS_']
        modelSRIOVVariables=['UUIDFinal_SRIOV_','InvariantUUID_SRIOV_','service_name_SRIOV_']

        print("for NC vnfs") 

        #opening data file

        with open(sdc_data_file, "a+") as dataFile:
                #iterating over list variables
                for term in vnfFabricVariables:
                    #print(term)
                    searchText="{"+term+vnfName 
                    print(searchText)
                    #iterating over lines in file
                    dataFile.seek(0)
                    #fileData=dataFile.readlines()
                     
                    for line in dataFile:
                            if searchText in line:
                                print(searchText)
                                print(searchText+' is already present')
                    #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                    else:
                         dataFile.write('$'+searchText+'}                         '+'dummyValueOfFabricVariable\n')
                                 #&{NetworkRole_OVS_MCCD}        net1=oam_protected_net_1   net2=hsl_net_1 
                for ModelOVSterm in modelOVSVariables:
                                #print(term)
                                modelOvsSearchText="{"+ModelOVSterm+vnfName 
                              
                                #iterating over lines in file
                                dataFile.seek(0)
                                #fileData=dataFile.readlines()
                                  
                                for line2 in dataFile:
                                        if modelOvsSearchText in line2:
                                            print(modelOvsSearchText)
                                            print(modelOvsSearchText +' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                                else:
                                    for  netItr in range  (1,int(OVSModels)+1):
                                         dataFile.write('$'+modelOvsSearchText+'_'+str(netItr)+'}'+'                         '+'dummyMOdelValueOfOVSVariable\n') 
                                         
                                         
                                         
                #writing network roles for OVS and SRIOV 

                for line3 in dataFile:
                        if ModelOvsNetworkSearchText in line3:
                            print(ModelOvsNetworkSearchText)
                            print(ModelOvsNetworkSearchText +' is already present')
                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    dataFile.write('&'+modelOvsSearchText+'}' + "        "+"net1=abc     net2=def   net3=ghi   net4=jkl   net5=mno   net6=pqr    net7=stu   net8=vwx    net9=yza   net10=bcd\n")

                numModelOVSSearchText="{NumModels_OVS_" +vnfName                
                for line4 in dataFile:
                        if numModelOVSSearchText in line4:
                            print(numModelOVSSearchText)
                            print(numModelOVSSearchText +' is already present')
                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    dataFile.write('$'+numModelOVSSearchText+'}' + "        "+OVSModels+"\n")                          
                for ModelSRIOVterm in modelSRIOVVariables:
                                #print(term)
                                modelSRIOVSearchText="{"+ModelSRIOVterm+vnfName 
                                #iterating over lines in file
                                dataFile.seek(0)
                                #fileData=dataFile.readlines()
                                  
                                for line5 in dataFile:
                                        if modelOvsSearchText in line5:
                                            print(modelSRIOVSearchText)
                                            print(modelSRIOVSearchText+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                                else:
                                    for  netItr in range  (1,int(SRIOVModels)+1):
                                         dataFile.write('$'+modelSRIOVSearchText+'_'+str(netItr)+'}'+'                         '+'dummyMOdelValueOfOVSVariable\n')                                
                #writing network roles for OVS and SRIOV 
                ModelSRIOVNetworkSearchText="{NetworkRole_SRIOV_"+vnfName        
                for line6 in dataFile:
                        if ModelSRIOVNetworkSearchText in line6:
                            print(ModelSRIOVNetworkSearchText)
                            print(ModelSRIOVNetworkSearchText +' is already present')
                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    dataFile.write('&'+ModelSRIOVNetworkSearchText+'}' + "        "+"net1=abc     net2=def   net3=ghi   net4=jkl   net5=mno   net6=pqr    net7=stu   net8=vwx    net9=yza   net10=bcd\n")
                numModelSRIOVSearchText="{NumModels_SRIOV_"+vnfName                
                for line7 in dataFile:
                        if numModelOVSSearchText in line7:
                            print(numModelSRIOVSearchText)
                            print(numModelSRIOVSearchText +' is already present')
                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    dataFile.write('$'+numModelSRIOVSearchText+'}' + "        "+SRIOVModels+"\n")    

SDNCVariables=['_PRELOAD_TYPE','_VNF_NAME','_VOLUME_GROUPS_PRESENT','_NUMBER_OF_VOLUME_GROUPS','_SUBSCRIBER_NAME','_OWNING_ENTITY','_SUBSCRIBER_TYPE','_NW_PRODUCT_FAMILY','_NW_LCP_REGION','_NW_TENANT','_NW_PLATFORM'
               ,'_VNF_LINE_OF_BUSINESS','_VNF_PRODUCT_FAMILY','_VNF_LCP_REGION','_VNF_TENANT','_VNF_PLATFORM','_VF_MODULE_LCP_REGION','_VF_MODULE_LCP_REGION','_VF_MODULE_TENANT','_VOLUME_GROUP_LCP_REGION','_VOLUME_GROUP_TENANT']
VIDVariables=['created_service_Instance_ID_','NETWORK_ID_']
VidVolumeGroupVariables=['VOLUME_GROUP_ID_','VOLUME_GROUP_NAME_']

def  create_variavles_SDNC(vnfName,numVidNetworks,numVidVolumes): 
            print("for NC vnfs") 
            with open(sdc_data_file, "a+") as dataFile:
                #iterating over list variables
                for term in SDNCVariables:
                    #print(term)
                    searchText="{"+vnfName+term 
                    print(searchText)
                    #iterating over lines in file
                    dataFile.seek(0)
                    #fileData=dataFile.readlines()
                     
                    for line in dataFile:
                            if searchText in line:
                                print(searchText)
                                print(searchText+' is already present')
                    #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                    else:
                         dataFile.write('$'+searchText+'}                         '+'dummyVnfValueOfVariable\n')
                                 #
                for vidTerm in VIDVariables:
                                #print(term)
                                vidSearchText="{"+vidTerm+vnfName 
                                #iterating over lines in file
                                dataFile.seek(0)
                                #fileData=dataFile.readlines()
                                  
                                for line2 in dataFile:
                                        if vidSearchText in line2:
                                            print(vidSearchText)
                                            print(vidSearchText+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                                else:
                                    for  netItr in range  (1,int(numVidNetworks)+1):
                                         dataFile.write('$'+vidSearchText+'_Network_'+str(netItr)+'}'+'                         '+'dummyMOdelValueOfVariable\n') 
                for volumeTerm in VidVolumeGroupVariables:
                                #print(term)
                                volumeSearchText="{"+volumeTerm+vnfName 
                                #iterating over lines in file
                                dataFile.seek(0)
                                #fileData=dataFile.readlines()
                                  
                                for line3 in dataFile:
                                        if volumeSearchText in line3:
                                            print(volumeSearchText)
                                            print(volumeSearchText+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                                else:
                                    for  netItr in range  (1,int(numVidVolumes)+1):
                                         dataFile.write('$'+volumeSearchText+'_'+str(netItr)+'}'+'                         '+'dummyMOdelValueOfVariable\n')  
                for line3 in dataFile:
                                        if "${VNF_ID_"+vnfName in line3:
                                            print(volumeSearchText)
                                            print("${VNF_ID_"+vnfName+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    
                         dataFile.write("${VNF_ID_"+vnfName+'}'+'                         '+'dummyVnfId\n') 
                for line5 in dataFile:
                                        if "${created_service_Instance_ID_"+vnfName in line3:
                                         
                                            print("${created_service_Instance_ID_"+vnfName+' is already present')
                                #applying for else loop here.It means if condition is not matched in for loop do the part in else loop
                else:
                    
                         dataFile.write("${created_service_Instance_ID_"+vnfName+'}'+'                         '+'dummyServiceInstanceId\n')                                  

                                         
       






##creating list    
v = tk.IntVar()
tk.Radiobutton(window, text="Fresh", variable=v, value=1).grid(column=1,row=18)
tk.Radiobutton(window, text="Re-Run", variable=v, value=2).grid(column=1,row=19)

VnfData=tk.Label(text="Please enter data about your VNF here",font=("Times New Roman", 30))
VnfData.grid(column=1, row=0)
#creating Vnf type
VnfType=tk.Label(text="select your VNF type")
VnfType.grid(column=1, row=15) 

VnfTypeList =tk.Listbox(window)
VnfTypeList.grid(column=1, row=16)

for item in ["mobility", "Network Cloud"]:
    VnfTypeList.insert(tk.END, item)



#creating Vnf name
VnfName=tk.Label(text="Enter VNF name")
VnfName.grid(column=0, row=3, sticky='w')

#VnfNameValue=StringVar
VnfNameValue = StringVar()
VnfNameEntry=tk.Entry(window, textvariable=VnfNameValue)   #
VnfNameEntry.grid(column=1, row=3)

#creating heatfile name

HeatFileName=tk.Label(text="Enter heatfile  name")
HeatFileName.grid(column=0, row=4, sticky='w')
HeatFileValue = StringVar()
HeatFileNameEntry=tk.Entry(window, textvariable=HeatFileValue)
HeatFileNameEntry.grid(column=1, row=4)


#creating Policy Name
PolicyName=tk.Label(text="Enter naming policy name")
PolicyName.grid(column=0, row=5, sticky='w')
PolicyNameValue = StringVar()
PolicyNameEntry=tk.Entry(window,textvariable=PolicyNameValue)
PolicyNameEntry.grid(column=1, row=5)

#creating NFC naming code
nfcNamingCode=tk.Label(text="Enter nfc naming code")
nfcNamingCode.grid(column=0, row=6, sticky='w')
nfcNamingCodeValue=StringVar()
nfcNamingCodeEntry=tk.Entry(window,textvariable=nfcNamingCodeValue)
nfcNamingCodeEntry.grid(column=1, row=6)

#crerating Nf role
nfRole=tk.Label(text="Enter nf role", )
nfRole.grid(column=0, row=7, sticky='w')
nfRoleValue=StringVar()
nfRoleEntry=tk.Entry(window,textvariable=nfRoleValue)
nfRoleEntry.grid(column=1, row=7)
#craeting Nf naming code
nfNamingCode=tk.Label(text="Enter nf namingcode")
nfNamingCode.grid(column=0, row=8, sticky='w')
nfNamingCodeValue=StringVar()
nfNamingCodeEntry=tk.Entry(window,textvariable=nfNamingCodeValue)
nfNamingCodeEntry.grid(column=1, row=8)
#creating nf type
nfType=tk.Label(text="Enter nf type")
nfType.grid(column=0, row=9, sticky='w')
nfTypeValue=StringVar()
nfTypeEntry=tk.Entry(window,textvariable=nfTypeValue)
nfTypeEntry.grid(column=1, row=9)

#craeting number of models
numModels=tk.Label(text="Enter number of models to be run")
numModels.grid(column=0, row=10, sticky='w')
numModelsValue=StringVar()
numModelsEntry=tk.Entry(window,textvariable=numModelsValue)
numModelsEntry.grid(column=1, row=10)

#creating Sriov model count
numModelsSriov=tk.Label(text="Enter number of SRIOV models to be run")
numModelsSriov.grid(column=0, row=11, sticky='w')
numModelsSriovValue=StringVar()
numModelsSriovEntry=tk.Entry(window,textvariable=numModelsSriovValue)
numModelsSriovEntry.grid(column=1, row=11) 

#creating OVS model counrt
numModelOVS=tk.Label(text="Enter number of OVS models to be run")
numModelOVS.grid(column=0, row=12, sticky='w')
numModelOVSValue=StringVar()
numModelOVSEntry=tk.Entry(window,textvariable=numModelOVSValue)
                          
numModelOVSEntry.grid(column=1, row=12) 
#Select_TestCases(parent='Window', picks=['ram','shyam','sita','gita'], side="LEFT", anchor="W")
#creating first Submit button
submitButton = tk.Button(text="submit",bg='red',command=lambda: get_entry(content))
submitButton.grid(column=1,row=21)

#creating Second submit button
submitButton2 = tk.Button(text="submit",bg='red',command=window.destroy)
submitButton2.grid(column=1,row=23)
var1=tk.IntVar()
var2=tk.IntVar()

          
        
Checkbutton(window,text='first',variable=var1).grid(column=0,row=23)
Checkbutton(window,text='first',variable=var2).grid(column=1,row=23)

create_TestCasesCheckBox(testCases)


#starint mainloop
window.mainloop()
#print("new value is "+get_entry(VnfNameValue))
#
#newReplacedValue='SCN}' + "             " +get_entry(VnfNameValue) +'\n'
#replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# print(sdc_data_file)

#finding heat value and replacing in file
# Search_StringValue=Search_String(sdc_data_file,'Dict_LMSP}'+'[\s+a-zA-Z://0-9.-_]*'+'heatfile_Update=')  
# print(Search_StringValue)
# heatvalue=get_entry(HeatFileValue)
# replace_value=Search_StringValue[0] +heatvalue+"    "
# replace_vnf_data(sdc_data_file,Search_StringValue[0],replace_value)
# #newSearch_StringValue=Search_String(sdc_data_file,replace_value+'[\s+a-zA-Z://0-9.-_]*') 
# newSearch_StringValue=Search_String(sdc_data_file,'Dict_LMSP}'+'[\s+a-zA-Z://0-9.-_]*'+'heatfile_Update='+heatvalue+'\s+'+'[a-zA-Z://0-9.-_]*') 
# print(newSearch_StringValue[0]) 
# replace_vnf_data(sdc_data_file,newSearch_StringValue[0],replace_value)

#create_Variables_Mobility("MMM",'4')
Select_TestCases(parent='Window', picks=['ram','shyam','sita','gita'], side=LEFT, anchor="W")



















# newReplacedValue='SCN}' + "             " +get_entry(HeatFileValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(PolicyNameValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(nfcNamingCodeValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(nfRoleValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(nfNamingCodeValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(nfTypeValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(numModelsValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(numModelsSriovValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)
# 
# newReplacedValue='SCN}' + "             " +get_entry(numModelOVSValue) +'\n'
# replace_vnf_data(sdc_data_file,'SCN}[\s+a-zA-Z://0-9.-_]*',newReplacedValue)


