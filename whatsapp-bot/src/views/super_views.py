#!/usr/bin/python
import MySQLdb
import hashlib
import config
import random
import subprocess
from utils.media_sender import ImageSender, VideoSender, UrlPrintSender, EspeakTtsSender
from utils.media_sender import UrlPrintSender
from yowsup.layers.protocol_messages.protocolentities.message_text import TextMessageProtocolEntity
import random
db = MySQLdb.connect("brezie.com","brezieadmin","83Chandra@8#","breziead_breziewebsite")
cursor = db.cursor()
phone_no = "919049433263"
device_id = "WhatsApp"
source_id = "1"
user_id = "99999"
quote = "0"
mood_id = "0"
ref_id ="qwerTyui0"
start_id = "0"
class SuperViews():
    

    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
	self.image_sender = ImageSender(interface_layer)
	self.video_sender = VideoSender(interface_layer)
        self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [
            ("^/help", self.help),
            ("^/about", self.about),
	    ("^/latest", self.latest),  #mood_type_1
	    ("^/happy", self.happy),#mood_type_2
	    ("^/motivational", self.motivational),#mood_type_3
	    ("^/spiritual", self.spiritual),#mood_type_4
	    ("^/romantic", self.romantic),#mood_type_5
	    ("^/naughty", self.naughty),#mood_type_6
	    ("^/loved", self.loved),#mood_type_7
            ("^/roll", self.roll),
            ("/(?P<evenOrOdd>even|odd)$", self.even_or_odd),
        ]

    def about(self, message=None, match=None, to=None):
        self.url_print_sender.send_by_url(message.getFrom(), "https://github.com/joaoricardo000/whatsapp-bot-seed", ABOUT_TEXT)

    def roll(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("[%d]" % random.randint(1, 6), to=message.getFrom())

    def even_or_odd(self, message=None, match=None, to=None):
        is_odd = len(match.group("evenOrOdd")) % 2
        num = random.randint(1, 10)
        if (is_odd and num % 2) or (not is_odd and not num % 2):
            return TextMessageProtocolEntity("[%d]\nYou win." % num, to=message.getFrom())
        else:
            return TextMessageProtocolEntity("[%d]\nYou lose!" % num, to=message.getFrom())
###########################################################LATEST############################################################################### 
    def latest(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################

   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Latest mode!", to=message.getFrom())


###########################################################HAPPY############################################################################### 
    
    def happy(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Happy mode!", to=message.getFrom())

###########################################################MOTIVATIONAL############################################################################### 
  
    def motivational(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Motivational mode!", to=message.getFrom())

###########################################################LOVED############################################################################### 
  
    def loved(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Loved mode!", to=message.getFrom())
###########################################################SPIRITUAL############################################################################### 
  
    def spiritual(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Spiritual mode!", to=message.getFrom())
###########################################################ROMANTIC############################################################################### 
  
    def romantic(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Romantic mode!", to=message.getFrom())
###########################################################NAUGHTY############################################################################### 
  
    def naughty(self,message, match,to=None):
	global phone_no
	global device_id
	global ref_id
	global cursor
	global db
   	global mood_id
   	global user_id
	global quote	
	global start_id
	phone_no = message.getFrom()
	phone_no = phone_no.split("@")
	phone_no = phone_no[0]
	
#	phone_no = "919049433263"
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
#	self.image_sender.send_by_url(jid=message.getFrom(), file_url="http://www.w3schools.com/css/trolltunga.jpg")
	try:
   # Execute the SQL command
		global phone_no
		print "inside try0"
		cursor.execute("""SELECT user_id FROM user_bot WHERE phone_no = %s""",(phone_no,))
      # Execute the SQL command
   		if not cursor.rowcount:
			print "inside try0 in if"
#			global cursor
#			global phone_no
#			global device_id
#			global ref_id
			print phone_no
			print device_id
			ref_id = ''.join(random.choice('0123456789ABCDEF') for i in range(9))			
			print ref_id
			print user_id
        		print "No results found"
			
        		cursor.execute("""INSERT INTO user (device_id, notification_id,ref_code) VALUES (%s,%s,%s)""" , (device_id,phone_no,ref_id))
			db.commit()       		
			print user_id
			print source_id
			print "some"
        		user_id = cursor.lastrowid
			print "userid "
			print user_id
        		cursor.execute("""INSERT INTO user_bot(phone_no, user_id, source_id) VALUES(%s,%s,%s)""" ,(phone_no,user_id,source_id))
			db.commit()
			print "if ended"
   		else:
			print "inside try0 in else"
			global phone_no
        		results = cursor.fetchall()
   			for row in results:
   				print row[0]
   				print "done"
		print "inside try0 after if else"
   		cursor.execute("""SELECT MAX(start_id) FROM user_quote_mood WHERE user_id = %s AND mood_id = %s""",(user_id,mood_id,))
  		start_id = cursor.fetchall()
		print start_id
   		start_id = start_id[0][0]
		print "quote"
		print start_id
   		if start_id == None:
			print "test1"
   			print "quote is 0"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			start_id = 0
   			print "quote id is: " 
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test2"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)
   			quote = results[4][0]
        		start_id = start_id + 5
			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"
  		else:
   			print "quote is id"
			print "test11"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			mood_id = "1"
#############--------------------------------------------CHANGE MOOD ID HERE-----------------------------###############################
   			print "quote id is: " 
			print start_id
   			cursor.execute("""SELECT quote.quote_id, quote.quote_path FROM quote_mood INNER JOIN quote ON quote_mood.quote_id = quote.quote_id WHERE quote_mood.mood_id = %s LIMIT %s, 5""",(mood_id,start_id,))
   			print "test12"
   			results = cursor.fetchall()
   			print results
#   			im1 = results[0][1]
#   			im2 = results[1][1]
#   			im3 = results[2][1]
#   			im4 = results[3][1]   	
#   			im5 = results[4][1]
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im1)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im2)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im3)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im4)
			self.image_sender.send_by_url(jid=message.getFrom(), file_url=im5)

   			quote = results[4][0]
        		start_id = start_id + 5

			print "here is err"			
			print quote
  			cursor.execute("""INSERT INTO user_quote_mood(user_id, mood_id, quote_id, start_id) VALUES(%s,%s,%s,%s)""", (user_id,mood_id,quote,start_id))
			db.commit()
  			print "inserted"

      
	except:
   		print "Error: unable to fetch data"

	
	print phone_no[0]
	print "test"
    	return TextMessageProtocolEntity("Naughty mode!", to=message.getFrom())
############################################################################################################################################## 

    def help(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HELP_TEXT, to=message.getFrom())


HELP_TEXT = """ [HELP]
- Commands
WELCOME TO BREZIE
USE FOLLOWING COMMANDS TO GET YOUR QUOTES
/latest
/happy
/motivational
/spiritual
/romantic
/naughty
/loved
/about
/help - Show this message.

HAVE AWESOME DAY 
-BREZIE BOT

"""

ABOUT_TEXT = """ [Whatsapp Bot BREZIE]
A small effort to make your perfect day !
"""
