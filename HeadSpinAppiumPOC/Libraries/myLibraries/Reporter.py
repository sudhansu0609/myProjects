
##WRITTEN BY SUDHANSU KUMAR SINGH 
## PLEASE MENTION YOUR NAME IF YOU UPDATE IT
import os
import shutil
import datetime
import testScreenshot
now = datetime.datetime.now()

class Reporter(object):
 
    ROBOT_LIBRARY_VERSION = 1.0
     
    def __init__(self):
        pass

    def createFile(self, path):
        file_name = path + "\\report.html"
        with open(file_name, 'w+') as file_handle:
               message = """<HTML><BODY><TABLE BORDER=0 CELLPADDING=3 CELLSPACING=1 WIDTH=100% BGCOLOR=ORANGE>
                                <TR><TD WIDTH=90% ALIGN=CENTER BGCOLOR=WHITE><FONT FACE=VERDANA COLOR=ORANGE SIZE=3><B>AMDOCS</B></FONT></TD></TR><TR><TD ALIGN=CENTER BGCOLOR=ORANGE><FONT FACE=VERDANA COLOR=WHITE SIZE=3><B>Selenium Framework Reporting</B></FONT></TD></TR></TABLE><TABLE CELLPADDING=3 WIDTH=100%><TR height=30><TD WIDTH=130% ALIGN=CENTER BGCOLOR=WHITE><FONT FACE=VERDANA COLOR=//0073C5 SIZE=2><B>&nbsp; Automation Result : Wed Jul 18 18:21:54 IST 2018 on Machine KUMARSIS01 by user kumarsis on Browser IE1</B></FONT></TD></TR><TR HEIGHT=5></TR></TABLE>
                                <TABLE BORDER=0 BORDERCOLOR=WHITE CELLPADDING=3 CELLSPACING=1 WIDTH=100%>
                                <TR><TD BGCOLOR=BLACK WIDTH=20%><FONT FACE=VERDANA COLOR=WHITE SIZE=2><B>Test     Name:</B></FONT></TD><TD COLSPAN=6 BGCOLOR=BLACK><FONT FACE=VERDANA COLOR=WHITE SIZE=2><B>R1129 - OPUS</B></FONT></TD></TR>
                                </TABLE><BR/><TABLE WIDTH=100% CELLPADDING=3>
                                <TR WIDTH=100%><TH BGCOLOR=ORANGE WIDTH=5%><FONT FACE=VERDANA SIZE=2>Step No.</FONT></TH><TH BGCOLOR=ORANGE WIDTH=10%><FONT FACE=VERDANA SIZE=2> Timestamp   </FONT></TH><TH BGCOLOR=ORANGE WIDTH=15%><FONT FACE=VERDANA SIZE=2>Step Description</FONT></TH><TH BGCOLOR=ORANGE WIDTH=15%><FONT FACE=VERDANA SIZE=2>Expected Value</FONT></TH><TH BGCOLOR=ORANGE WIDTH=15%><FONT FACE=VERDANA SIZE=2>Obtained Value</FONT></TH><TH BGCOLOR=ORANGE WIDTH=10%><FONT FACE=VERDANA SIZE=2>Screen Shot</FONT></TH></TR>"""                      
               file_handle.write(message)
       
       # shutil.move(f, path)
        
        

    def apendFile(self,path,KeywordName,expected,actual,imgPath,count):
        file_name=path+"\\report.html"    
        with open(file_name,'a+') as file_handle:
             message="<TR WIDTH=100%><TD BGCOLOR=#D3D3D3 WIDTH=5% ALIGN=CENTER><FONT FACE=VERDANA SIZE=2 COLOR=green><B>1</B><TD BGCOLOR=#D3D3D3 WIDTH=15%><FONT FACE=VERDANA SIZE=2 COLOR=green>"+now.strftime("%Y_%m_%d-%H%M%S") +"</FONT></TD></FONT></TD><TD BGCOLOR=#D3D3D3 WIDTH=15%><FONT FACE=VERDANA SIZE=2 COLOR=green>"+KeywordName +"</FONT></TD><TD BGCOLOR=#D3D3D3 WIDTH=15%><FONT FACE=VERDANA SIZE=2 COLOR=green>"+expected+"</FONT></TD><TD BGCOLOR=#D3D3D3 WIDTH=15%><FONT FACE=VERDANA SIZE=2 COLOR=green>"+actual+"</FONT></TD><TD BGCOLOR=#D3D3D3 WIDTH=10% ALIGN=CENTER><A HREF='"+imgPath+"\mypic_"+count+".jpg'><IMG SRC='"+imgPath+"\mypic_"+count+".jpg' alt='Screen Shot' style='width:250px;height:200px'></A></TD></TR>"
             file_handle.write(message)
        #file_handle.close
        #shutil.move(file_handle, path)
         
    def CloseFile(self,path,message):
        file_name=path+"\\report.html"
        with open(file_name,'a+') as file_handle:
          message = """end tags"""
        file_handle.write(message)
        file_handle.close
       # shutil.move(file_handle, path)     
