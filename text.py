#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC99e423da23abdd21268a6067268a033c"
# Your Auth Token from twilio.com/console
auth_token  = "dbce85e9df43c6e9b7545f02122c8c5d"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+491631434458",
    from_="+15406921732",
    body="宝宝我爱你！！！")

print(message.sid)
