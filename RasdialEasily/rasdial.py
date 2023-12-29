import os
import time
import yagmail
def connect(username,password):
    name = "MyInternet"
    cmd_str = "rasdial \"%s\" %s %s" %(name,username,password)
    res = os.system(cmd_str)
    if res == 0:
        return True
    else:
        print(res)
    time.sleep(5)
def disconnect():
    name="Seele's Internet"
    cmdstr="rasdial %s /disconnect" %name
    os.system(cmdstr)
    time.sleep(5)
def get_local_ip_address():
    ip_address = ''
    try:
        ipconfig_progress = os.popen('ipconfig')
        ipconfig_output = ipconfig_progress.read()
        ipconfig_progress.close()
        for line in ipconfig_output.split('\n'):
            if ('IPv4' in line) and ('220' in line):
                ip_address = line.split(': ')[-1]
                break
    except:
        print("error")
    return ip_address
def email_get_and_send():
    read = open("emailInfo.txt","r")
    email_address,verification_code,domain_name = [i.strip() for i in read.readlines()]
    print(email_address,verification_code,domain_name)
    ip = get_local_ip_address()
    mail = yagmail.SMTP(email_address,verification_code,domain_name)
    mail.send(email_address,"Current ip of your computer",ip)
    mail.close
    read.close()

if __name__ == "__main__":
    f = open("rasdialInfo.txt","r")
    line1,line2 = [i.strip() for i in f.readlines()]
    print(line1,line2)
    if(connect(line1,line2) == True):
        print("Success!")
        email_get_and_send()
    f.close()