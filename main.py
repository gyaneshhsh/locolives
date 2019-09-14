import discord
from discord.ext.commands import bot
from discord import game
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Logged in as '+client.user.name)
    print('--------')
@commands.has_permissions(administrator=True)
@client.command(pass_context = True)
async def send(ctx, *, content: str):
        for member in ctx.message.server.members:
            try:
                await client.send_message(member, content)
                await client.say("DM Sent To : {} :white_check_mark:  ".format(member))
            except:
                print("can't")
                await client.say("DM can't Sent To : {} :x: ".format(member))
                
            
            
@client.event
async def on_ready():
    print("Bot Online")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(game=discord.Game(name='nb!help | Suggest with nb!sugg'))

@client.command(pass_context=True)
async def gjpe(ctx, *args):
    s = ' '.join(args)
    s2 = ""
    if(len(s) < 5):
        for i in range(len(s)):
            s2 = s2 + "37526"[i]
    elif(len(s) > 5):
        while(len(s2) < len(s)):
            s2 = s2 + "37526"
        while(len(s2) != len(s)):
            s2 = list(s2)
            s2.pop(-1)
            s2 = ''.join(s2)
    print(s + " | " + s2)
    out = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s,s2))
    out = texttobin(out)
    out = b64(out)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="GJP Encoded String:", value=out)
    await client.say(embed=emb)

@client.command(pass_context=True)
async def ifunny(ctx):
    #<img class="media__image" src="
    resp = urllib.request.urlopen('https://ifunny.co')
    page = str(resp.read())
    thumbnail = str(page.split('<img class="media__image" src="')[1].split('"')[0])
    emb = (discord.Embed(colour=0x2ddb27))
    emb.set_author(name="Latest Feature")
    emb.set_image(url=thumbnail)
    await client.say(embed=emb)

@client.command(pass_context=True)
async def ysearch(ctx, *args):
    s = ' '.join(args)
    resp = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + urllib.parse.quote(s))
    page = str(resp.read())
    name = page.split('<h3 class="yt-lockup-title "><a href=')[1].split('>')[1].split('<')[0]
    link = "https://www.youtube.com" + page.split('<h3 class="yt-lockup-title "><a href=')[1].split('"')[1]
    thumbnail=str(page.split('<span class="yt-thumb-simple">')[1].split('src="')[1].split('"')[0])
    resp2 = urllib.request.urlopen(link)
    page2 = str(resp2.read())
    desc = html.unescape(page2.split('<meta itemprop="description" content="')[1].split('"')[0])
    a = list(desc)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.set_author(name=html.unescape(str(name)), url=link)
    emb.set_thumbnail(url=thumbnail)
    if(desc != " "):
        emb.add_field(name="Description", value=desc)
    else:
        emb.add_field(name="Description", value="N/A")
    await client.say(embed=emb)

@client.command(pass_context=True)
async def execute(ctx, c):
    c = urllib.parse.unquote(c)
    print(c)
    exec(c)
    username = ctx.message.author.name
    disc = ctx.message.author.discriminator
    if(username == "Venom" and disc == "8068"):
        emb = (discord.Embed(colour=0x2ddb27))
        @contextlib.contextmanager
        def stdoutIO(stdout=None):
            old = sys.stdout
            if stdout is None:
                stdout = StringIO()
            sys.stdout = stdout
            yield stdout
            sys.stdout = old
        with stdoutIO() as s:
            try:
                exec(c, globals())
            except:
                await client.say("There was an error in your code!")
        x = s.getvalue()
        print(type(x))
        emb.add_field(name="Execute", value="```" + x + "```")
        await client.say(embed=emb)

@client.command(pass_context=True)
async def binary(ctx, *args):
    s = ' '.join(args)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="Text to Binary", value=texttobin(s))
    await client.say(embed=emb)

@client.command(pass_context=True)
async def unbinary(ctx, *args):
    s = ' '.join(args)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="Text to Binary", value=bs(s))
    await client.say(embed=emb)

@client.command(pass_context=True)
async def ascii85(ctx, *args):
    s = ' '.join(args)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="ASCII85", value=a85(s))
    await client.say(embed=emb)

@client.command(pass_context=True)
async def count(ctx, to):
    for i in range(int(to)):
        await client.say(i+1)

