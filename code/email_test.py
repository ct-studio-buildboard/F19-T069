import smtplib
from email.mime.text import MIMEText as text

email = 'reconnect.team69@gmail.com' # Your email
password = 'tech5100-team69' # Your email account password
send_to_email = 'at669@cornell.edu' # Who you are sending the message to
# message = 'This is my message' # The message in the email
job_title = "Test job"
company = "Test co"
message =  ("{}, {} has applied to your job, {}. Contact them at: {}").format(company, email, job_title, email)

m = text(message)

m['Subject'] = 'Hello!'
m['From'] = email
m['To'] = send_to_email

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email, m.as_string())
server.quit() # Logout of the email server

# message =  ('''\
# From: ReConnect\n
# Subject: {}

# {}, {} has applied to your job, {}. Contact them at: {}''').format(job_title, company, email, job_title, email)
# print(message)
# server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
# server.starttls() # Use TLS
# server.login(email, password) # Login to the email server
# server.sendmail(email, send_to_email , message) # Send the email
# server.quit() # Logout of the email server