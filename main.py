import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace these with your information
sender_email = "sender email"  # Your Gmail address
receiver_email = "receiver email"  # Recipient's email address
password = input("Type your app password and press enter: ")  # Use your app password

# Create the email message
message = MIMEMultipart("alternative")
message["Subject"] = "Automated Email"
message["From"] = sender_email
message["To"] = receiver_email

# Create the HTML version of your message
html = """\
<html>
 <body>
 <p>Hi,<br>
 <br>
 This is an <b>automated</b> email.
 </p>
 </body>
</html>
"""

# Turn this into a MIMEText object
part = MIMEText(html, "html")
message.attach(part)

try:
    # Connect to the Gmail SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # Upgrade the connection to a secure TLS connection
    server.login(sender_email, password)  # Login to your Gmail account
    server.sendmail(sender_email, receiver_email, message.as_string())  # Send the email
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()  # Close the server connection
