'''
Created on Jun 24, 2017

@author: moni
'''
# sms.py
# Sends sms message to any cell phone using gmail smtp gateway
# Written by Alex Le

import smtplib

# Use sms gateway provided by mobile carrier:
# at&t:     number@mms.att.net
# t-mobile: number@tmomail.net
# verizon:  number@vtext.com
# sprint:   number@page.nextel.com

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( 'bless727@gmail.com', 'Xcomp345t36;' )

# Send text message through SMS gateway of destination number
server.sendmail( 'bless727@gmail.com', '2672304684@tmomail.net', '<Rock>' )

"""

# Establish a secure session with gmail's outgoing SMTP server using your gmail account
server = smtplib.SMTP( "smtp.gmail.com", 587 )

server.starttls()

server.login( '<gmail_address>', '<gmail_password>' )

# Send text message through SMS gateway of destination number
server.sendmail( '<from>', '<number>@tmomail.net', '<msg>' )"""