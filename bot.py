import telebot



token = ""

bot = telebot.TeleBot(token)


file = False
file_path = None

help_string = """ 
AVAILABLE COMS: 
---------------
/validate 
                  
/compute_tranfers 
                  
/export
                  
/magic
"""
# bot.send_message(message.chat.id,

start_info_msg = """
Pipeline: 
1. send document in .xlsx format
2. /validate command (to check bad cases) 
3. /compute_tranfers (to compute placement for transfers)
4. /export (to download final result)
"""

# write as class 

@bot.message_handler(commands=['start'])
def start_func(msg):
    bot.send_message(msg.chat.id, start_info_msg + "\n /help")
    

@bot.message_handler(commands=['help'])
def get_help_info(msg):
    #pass    
    bot.send_message(msg.chat.id, help_string)


@bot.message_handler(content_types=['document'])
def handle_docs(msg):
    file_name = msg.document.file_name
    # add hash here per session
    file_info = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open('./cache/' + file_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    global file 
    global file_path
    file = True
    file_path = './cache/' + file_name

# ------ 

@bot.message_handler(commands=['compute_tranfers'])
def doc_comp(msg):
    global file
    reply = 'process...' if file else 'upload_file' 
    bot.send_message(msg.chat.id, reply)


@bot.message_handler(commands=['validate'])
def dic_val(msg):
    global file
    reply = 'process...' if file else 'upload_file' 
    bot.send_message(msg.chat.id, reply)
 

@bot.message_handler(commands=['export'])
def doc_exp(msg):
    global file 
    reply = 'process...' if file else 'upload_file' 
    bot.send_message(msg.chat.id, reply)
    # delete file 
    # update flag and path pointer    



bot.infinity_polling()


