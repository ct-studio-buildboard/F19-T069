import smtplib

email = 'reconnect.team69@gmail.com' # Your email
password = 'tech5100-team69' # Your email account password
send_to_email = 'amanda.q.trang@gmail.com' # Who you are sending the message to
message = 'This is my message' # The message in the email

server = smtplib.SMTP('smtp.gmail.com', 587) # Connect to the server
server.starttls() # Use TLS
server.login(email, password) # Login to the email server
server.sendmail(email, send_to_email , message) # Send the email
server.quit() # Logout of the email server