

'''
 Example Python script to concurrently run multiple parametrized Robot Framework tests
 Expects following input files:
    - suite.robot:     Robot Framework test case file
    - user_list.txt:   List of usernames (one per line)
'''

import os
import random
import subprocess
import time
import webbrowser


# config
baseFolder = '..//Resources//data_tests'
testCaseName = 'Headspin testing of youtube'
DeviceFile = '..//Assets//DeviceName.txt'
testUsersPassword = 'secret'

#get robotfile path
#os.system('cmd /k "Your Command Prompt Command"')
suiteFile = os.path.join(os.path.abspath(os.getcwd()), '..\TestSuite\Driver_Appium_Trial.robot')
print(os.path.abspath(os.getcwd()))

# clean up base folder
#os.system('rm -rf ' + baseFolder)
if not os.path.exists(baseFolder):
    os.mkdir(baseFolder)

# no output to console please
FNULL = open(os.devnull, 'w')

# load list of usernames
f = open(DeviceFile, 'r')
lines = f.readlines()
f.close()

# spawn subprocess for each user
userPathes = []
processes = set()


for line in lines:
    user = line.strip()
    userPath = baseFolder + '/' + user
    userPathes.append((user, userPath))
    if not os.path.exists(userPath):
           os.mkdir(userPath)
    cmdParts = [
        'robot',
        # abitrary amount of variables can be added here
        '--variable', 'DeviceArg:' + user,
        
        # use -t argument to execute only the test named 'Login Test' from the suite
        '-t', testCaseName,
        suiteFile,
    ]
    processes.add(subprocess.Popen(cmdParts, cwd=userPath, stdout=FNULL))
    print('Spawned ' + user)

    # random timeout to simulate more realistic user behavior
    time.sleep(random.randint(0, 1))

# wait until all subprocesses finished
for proc in processes:
    proc.wait()

# collect output and open log files of failed tests
# for username, path in userPathes:
#     f = open(path + '/output.xml')
#     content = f.read()
#     f.close()
#     if 'status="FAIL"' in content:
#         print(username + '\t'*5 + '[Failed]')
#         webbrowser.open(path + '/report.html')
#     else:
#         print(username + '\t'*5 + '[OK]')
        