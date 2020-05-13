'''
Created on Nov 6, 2018

@author: kumarsis
'''
# -*- coding: cp1252 -*-
# The execution starts from calling  validate_Input(inputFilePath) in which ith path of input directory is given
# this function checks if a file called common.bin is present or not.if it is present it checks if credentials are present
# in encrypted format in it or not.if  found it reads th common.bin line by line, decrypts the credentials and stores in
# a temporary file name temp.txt. Now from this file values are read one by one and checked if the UUID(computers unique identification number)
# of the computer running the code matches with any already stored UUID in the common.bin(and temp.txt after encryption).if it matches  it means,
# this computer has run the script earlier and was authorised.Now when the UUID matches, the function again reads the next line(userid in temp.txt)
# to see if the userid stored in common.bin in encrypted format (now also  in temp.txt after decryption) matches the current user id of the user.
# if both of these match, then the authentication passes and ATT_Username and password are printed.

# if the file common.bin is not present ,check_input_file(inputfilepath) is called which also takes the path of input directory as parameter.It checks
# if input.txt is present or not.if it is not present it gives error that inputfile is not present.if it is present it checks if the file is empty
# or not, if it is empty an error is displayed that the file is empty.Else all the credentials are read from input .txt and stored in variables.
# also it is checked that common.bin file is present or not in the input directory.if not, it is created
# then UpdateNewuser(UUID,inputFilePath) function is called .This functions takes the variables from input.txt and also UUID(in parameter),it encrypts
# them and stores in the file called common.bin in the input directory.then again validate_Input(inputFilePath) is called and process begins from beginning.

# Thus it is a two level authentication (UUID and userId) as well as encryption to make the authentication as secure as possible.The algorithm
# uses AES encryption for 128 bit encryption.Still the key can be more of any bit lenght(not just multiple of 16 ) as it uis hashed.

from  Crypto.Cipher import AES
import base64
from Crypto import Random
import os
from io import BytesIO
# import platform, os
import subprocess
import getpass
from Crypto.Hash import SHA256
from encodings import utf_8
import logging

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
#unpad = lambda s: s[0:-ord(s[-1])]
unpad = lambda s: s[0:-s[-1]]
credentials = None


# class AESCipher:
class AuthenticationNew:
    
    def __init__(self, key):
        
        self.key = SHA256.new(key).digest()

#     def get_loggings(self):
#         #logging.disable(logging.INFO) 
#         for key in logging.Logger.manager.loggerDict:
#             print("abc") 
#              
#             logging.getLogger(key).setLevel(logging.CRITICAL) 

# #function to encrypt raw data
    def encrypt(self, raw):
        raw = pad(raw).encode('utf-8')
        iv = Random.new().read(AES.block_size)   
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

# #function to decrypt raw data
    def decrypt(self, enc):
        enc = base64.b64decode(enc)
       # iv = Random.new().read(AES.block_size)
        iv = enc[:16]
       
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))
#######################################################################################################################
#######################################################################################################################

