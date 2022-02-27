from javascript import require, On, Once, AsyncTask, once, off
import time
import os
import random
#information on server and bot
mineflayer = require('mineflayer')
BOT_USERNAME="wullieBot"
bot = mineflayer.createBot({ 'host': '1b1t.me', 'port': 25565, 'username': BOT_USERNAME, 'hideErrors': False })
Login = False

#using other bots for warps and shit
Summon = 'cd bots && python3 niggerBot.py'
Spy = 'cd bots && python3 spy.py '
StashBot = 'cd bots && python3 stashBot.py'


@On(bot, 'chat',)
def onChat(this, user, message, task, *rest):
	if '/register' in message:
		bot.chat('/register Linux Linux')
	#login and chat log, login requied on some server custom password are recomended 
	if '/login' in message:
		Login = True
		bot.chat('/login ')
		time.sleep(2)
		Login = False
		
	#chat
	print(f'{user} said "{message}"')
	
	
	#commands for wullieBot most only work on 1b1t.me
	if '%help' in message:
		bot.chat('commands, %report, %penis, %hentai, %co-ords, %imHorny, %ip, %pt, %ping, %tps, %niggerBot, %boobs, %nword, %noword, %yesword, %lolliPorn %summon')
			
	if '%report' in message:
		bot.chat('fuck you')
	if '%penis' in message:
		bot.chat('8================D')
	if '%hentai' in message:
		bot.chat('get a life')
	if '%co-ords' in message:
		bot.chat('no im at base')
	if '%imHorny' in message:
		bot.chat('get a life')
	if '%ip' in message:
		bot.chat('127.0.0.1')
	if '%pt' in message:
		bot.chat('!pt wullieBot')
	if '%ping' in message:
		bot.chat('!ping' + {user})
	if '%tps' in message:
		bot.chat('idk press tab, if tps is below 5 blame spyrow')
	if '%niggerBot' in message:
		bot.chat('!nword niggerBot')
	if '%boobs' in message:
		bot.chat('(.) (.)')
	if '%nword' in message:
		bot.chat('nigger')
	if '%noword' in message:
		bot.chat('no')
	if '%yesword' in message:
		bot.chat('yes')
	if '%lolliPorn' in message:
		bot.chat('this interaction has been reported to Scotland yard')
	
	#runs stashbot for exbase members and jq	
	@AsyncTask(start=True)
	def  breakListener(task):
		if '%stash' in message:
			bot.chat('brining stashBot online use %stop before adding another bot')
			os.system(StashBot)
			
	
	
	#runs spy for exbase members and jq
	@AsyncTask(start=True)
	def handleMsg(task):
		if '%station' in message:
			bot.chat('brining spy online use %stop before adding another bot')
			os.system(Spy)
		
	#summons niggerBot
	@AsyncTask(start=True)
	def break_block(task):
		if '%summon' in message:
			bot.chat('I summon you niggerBot to forfill your oath')
			os.system(Summon)
		
	#tp players to dupe stash designd for 1b1.me
	@AsyncTask(start=True)
	def onChat(task):
		while True:
			time.sleep(2)
			bot.chat('/tpy wullie')
			time.sleep(2.5)
			bot.chat('/tpy chmoka90')
			time.sleep(2.5)   
			bot.chat('/tpy RealSteak')
			time.sleep(2.5)
			bot.chat('/tpy Mr_Trebor')
			time.sleep(2.5)
			bot.chat('/tpy _Smertushka_')
			time.sleep(2.5)
			bot.chat('/tpy MulfoK')
			time.sleep(2.5)	    
			bot.chat('/tpy jaya_97')
			time.sleep(2.5)
			bot.chat('/tpy jqjj')
			time.sleep(2.5)
			bot.chat('/tpy SpyrowGr')
			time.sleep(2)
			
