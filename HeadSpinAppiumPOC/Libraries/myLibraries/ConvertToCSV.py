import subprocess

#Call VBS function from python
def callVBS(scriptPath,ExcelPath,OutputPath):
    try:
        subprocess.call('cscript.exe '+ scriptPath +' '+ExcelPath+' '+OutputPath)
        return "PASS"
    except:
        return "FAIL"