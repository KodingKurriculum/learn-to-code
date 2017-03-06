# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 12:02:36 2017

@author: rswaby
"""

from email.mime.text import MIMEText
from creds import cdict
import smtplib
 
msg = MIMEText("Oh yeah python is awsome!!")

msg['Subject'] = "Hello Innovation day"
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(cdict["emailuser"],cdict["emailpass"])
server.sendmail(cdict["emailuser"],"rohan_swaby51@yahoo.com",msg.as_string())
server.quit()


