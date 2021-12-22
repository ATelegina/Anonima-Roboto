######
# POR KE VIA ROBOTO FUNKCIU, ŜANĜU "TOKENOOOOOOO" AL TOKENO, RICEVITA DE @BotFather
# POR RICEVI IDILO_DE_LA_BABILEJO SENDU /IDILO AL LA GRUPO 
######


import random


TOKEN = "TOKENOOOOOOOOOO"
#EKZEMPLE: TOKEN = "1889084381:AAFA5Q8B9K2W5iuXS3pZm9fyfUykH9EG9aE"
ne_id = "IDILO_DE_LA_BABILEJO. FORIGU CITILOJN!"
#EKZEMPLE: ne_id = -1001204743894

    
frazoj=["La mesaĝo estas sendita"]
kodilo = "@#$%^^&**!@#$%^&QOurjwSGlkqmalBX%@#$@fl%@GHSNXL:>QOS>XSO@sp&%$@#VLMIIDM@&NXS>DLkmpDWsOWI*@*@@__@_@JDKSLKSJDJWkld[**U*U*UJDJI*W*U*DJKJDIJDJ*J*DJJkwmxbfDDKI**JIJ**JIJJOIJ@*HDSNMeSOEO*E*@*@*@*@*@*NXNNjeleXU@KLLW@@**>OQP>MMNOiLEIWUEDMNVWI%^$^_*&^AHJS*%^!%&$%$"

import telebot
from telebot import types, util
import time


user_dict={}

class User:
    def __init__(self, name):
        self.teksto = None
        self.name = name
        self.tipo = None
        self.cu = None
        self.caption = None
        self.unikilo = None
        self.ligilo = None

bot = telebot.TeleBot(TOKEN)
  
versio="prenita de @Neniulo"

@bot.message_handler(commands=['start', 'komencu'])
def send_welcome(message):
    bot.reply_to(message, "La ludo komencu!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Ĵetu viajn galantvortojn, aĉulo")
    
@bot.message_handler(commands=['idilo'])
def sendu_idilon(message):
    bot.reply_to(message, "Idilo de la babilejo: {}".format(message.chat.id)) 
    
@bot.message_handler(commands=['versio'])
def send_version_de_robotino(message):
    bot.reply_to(message, "Versio: " + versio)
   
   
@bot.message_handler(content_types = ['text', 'photo', 'video', 'animation', 'sticker', 'document', 'audio', 'voice', 'poll', "video_note"])
def sendu_tekston(message):
    
    if message.chat.id != ne_id and message.chat.type == "private":
         if bot.get_chat_member(ne_id, message.from_user.id).status == 'left':   
             bot.send_message(message.chat.id, "Vi ne estas vera kloakano. Aliĝu: @Esperantujoo")
         elif message.chat.id != ne_id and message.chat.type != "private":
             pass
         else:
            
                     user_id = message.from_user.id
                     name=message.text
                     user = User(name)
                     user_dict[user_id] = user
                     user = user_dict[user_id]
                     
                     if message.text: 
                         teksto = message.text
                         user.tipo = "teksto"
                     elif message.sticker: 
                         teksto = message.sticker.file_id
                         user.tipo = "glumarko"
                         user.unikilo = message.sticker.file_unique_id
                     elif message.video_note:
                         teksto = message.video_note.file_id
                         user.tipo = "video_note"
                         user.unikilo = message.video_note.file_unique_id
                     elif message.video:
                         teksto = message.video.file_id
                         user.tipo = "video"
                         user.unikilo = message.video.file_unique_id
                     elif message.audio:
                         teksto = message.audio.file_id
                         user.tipo = "audio"
                         user.unikilo = message.audio.file_unique_id
                     elif message.voice:
                         teksto = message.voice.file_id
                         user.tipo = "voice"
                         user.unikilo = message.voice.file_unique_id
                     elif message.document:
                         teksto = message.document.file_id
                         user.tipo = "document"
                         user.unikilo = message.document.file_unique_id
                     elif message.photo:
                         teksto = message.photo[-1].file_id
                         user.tipo = "bildo"
                         user.unikilo = message.photo[-1].file_unique_id
                     elif message.animation:
                         teksto = message.animation.file_id
                         user.tipo = "movbildo"
                         user.unikilo = message.animation.file_unique_id
                     elif message.poll:
                         teksto = message.poll
                         user.tipo = 'poll'
                         i = 0
                         user.unikilo = teksto.question
                         while i < 11:
                             try: 
                                 
                                 opcioj = teksto.options[i].text
                                 i +=1
                                 user.unikilo = user.unikilo + kodilo + opcioj
                             except Exception as e:
                                 i = 11
                                 
                     
                     if message.caption:
                         print("mmmm capciooo")
                         caption = message.caption
                     else:
                         print("klf estas via kapcio")
                         caption = None
                        
                     user.teksto = teksto
                     user.caption = caption
                     
                     
                     if True:
                         markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
                         itembtn1 = types.KeyboardButton('Jes')
                         itembtn2 = types.KeyboardButton('Ne')
                         markup.add(itembtn1, itembtn2)
                         message = bot.reply_to(message, "Ĉu vi certas ke vi volas sendi ĉi tiun aĉaĵon {}?".format("[kloaken](https://t.me/Esperantujoo)"), reply_markup=markup, parse_mode = "Markdown", disable_web_page_preview=True)
                         bot.register_next_step_handler(message, certas_demando)
                    
    else:
        bot.send_message(message.chat.id, "Via mesaĝo ne povas esti sendita pro talpoj. Identilo de babilejo: " + str(ne_id) + " tamen devus esti " + str(message.chat.id) + ". Tipo de babilejo: " + str(message.chat.type))
