import smtplib

print("This is a very simple program that helps you automate email sending with Python. You have to enable less secure "
      "apps on the email address of the sender before this can work."
      " You can use this link to do that on Gmail. https://www.google.com/settings/security/lesssecureapps")


def send_alert():
    to_num = int(input("How many email addresses are you sending this mail to: "))
    to = []
    from_user = input("Who is this email from: ")
    while to_num > 0:
        to_prompt = input("Enter the email address to send this email to:  ").strip()
        to_num -= 1
        to.append(to_prompt)
    gmail_user = input("Enter the email address of the sender: ").strip()
    gmail_pwd = input("Enter the password of the sender's email address: ")
    subject = input("What is the subject of this email? ")
    message = input("What is the message you want to send? ")
    # gmail_type = "smtp" + input("Enter the typ")
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + ", ".join(to) + '\n' + 'From: ' + from_user + '\n' + 'Subject: ' + subject + '\n'
    msg = header + '\n' + message + '\n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()

send_alert()