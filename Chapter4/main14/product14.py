import smtplib
from email.mime.text import MIMEText

send_eamil = "neoprince1@naver.com"
send_pw = "ehddbs11!!"

recv_email = "sho801921@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
메일 내용을 여기 적습니다.
여러 줄 입력 가능
"""

msg = MIMEText(text)

msg['Subject'] = "메일 제목은 여기 넣습니다."
msg['Form'] = send_eamil
msg['To'] = recv_email

print(msg.as_string())

s=smtplib.SMTP( smtp_name, smtp_port)

s.starttls()
s.login(send_eamil, send_pw)
s.sendmail(send_eamil, recv_email, msg.as_string())
s.quit()