def responda_ligilo(tekst):
    return None, None
    
def certas_demando(message):
        try:
                 user_id = message.from_user.id
                 if message.text:
                    cu = message.text
                 else:
                         sendu_tekston(message)
                         return
                 print("denove jes kara")
                 user = user_dict[user_id]
                 print("kaaraaaaaaaa")
                 if (cu.lower() == u'jes') or (cu.lower() == u'"jes"'):
                     user.cu = cu
                 elif cu.lower() == u'ne':
                     time.sleep(0.3)
                     bot.reply_to(message, 'Okej')
                     return
                 else:
                    sendu_tekston(message)
                    return                   

                 time.sleep(2)
                                 
                 capcio = user.caption               
                 
                 if user.tipo == 'teksto': 
                     if responda_ligilo(user.teksto) != None:
                         respondato, tekst = responda_ligilo(user.teksto)   
                         try:
                             msg = bot.send_message(ne_id, tekst, reply_to_message_id=respondato)
                         except Exception as e:
                             msg = bot.send_message(ne_id, user.teksto)
                     else:
                         msg = bot.send_message(ne_id, user.teksto)
                 elif user.tipo != "poll" and user.tipo != "glumarko": 
                    if user.caption != None:
                         print("lll"+ str(user.caption) + "lll")
                         respondato, capcio = responda_ligilo(user.caption)
                    else:
                        respondato = None
                        
                 knopka = None
                 if user.tipo == 'glumarko': msg = bot.send_sticker(ne_id, user.teksto, reply_markup=knopka)
                 if user.tipo == 'movbildo': 
                     try:
                         msg = bot.send_animation(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka)
                     except Exception as e:
                         msg = bot.send_animation(ne_id, user.teksto, caption = user.caption, reply_markup=knopka)
                 if user.tipo == 'voice': 
                     try:
                         msg = bot.send_voice(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka)
                     except Exception as e:
                         msg = bot.send_voice(ne_id, user.teksto, caption = user.caption, reply_markup=knopka)
                 if user.tipo == 'document': 
                     try:
                         msg = bot.send_document(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka)
                     except Exception as e:
                         msg = bot.send_document(ne_id, user.teksto, caption = user.caption, reply_markup=knopka)
                 if user.tipo == 'video':
                     try:
                         msg = bot.send_video(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka)
                     except Exception as e:
                         msg = bot.send_video(ne_id, user.teksto, caption = user.caption, reply_markup=knopka)
                 if user.tipo == 'video_note': msg = bot.send_video_note(ne_id, user.teksto, reply_markup=knopka)
                 if user.tipo == 'audio': 
                     try:
                         msg = bot.send_audio(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka)
                     except Exception as e:
                         msg = bot.send_audio(ne_id, user.teksto, caption = user.caption, reply_markup=knopka)
                 if user.tipo == 'bildo':
                     try:
                         msg = bot.send_photo(ne_id, user.teksto, caption = capcio, reply_to_message_id=respondato, reply_markup=knopka) 
                     except Exception as e:
                         msg = bot.send_photo(ne_id, user.teksto, caption = user.caption, reply_markup=knopka) 
                 if user.tipo == 'poll' : 
                     if user.teksto.correct_option_id != None: enketa_tipo = 'quiz'
                     else: enketa_tipo = None
                     msg = bot.send_poll(ne_id, user.teksto.question, user.teksto.options, type = enketa_tipo, correct_option_id = user.teksto.correct_option_id, allows_multiple_answers=user.teksto.allows_multiple_answers, is_anonymous = user.teksto.is_anonymous, explanation = user.teksto.explanation)
                 
                         
                 bot.send_message(message.chat.id, frazoj[random.randint(0,len(frazoj)-1)])


        except Exception as e:
              print(e)
              time.sleep(0.3)
              bot.send_message(message.chat.id, "Eraro okazis ({}). Provu denove".format(e))



bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()  
               
bot.infinity_polling(allowed_updates=util.update_types)