# #function to get UUID
    def cpu_info(self):
        #important changed the below line as bytes and string are copnsidered different in python3 and not in python2
       # current_machine_id = base64.b64encode(subprocess.check_output('wmic csproduct get uuid').split('\n')[1].strip())
       try:
          current_machine_id = subprocess.check_output('wmic csproduct get uuid').decode('utf-8').strip('UUID').replace('\n','').strip()
       except AttributeError:   
            current_machine_id = subprocess.check_output('wmic csproduct get uuid').strip('UUID').replace('\n','').strip()
       return current_machine_id

    #####################################################################################################################
    #####################################################################################################################
    UUID_Actual = cpu_info(None)
    secret = cpu_info(None) 
    #######################################################################################################################
    #######################################################################################################################

    def getUsername(self):
        user_name = getpass.getuser()
        return user_name
    
    #######################################################################################################################
    #######################################################################################################################
    def file_read(self, fname):
        with open(fname) as f:
            content_list = f.readlines()
            return content_list

    #######################################################################################################################
    #######################################################################################################################
    
    # #function to create a new file in the given file path
    def createFile(self, filePath):
        f = open(filePath, 'w+')
        f.close()
    
    #######################################################################################################################
    #######################################################################################################################
    
    # #reading inputs from input.txt and setting variables for the run
    # it checks if file is present or not.if yes is it vacant or not.if not
    # het values of credentials from this file and call UpdateNewuser(UUID, inputFilePath) to set encrted values of variables in common.bin
                
    def check_input_file(self, inputFilePath):
        print("calling check input")
        commonFilePath = inputFilePath
        if os.path.isfile(inputFilePath + "\\input.txt"):
           name = self.file_read(inputFilePath + "\\input.txt")
           if not len(name) == 0:
               print("using input file")
               global user_name
               user_name = name[0]
               global att_user
               att_user = name[1]
               global password
               password = name[2]
               global itServicesPassword
               itServicesPassword = name[3]
               global rsaPin
               rsaPin = name[4].rstrip()
               global testItServices
               try:
                  testItServices = name[5]
               except IndexError:  
                   testItServices = None 
               self.UpdateNewuser(UUID, inputFilePath)
               open(inputFilePath + '\\input.txt', 'w').close()
           else:
               print("input file is blank or not present and credentials could not be matched")
               exit(1)
    
        else:
            print("file does not exist")
       
        return self.credentials
        #if not os.path.isfile(inputFilePath + "\\common.bin"):
          
            #self.createFile(inputFilePath + "\\common.bin")
    #######################################################################################################################
    #######################################################################################################################
    # check_input_file("C:\\SourceCloud\\smoketest\\properties\\Input")
    
    #######################################################################################################################
    #######################################################################################################################
    
    # #encrypting username and passwords and other variables and writing in common.bin
    def UpdateNewuser(self, UUID, commonFilePath):
        print("calling update")
       # with open(commonFilePath + '\\common.bin', 'a+') as f:
        with open(commonFilePath + '\\common.bin', 'w+') as f:
            try :
                f.writelines(self.encrypt(UUID).decode('utf-8'))
                f.write("\n")
            except AttributeError:
                f.writelines(self.encrypt(UUID))
                f.write("\n")    
            f.writelines(self.encrypt(user_name).decode('utf-8'))
            f.write("\n")
            f.writelines(self.encrypt(att_user).decode('utf-8'))
            f.write("\n")
            f.writelines(self.encrypt(password).decode('utf-8'))
            f.write("\n")
            #if itServicesPassword == None:
            #   f.writelines(self.encrypt("dummy_value").decode('utf-8'))
            #   f.write("\n")
            #else:
            f.writelines(self.encrypt(itServicesPassword).decode('utf-8'))
            f.write("\n") 
            f.writelines(self.encrypt(rsaPin).decode('utf-8'))
            f.write("\n")  
            if testItServices == None:
               f.writelines(self.encrypt("dummy_valueTest").decode('utf-8'))
               f.write("\n")
            else:
               f.writelines(self.encrypt(testItServices).decode('utf-8'))
               f.write("\n")
            #f.writelines(self.encrypt(testItServices).decode('utf-8')) 
            f.writelines("--------------------------------------------------------------------------------------------------------")
            f.write("\n")
        open(commonFilePath + '\\input.txt', 'w').close()
        self.validate_Input(commonFilePath)
    
    #######################################################################################################################
    #######################################################################################################################
    
    # #validating values of username and passwords.it checks if UUID, username , att_username, password matches with that present in common.bin
    # if it matches it returns a list of credentials containing att_usernams,password and itservicesPassword
    def validate_Input(self, commonFilePath):
        print ("calling validate")
        self.createFile(commonFilePath + "\\temp.txt")
        
        
        if os.path.isfile(commonFilePath + "\\input.txt"):
            name = self.file_read(commonFilePath + "\\input.txt")
            if len(name) == 0:
       # if os.path.isfile(commonFilePath + "\\common.bin"):
                with open(commonFilePath + '\\common.bin', 'r+') as file:
                        global UUID
                        UUID = self.decrypt(file.readline()).decode('utf-8')
                        global user_name
                        user_name = self.decrypt(file.readline()).decode('utf-8')
                        global att_user
                        att_user = self.decrypt(file.readline()).decode('utf-8')
                        global password
                        password = self.decrypt(file.readline()).decode('utf-8')
                        global itServicesPassword
                        itServicesPassword = self.decrypt(file.readline()).decode('utf-8')
                        #print(itServicesPassword)
                        global rsaPin
                        rsaPin = self.decrypt(file.readline()).decode('utf-8')
                        global testItServices
                        testItServices = self.decrypt(file.readline()).decode('utf-8')
                     
                        global lineSeparator
                    
                        lineSeparator = file.readline()
                       # print "line separator is  " + lineSeparator
                        with open(commonFilePath + '\\temp.txt', 'a+') as fileTemp:
                                fileTemp.write(UUID)
                                fileTemp.write("\n")
                                fileTemp.write(user_name)
                                
                                fileTemp.write(att_user)
                                fileTemp.write(password)
                                fileTemp.write(itServicesPassword)
                                #fileTemp.write("\n")
                                fileTemp.write(rsaPin)
                                fileTemp.write("\n")
                                fileTemp.write(testItServices)
                                fileTemp.write("\n")
                                fileTemp.write(lineSeparator)
                                print ("line is " + lineSeparator)
                                # fileTemp.write("\n")
                with open(commonFilePath + '\\temp.txt', 'r') as TempFile:
        
                    user_name_Actual = self.getUsername()
                    #print("username actual is "+user_name_Actual.rstrip() +"line")
    
                    UUID_final = TempFile.readline()
                    user_name_final = TempFile.readline()
                    #print("username final is "+user_name_final.rstrip() +"line")
                    att_user_final = TempFile.readline()
                    Password_final = TempFile.readline()
    
                    itServicesPassword_final = TempFile.readline()
                    rsaPinFinal = TempFile.readline()
    
                    testItServicesFinal=TempFile.readline()
    
                    lineSeparator_final = TempFile.readline()
    
                    if str(UUID_final).strip()==self.UUID_Actual.rstrip():
                        print ("UUID is matched and correct")
                        if user_name_final.rstrip().lower()==user_name_Actual.rstrip().lower():
                            print ("UUID and username matches checking credentials now")
                            if str(att_user_final).rstrip()==att_user.rstrip():
                                 print ("att_user matches.now checking password")
                                 if str(Password_final).rstrip()==password.rstrip():
                                     print("  password also matches.checking itservices password")
                                     if str(itServicesPassword_final).rstrip()==itServicesPassword.rstrip():
                                         print(str(rsaPinFinal).rstrip()+"||||||"+str(rsaPin).rstrip()+"<||||||")
                                         print("itServicesPassword also matches, checking rsa pin")
                                         if str(rsaPinFinal).rstrip()==str(rsaPin).rstrip():
                                            print("rsa matches. checking testItServices if present") 
                                            if str(testItServicesFinal).rstrip()==testItServices.rstrip():
                                                print("TestItservices also matches.User is authentic")
                                                self.credentials = [att_user, password, itServicesPassword,rsaPin,testItServices]

                TempFile.close()
                open(commonFilePath + '\\temp.txt', 'w+').close()
                os.remove(commonFilePath + '\\temp.txt')
                return self.credentials
            else:
            # exit(1)
                self.check_input_file(commonFilePath)
                
            

        
        else:
            print("input file is blank or not present and credentials could not be matched")
            exit(1)
            

        #else:
         #   self.check_input_file(commonFilePath)
    
    #######################################################################################################################
    #######################################################################################################################
    
    def main(self, inputFilePath):
        global UUID
        #self.get_loggings()
        UUID = self.cpu_info()
        self.validate_Input(inputFilePath)
        
        return self.credentials
    def create_profile(self,path):
        from selenium import webdriver
        fp =webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir",path)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk",'application/csv')
        fp.update_preferences()
        return fp.path

