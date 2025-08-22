from backupcfg import backupFile
from backupcfg import srcDir
from backupcfg import srcFile
from backupcfg import dstDir
 
import smtplib
 
import sys
import pathlib
import shutil
from datetime import datetime
 
import sys
import logging

#Copy the file
#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the elasticemail.com smtp server.

"""

import smtplib

smtp = {"sender": "30025583@students.sunitafe.edu.au",    # elasticemail.com verified sender
        "recipient": "hwin@sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "in-v3.mailjet.com",      # elasticemail.com SMTP server
        "port": 587,                           # elasticemail.com SMTP port
        "user": "",      # elasticemail.com user
        "password": ""}     # elasticemail.com password

# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print("ERROR: An error occurred.")
#!/usr/bin/python3

import sys
import pathlib
import shutil
from datetime import datetime

def copyFileDirectory():
    """
    This Python code demonstrates the following features:
    
    * extracting the path component from a full file specification
    * copying a file
    * copying a directory.
    
    """
    try:
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
        
        srcFile = "/home/ec2-user/environment/ICTPRG302AssDoc/file1.txt"
        srcDir = "/home/ec2-user/environment/ICTPRG302AssDoc/dir1"
        
        srcLoc = srcFile # change this srcLoc = srcDir to test copying a directory
        srcPath = pathlib.PurePath(srcLoc)
        
        dstDir = "/home/ec2-user/environment/ICTPRG302AssDoc/backups"
        dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
        
        print("Date time stamp is " + dateTimeStamp) 
        print("Source file is " + srcFile)
        print("Source directory is " + srcDir)
        print("Source location is " + srcLoc)
        print("Destination directory is " + dstDir)
        print("Destination location is " + dstLoc)
        
        if pathlib.Path(srcLoc).is_dir():
            shutil.copytree(srcLoc, dstLoc)#Copying the Wholoe Directory/Folder
        else:
            shutil.copy2(srcLoc, dstLoc)#Copy thw Whole File
    except:
        print("ERROR: An error occurred.")
    
#check the job file
#!/usr/bin/python3

import sys
import logging
logging.basicConfig(filename=backupFile, level = logging.DEBUG)
loggerFile = logging.getLogger()

def main():
    """
    This Python code demonstrates the following features:
    
    * accessing command line arguments.
    
    """
    try:
        argCount = len(sys.argv)
        program = sys.argv[0]
        arg1 = sys.argv[1] #getting the job's number by the number provided 
        
        print("The program name is " + program + ".")
        print("The number of command line items is " + str(argCount) + ".")
        print("Command line argument 1 is " + arg1 + ".")
        if arg1 == 'job1'or arg1 == 'job2'or arg1 == 'job3': #check if the job number is correct
         copyFileDirectory() #Copy the Files by calling the "callFileDirctory" function
         loggerFile.info("SUCCSESS")
         print ("copy this file")
        else:#If the Job file is incorrect
            print("logging and sending email")
            loggerFile.error("ERROR-FAIL: Job Number is inorrect")
    except Exception as e: #Catch the unexpted Error
        print("ERROR: An error occurred.")
        sendEmail("Exceptions Occured {e}")#Sending the email alert
    
if __name__ == "__main__":
    main()
