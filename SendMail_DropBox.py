#!/usr/bin/env python
# coding: utf-8

# In[21]:


import os
import zipfile as zf
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders


def get_filePath(dir_nam):
    file_paths=[]
    for path,sub,files in os.walk(dir_nam):
        for file in files:
            file_paths.append(os.path.join(path,file))
    return file_paths

def Zip_File(file_paths,Zip_file):
    with zf.ZipFile(Zip_file,'w') as zip:
        for file in file_paths:
            zip.write(file)
            
def send_mail(Zip_file):
    fromaddr = 'xyztest321@gmail.com'
    toaddr = 'miglani.inbox@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = fromaddr 
    msg['To'] = toaddr 
    msg['Subject'] = 'DropBox_Backup'
    body = 'Please Find The attached'
    msg.attach(MIMEText(body, 'plain')) 
    filename = Zip_file
    attachment = open('Dropbox.zip', 'rb') 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', 'attachment; filename= %s' % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls()  
    s.login(fromaddr,'xyz@1234') 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit() 
    print('Mail Sent!!')            

    
dir_name=r'C:\Users\priyanka\Desktop\dropbox'
Zip_file = 'Dropbox_Bck2.zip'
#Get file path of all files in dropbox
file_paths=get_filePath(dir_name)

#ZipFile
Zip_File(file_paths,Zip_file)

#Send Mail
send_mail(Zip_file)


