import discord, datetime, time
from discord.ext.commands import Bot
from discord.ext import commands
import time
import asyncio

bot = Bot(command_prefix='~')
TOKEN = '(insert token here)'


@bot.event
async def on_ready():
    print(f'Login successful as {bot.user}')

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game('Use ~help to see commands.'))

@bot.event
async def on_message(message):
  if message.content.startswith('~fuckoff'):
   await message.channel.send('<:fuckoff:791303665918279680>')

  ##if message.content.startswith('~disabled2'):
   #await message.channel.send('cock and cum <a:succanimated:585943845846646785>')

  if message.content.startswith('~milk'):
    await message.channel.send('Have some choccy milk,because you are epic.')

  if message.content.startswith('~timetest'):
    await message.channel.send('<a:succanimated:585943845846646785>')
    time.sleep(3)
    await message.channel.send('<:WoeIsYou:794710660478926908>')

  if message.content.startswith('~copypasta'):
    await message.channel.send('```Hello Meemie, \n \nXiphos is a big cunt. He makes fun of me and throws eggs at me until I´m forced to submit to his wishes. Meemie, I pray to you every day to no avail. Meemie, please answer my wishes; I´ve been a saint to those around me except Xiphos because Xiphos is a big cunt. \n \nMeemie, yesterday, I went to the store to buy a sola meme with my hard-earned money. I had struggled through winter, the snow-ladden streets a hellscape with an oil barrel fire and a raccoon as my only companions. Twice on a particularly windy and freezing Sunday did Xiphos try to steal my money because Xiphos is a big cunt. My only income was selling eggs on the street, eggs that the friendly big bouncy bird had given me; I did not eat them, for the money had to be saved for sola meme, and I do not eat eggs because I am not a big fucking cunt. \n \nIn the store, I felt the gazes of the other customers on me. Parents bustled around, purchasing the leather bound special edition of the Linux Programming Interface for their children. I scurried to the back of the store to find my latest hit of sola meme from the sola meme dealer. To my horror, Xiphos is a big cunt, and he stood on top of the sola meme dealer´s bloody corpse and a Greek xiphos in his hand. It was then, Meemie, that he focused his gaze on me, his empty eye sockets darker than the pit that his soul lay in. Meemie, I was scared because Xiphos is a big cunt. \n \nI´ve now found shelter under the rock roof of a raccoon´s rocket rack. As I eat my rice that´s grown rank, I rummage through my thoughts and seek to reign in the raging emotions, my hopes razed by the raid on my sola meme dealer. \n \nXiphos is a big cunt. \n \nYours truly, \n \nA secret admirer.```')

  #if message.content.startswith('@linux user'):
    #await message.channel.send('<@251828585516498945>')

  if message.content.startswith('~test'):
    await message.channel.send(':robot:')

  #if message.content.startswith('ugly ass'):
    #await message.channel.send('<@478306198513385492>')

  #if message.content.startswith('@nvidiots'):
    #await message.channel.send('<@791258874514112512>')

  if message.content.startswith('fatter fuck'):
    await message.channel.send('<@312574073869828096>')

  if message.content.startswith('fattest fuck'):
    await message.channel.send('<@526138306488959048>')

  if message.content.startswith('~cinnyroll'):
    await message.channel.send('Baking Cinny Roll...')
    time.sleep(2)
    await message.channel.send('Cinnamon Roll baked <:cinnyroll:804502941796139049>')

  if message.content.startswith('~pat desolate'):
    await message.channel.send('<a:desolatepat:779388806063325234>')

  if message.content.startswith('~pat pepega'):
    await message.channel.send('<a:patpega:791415508795654154>')

  if message.content.startswith('~pat weirdga'):
    await message.channel.send('<a:weirdpat:779390872839913472>')

  if message.content.startswith('~pat panzer'):
    await message.channel.send('<a:petzer:762399658282057778>')

  if message.content.startswith('~pat peepo'):
    await message.channel.send('<a:peepopat:759870492785508372>')

  if message.content.startswith('~pat lisa'):
    await message.channel.send('<a:lisapat:791419602491015188>')

  if message.content.startswith('~pat lfg'):
    await message.channel.send('<a:letsfuckingpat:791420442173898752>')

  if message.content.startswith('~pat troll'):
    await message.channel.send('<a:trollpat:791424971989450764>')

  if message.content.startswith('~pat succ'):
    await message.channel.send('<a:succpat:791424972434046997>')

  if message.content.startswith('fat fuck'):
    await message.channel.send('<@!219392891905114112>')

  #if message.content.startswith('~kspin'):
    #await message.channel.send('<a:kirbySpin:753653606716145685>')

  if message.content.startswith('~kfspin'):
    await message.channel.send('<a:kirbysf:794706639139373127>')

  if message.content.startswith('~krspin'):
    await message.channel.send('<a:kirbysrfast:794708050602098719>')

  if message.content.startswith('~motivation'):
    await message.channel.send('https://www.brainyquote.com/quote_of_the_day')

  if message.content.startswith('~nsfw'):
    await message.channel.send('||No NSFW in this Christian Discord Server you <:horny:714885946763509831>.||')

  if message.content.startswith('~help'):
    embed = discord.Embed(title="Choccy Boi help function", description="List of usable commands(prefix ~(tilde)):", color=0x83B5E3)
    embed.add_field(name="milk", value="Will give you Choccy Milk.", inline=True)
    embed.add_field(name="test", value='Will test if the bot is working showing the :robot: emote.', inline=True)
    embed.add_field(name="cinnyroll", value='Bakes a Cinnamon Roll', inline=True)
    #embed.add_field(name="kspin", value='Spin Kirb <a:kirbySpin:753653606716145685> ', inline=True)
    embed.add_field(name="kfspin", value='Spinny Kirb <a:kirbysf:794706639139373127> ', inline=True)
    embed.add_field(name="krspin", value='Spinnier Kirb <a:kirbysrfast:794708050602098719> ', inline=True)
    embed.add_field(name='pat', value='Pats an emote.', inline=True)
    embed.add_field(name='nsfw', value='Has a ||0%|| chance to show you NSFW.', inline=True)
    embed.add_field(name='motivation', value='Shows a website for inspirational quotes.', inline=True)
    embed.add_field(name='pls fortnite', value='Substitutes Dank Memer´s original command(no ~).', inline=True)
    embed.add_field(name='owo/OwO/pls owo', value='Makes the bot mad,please don´t use it(no ~).', inline=True)
    embed.add_field(name='dcxd', value='Dead Chat XD.', inline=True)
    embed.add_field(name='asktoriel', value='Ask Toriel<:toriel:791404835589062727> for a Pie.', inline=True)
    #embed.add_field(name='ping', value='~~pings new role~~ Disabled until further notice.', inline=True)
    #embed.add_field(name='skpls', value='<a:skelepls:552650569135816720>', inline=True)
    embed.add_field(name='scp', value='Shows a link to a SCP concept based on r/AyyMD.', inline=True)
    embed.add_field(name='help', value="will give you the Choccy Boi's command list", inline=False)
    await message.channel.send(embed=embed)

  #if message.content.startswith('~disabled yee'):
    #await message.channel.send('no it´s mine <:gunr:753982079670419456>')

  if message.content.startswith('pls owo'):
    await message.channel.send('***NO OWOING***')

  if message.content.startswith('~asktoriel'):
    await message.channel.send('Hello my child,I´m cooking a Pie,do you want Butterscotch(~bst) or Cinnamon(~cin)? <:toriel:791404835589062727>')

  if message.content.startswith('~bst'):
    await message.channel.send('Here my child,have a Butterscotch Pie \nhttps://toriavey.com/images/2016/01/IMG_6437-2.jpg')

  if message.content.startswith('~ciny'):
    await message.channel.send('Here my child,have a Cinnamon Pie \nhttps://cdn.greatlifepublishing.net/wp-content/uploads/sites/2/2018/11/22012318/Cinnamon-Pie-Horizontal-OG-2.jpg')

  if message.content.startswith('~cboth'):
    await message.channel.send('Here my child,have a Butterscotch-Cinnamon Pie \nhttps://64.media.tumblr.com/95eca899f0b01f98c53b4854445ea84e/tumblr_inline_nvg3alCRGL1trnyzt_1280.jpg')

  if message.content.startswith('~aglogi'):
    await message.channel.send('You drank <:glogi:606156337566711830> and fainted...')
    time.sleep(2)
    await message.channel.send('\nYou woke up in Finland :flag_fi:.')

  if message.content.startswith('OwO'):
    await message.channel.send('***NO OWOING***')

  if message.content.startswith('owo'):
    await message.channel.send('***NO OWOING***')

  if message.content.startswith('~scp'):
    await message.channel.send('http://scp-sandbox-3.wikidot.com/ayymd')

   if message.content.startswith('~pound MrAss'):
    await message.channel.send('<@!682224399482748953> got pounded by a horse <a:succanimated:585943845846646785>')

  if message.content.startswith('~dcxd'):
    await message.channel.send('https://tenor.com/view/dead-chat-dead-discord-death-gif-18239566')

  if message.content.startswith('~cheese'):
    await message.channel.send('Sometimes, I dream about :cheese:')

  if message.content.startswith('stfu'):
    await message.channel.send('<a:nou_neon:470036539976712194>')

  #if message.content.startswith('~disabledshit'):
    #await message.channel.send('<@&774318842859880548>')
    #time.sleep(1)
    #await message.channel.send('<@&774318842859880548>')
    #time.sleep(1)
    #await message.channel.send('<@&774318842859880548>')
    #time.sleep(1)
    #await message.channel.send('<@&774318842859880548>')
    #time.sleep(1)
    #await message.channel.send('<@&774318842859880548>')
    #time.sleep(1)
    #await message.channel.send('<@&774318842859880548>')

  if message.content.startswith('~insult'):
    await message.channel.send('<@&774318842859880548> is a nigga-ass coward')

  if message.content.startswith('i am going to sleep'):
    await message.channel.send('me too <:cheemssleep:753357088788578374>')

  if message.content.startswith('~credits'):
    await message.channel.send('Coders: \n@tiypo#3141 \n@An12854#6583 \n@Jyrka98#1337 \n@Simply.png#6722 \nOther thanks: \n@anx#6875 ')

  if message.content.startswith('~skpls'):
    await message.channel.send('<a:skelepls:552650569135816720>')
    

bot.run('(insert token here)')
