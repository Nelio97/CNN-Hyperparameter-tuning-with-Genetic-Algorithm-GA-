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
    
    from_add = 'testemail.njcandelaria@gmail.com'
    to_add = "nelio.jac97@gmail.com"
    
    msg =  MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    
    msg['Subject'] = "Ping: Code ready"
    body = 'I believe your code is ready, sir.'
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, 'thisisatest97')
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
#    sender_email = "testemail.njcandelaria@gmail.com"  # Enter your address
#    receiver_email = "nelio.jac97@gmail.com"           # Enter receiver address
#    password = "thisisatest97"
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
    
#    fromaddr = 'njcandelaria@fc.ul.pt'  
#    toaddrs  = 'nelio_jac97@gmail.com'  
#    msg = 'Spam email Test'  
#    
#    username = 'njcandelaria@fc.ul.pt'  
#    password = 'fyutk.fculebb1819'
#    
#    server = smtplib.SMTP('smtp.gmail.com', 587)  
#    server.ehlo()
#    server.starttls()
#    server.login(username, password)  
#    server.sendmail(fromaddr, toaddrs, msg)  
#    server.quit()

send_me_an_email()