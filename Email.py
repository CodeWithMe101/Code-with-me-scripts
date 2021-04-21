import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('Email', 'Password') #replace with relevant details
conn.sendmail('Email','recipient', /
              'Subject: so long...\nSo long, and thanks for all the fish....')
con.quit()
