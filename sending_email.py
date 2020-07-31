#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:09:36 2019
@author: njcandelaria

HOW TO SEND AN EMAIL

"""


def send_me_an_email():
    
    import smtplib

    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    
    from_add = '...'
    to_add = "..."
    
    msg =  MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    
    msg['Subject'] = "Ping: Code ready"
    body = 'I believe your code is ready, sir.'
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, '...')
    text = msg.as_string()
    server.sendmail(from_add, to_add, text)
    server.quit()
    
    """
    OPTION # 2
    """  
    
#    import smtplib
#    import ssl
#
#    port = 465  # For SSL
#    smtp_server = "smtp.gmail.com"
#    sender_email = "..."  # Enter your address
#    receiver_email = "..."           # Enter receiver address
#    password = "..."
#    message = """\
#    Subject: Hi there
#    
#    This message is sent from Python."""
#
#    context = ssl.create_default_context()
#    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#        server.login(sender_email, password)
#        server.sendmail(sender_email, receiver_email, message)
    
    
    """
    OPTION # 3
    """
    
#    fromaddr = '...'  
#    toaddrs  = '...'  
#    msg = 'Spam email Test'  
#    
#    username = '...'  
#    password = '...'
#    
#    server = smtplib.SMTP('smtp.gmail.com', 587)  
#    server.ehlo()
#    server.starttls()
#    server.login(username, password)  
#    server.sendmail(fromaddr, toaddrs, msg)  
#    server.quit()

send_me_an_email()