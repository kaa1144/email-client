import os
import pymongo

from pyrogram import Client, filters
from tools.read_config import read_config
from tools.db_tools import  search_user

from email_client.email_send import send_mail
from email_client.email_get import recieve_mail

from model.db import create_connection

config_data = read_config('./config/config_bot.json')
app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])
db = create_connection()
table = db.users.users

 
@app.on_message(filters.command('recieve'))
def recieve_emails(client, message):
    
    #extract identifier form client or message
    # db_user = search_user(client, table)
    
    message.reply_text('getting emails') 
    
    # user = db_user['email'] 
    # pwd = db_user['password']
    
    texts = message.text.split(" ")
    user = texts[1]
    pwd = texts[2]
    emails = recieve_mail(user,pwd)
    for i in emails:
        message.reply_text(i)

# TODO make this to work with diferent messages, 
# /send triggers the action and then it asks for credentials (or get them from the stored date)
# then it asks for the email of the reciever
# then the subject and finally the body of the email 

@app.on_message(filters.command('send'))
def send_email(client,message):
    
    #extract identifier form this
    # db_user = search_user(client, table)

    texts = message.text.split(" ")

    # user = db_user['email'] 
    # pwd = db_user['password']

    user = text[1]
    pwd = texts[2]
    to = texts[3]
    subject = texts[4]
    body = texts[5]
    
    send_mail(user,pwd,to,subject, body)    
    message.reply_text('Sent!')
    
@app.on_message(filters.command('version'))
def get_version(client, message):
    message.reply_text('V-0.2') 

@app.on_message(filters.command('register'))
def register_user(client, message):
     
    #TODO Encript email and password
    userinfo = {}
    userinfo['identifier'] = identifier
    userinfo['email'] = email
    userinfo['password'] = password
    
    result = table.insert_one(userinfo)
    
if __name__ == '__main__':
    app.run()
    # main()

