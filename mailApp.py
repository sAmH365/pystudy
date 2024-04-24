import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# text = "메일 내용입니다"
# msg = MIMEText(text)

msg = MIMEMultipart('alternative') # """ 따옴표 3개는 글자 자료형
content = """
<h4>제목1</h4>
<button>버튼1</button>
"""
part1 = MIMEText(content, "html")
msg.attach(part1)

msg['Subject'] ="이것은 메일제목"
msg['From'] = 'npower5377@naver.com'
msg['To'] = '홍대리'
print(msg.as_string())

s = smtplib.SMTP( 'smtp.naver.com' , 587 )
s.starttls() #TLS 보안 처리
s.login( 'npower5377' , '' ) #네이버로그인
s.sendmail( 'npower5377@naver.com', 'npower5377@naver.com', msg.as_string() )
s.close()