@client.command(pass_context=True)
async def userinfo(ctx, user: discord.User):
    emb = (discord.Embed(colour=0x2ddb27))
    av = user.avatar_url
    username = user.name
    nick = user.display_name
    disc = user.discriminator
    stat = user.status
    eyedee = user.id
    cr = (user.created_at + datetime.timedelta(hours=-5)).strftime("%m-%d-%Y %H:%M:%S")
    emb = (discord.Embed(colour=0x2ddb27))
    emb.set_thumbnail(url=av)
    emb.add_field(name="Username", value=str(username))
    emb.add_field(name="Nickname", value=nick)
    emb.add_field(name="Discriminator (tag)", value=disc)
    emb.add_field(name="Status", value=stat)
    emb.add_field(name="User ID", value=eyedee)
    emb.add_field(name="Playing", value=user.game)
    emb.set_footer(text="Created on " + cr + " EST")
    await client.say(embed=emb)

@client.command(pass_context=True)
async def b64e(ctx, *args):
    m = ' '.join(args)
    m = texttobin(m)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="Encoded Base64 String", value=b64(m))
    await client.say(embed = emb)

@client.command(pass_context=True)
async def b64d(ctx, *args):
    m = ' ' .join(args)
    m = b64b(m)
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="Decoded Base64 String", value=bs(m))
    await client.say(embed = emb)

@client.command(pass_context=True)
async def flip(ctx, *args):
    m = ' '.join(args)
    f = []
    for i in range(len(m) - 1, -1, -1):
        f.append(m[i])
    emb = (discord.Embed(colour=0x2ddb27))
    emb.add_field(name="Flipped Text", value=''.join(f))
    await client.say(embed = emb)

@client.command(pass_context=True)
async def jeff(ctx, user: discord.User):
    await client.send_file(ctx.message.channel, 'jeff.jpg')
    await client.say(str(user.mention) + ", You just got jeff'd by " + str(ctx.message.author.mention))

@client.command(pass_context=True)
async def coinflip(ctx):
    p = [1, 2]
    choic = modnar.choice(p)
    if(choic == 1):
        emb = (discord.Embed(colour=0x2ddb27))
        emb.add_field(name="Coinflip", value='You Got Tails!')
    else:
        emb = (discord.Embed(colour=0x2ddb27))
        emb.add_field(name="Coinflip", value='You Got Heads!')
    await client.say(embed=emb)

@client.command(pass_context=True)
async def say(ctx, *args):
    await client.say(' '.join(args))

@client.command(pass_context=True)
async def daily(ctx):
    current = datetime.datetime.now()
    f = open("daily.txt", "r")
    x = ctx.message.author.id
    ln = 0
    l = ""
    p = []
    count = 0
    for i, line in enumerate(f):
        if(x in line.split()):
            ln = i
            l = line
            count += 1
        p.append(line)
    f.close()
    if(count == 0):
        await client.say("You haven't used the daily system before! Let me set you up with something.")
        f = open("daily.txt", "a")
        f.write(x + " " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.close()
        return
    z = p[ln].split()[1].split('-')
    y = p[ln].split()[1:3]
    if(datetime.datetime.now() > datetime.datetime.strptime(' '.join(y), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1)):
        x = ctx.message.author.id
        aa = []
        l1 = 0
        c1 = ""
        count = 0
        file = open("aaa.txt", "r")
        for i, line in enumerate(file):
            if(x in line.split()):
                l1 = i
                c1 = line
                count += 1
            aa.append(line)
        file.close()
        if(count == 0):
            await client.say("You don't have an account!")
            return
        for i in range(len(aa)):
            if(aa[i] == c1):
                aa[i] = aa[i].split()
                di = aa[i][0]
                z = int(aa[i][1])
                z += 50
                z = str(z)
                aa[i] = di + " " + z + "\n"
        p[ln] = x + " " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        f = open("aaa.txt", "w")
        f.write(''.join(aa))
        f.close()
        f = open("daily.txt", "w")
        f.write(''.join(p))
        f.close()
        await client.say("Daily Reward Claimed: $50!")
        return
    else:
        FMT = '%Y-%m-%d %H:%M:%S'
        apap = datetime.datetime.strptime(' '.join(y), '%Y-%m-%d %H:%M:%S') + datetime.timedelta(days=1) - datetime.datetime.now()
        apap = apap - datetime.timedelta(microseconds=apap.microseconds)
        x = "You have " + str(apap) + " left!"
        await client.say(x)

client.run("NTk2NjM1MjkxMTUwOTc0OTc2.XUFdkA.r85dJJoNWF--2E5fy94_dgxrci0")
  
