import discord
from discord.ext import commands
from youtubesearchpython import VideosSearch
from youtube_transcript_api import YouTubeTranscriptApi
import asyncio
import yt_dlp
import random
import json

with open("secret.json", 'r') as file:
    token = json.loads(file.read())["TOKEN"]

# add to server: https://discordapp.com/oauth2/authorize?client_id=893919853004603504&scope=bot&permissions=0

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='$', case_insensitive=True, activity=discord.Game(name="$play"), intents=intents)

ERROR_COLOUR = (255, 85, 85)
SUCCESS_COLOUR = (85, 255, 85)
INFO_COLOUR = (85, 255, 255)

special_people = [326116423556530187, 222478939287846913, 544682078508154910, 512001382522290198]
loop_song = {}
song_queue = {}
current_song = {}
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': "FFmpegExtractAudio",
        'preferredcodec': "mp3",
        'preferredquality': '192'
    }]
}


ffmpeg_options = {
    'options': '-vn',
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5"
}


def get_video_data(search):
    video = VideosSearch(search, 1)
    video_data = video.result()['result']
    if video_data:
        return video_data[0]
    else:
        return False


def get_mp3(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(url, download=False)
        except yt_dlp.DownloadError as e:
            return False, e
        song_url = info['url']
    return song_url


def create_embed(title, value, colour):
    embed = discord.Embed(color=discord.Colour.from_rgb(colour[0], colour[1], colour[2]))
    embed.add_field(name=title, value=value, inline=False)
    return embed


def invalid_command(proper, arguments):
    return create_embed(":x: Invalid command usage! :x:",
                        f"Try using it like:\n`{proper}`\n\nArguments:\n" + "\n".join(arguments),
                        ERROR_COLOUR)


def get_channel(ctx, number):
    channels = [c for c in ctx.message.guild.channels if c.type == discord.ChannelType.voice]
    for channel in channels:
        print(channel.position)
        if str(channel.position + 1) == number:
            return channel

    return None


def song_not_found(ctx):
    ctx.message.send(embed=create_embed(":x: SONG NOT FOUND :x:",
                                        "Youtube servers are either broken, or your search request is too obscure",
                                        INFO_COLOUR))


def play_next(ctx, voice_client):
    if len(song_queue[ctx.guild.id]) >= 1:
        current_song[ctx.guild.id] = song_queue[ctx.guild.id][0]["id"]
        url = "https://www.youtube.com/watch?v=" + current_song[ctx.guild.id]
        if ctx.guild.id in loop_song:
            if not loop_song[ctx.guild.id]:
                song_queue[ctx.guild.id].pop(0)
        else:
            song_queue[ctx.guild.id].pop(0)
        song_data = get_mp3(url)
        if len(song_data) == 2:
            if song_data[1].args[0].startswith("ERROR: Sign in to confirm your age"):
                asyncio.run_coroutine_threadsafe(ctx.send(embed=create_embed(":x: VIDEO IS AGE RESTRICTED :x:",
                                                                             "The youtube API cannot download age restricted videos!.",
                                                                             ERROR_COLOUR)), bot.loop)
            else:
                asyncio.run_coroutine_threadsafe(ctx.send(embed=create_embed(":x: API OUT OF DATE :x:",
                                                                             "Some songs will be unable to play until the API is updated.",
                                                                             ERROR_COLOUR)), bot.loop)
                asyncio.run_coroutine_threadsafe(
                    bot.get_user(326116423556530187).send("Please update the youtube-dl module on heroku"), bot.loop)
            return False
        voice_client.play(discord.FFmpegPCMAudio(song_data, **ffmpeg_options),
                          after=lambda e: play_next(ctx, voice_client))
    else:
        song_queue[ctx.guild.id] = []
        current_song[ctx.guild.id] = []


@commands.Cog.listener()
async def on_voice_state_update(self, member, before, after):
    if not member.id == self.bot.user.id:
        return
    if before.channel is None:
        voice = after.channel.guild.voice_client
        time = 0
        while True:
            await asyncio.sleep(1)
            time += 1
            if voice.is_playing() and not voice.is_paused():
                time = 0
            if time == 60 * 5:
                await voice.disconnect()
            if not voice.is_connected():
                break


@bot.command(pass_context=True)
async def loop(ctx):
    global loop_song

    if ctx.guild.id not in loop_song:
        loop_song[ctx.guild.id] = False

    loop_song[ctx.guild.id] = not loop_song[ctx.guild.id]
    change = ":recycle: Looping is now enabled :recycle:"
    if not loop_song[ctx.guild.id]:
        change = ":frog: Looping is now disabled :frog:"
    await ctx.send(embed=create_embed(change,
                                      "Use the `$loop` command to toggle looping",
                                      INFO_COLOUR))


@bot.command(pass_context=True)
async def shuffle(ctx):
    shuffled = random.shuffle(song_queue[ctx.guild.id])
    if shuffled is not None:
        song_queue[ctx.guild.id] = shuffled
    await ctx.send(embed=create_embed(":twisted_rightwards_arrows: Queue Shuffled :twisted_rightwards_arrows:",
                                      "ONG THE QUEUE WAS SHYUFEAD",
                                      SUCCESS_COLOUR))


@bot.command(pass_context=True, aliases=['yodropthelines', 'yodroptheline', 'l'])
async def lyrics(ctx):
    print('step 1')
    if ctx.guild.id in current_song:
        print('step 2')
        if len(current_song[ctx.guild.id]) > 0:
            try:
                transcript = YouTubeTranscriptApi.get_transcript(current_song[ctx.guild.id])
            except:
                await ctx.send(embed=create_embed(":x: Failed to Find Lyrics :x:",
                                                  "i guess you're gonna have to google it",
                                                  ERROR_COLOUR))
                return

            string_lyrics = []
            for lyric in transcript:
                string_lyrics += lyric["text"] + '\n'

            final_lyrics = [string_lyrics[start:start + 5500] for start in range(0, len(string_lyrics), 5500)]
            for lyric in final_lyrics:
                await ctx.send(embed=create_embed("Lyrics", "".join(lyric), INFO_COLOUR))


@bot.command(pass_context=True, aliases=['q'])
async def queue(ctx):
    queue_list = []
    if ctx.guild.id not in song_queue:
        queue_list.append("There are no songs queued right now.")
    else:
        for x, item in enumerate(song_queue[ctx.guild.id]):
            queue_list.append(f"**{x + 1}.** " + item["title"])
        if len(queue_list) <= 0:
            queue_list.append("There are no songs queued right now.")
    await ctx.send(embed=create_embed(":newspaper: Queued Songs :newspaper:",
                                      "\n".join(queue_list),
                                      INFO_COLOUR))


@bot.command(pass_context=True, aliases=['s', 'fs', 'next'])
async def skip(ctx):
    global loop_song
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client.is_playing():
        voice_client.stop()
        loop_song[ctx.guild.id] = False
        await ctx.send(embed=create_embed(":fast_forward: Skipping Song... :fast_forward:",
                                          "Use the `$play` command to add another song to the queue!",
                                          INFO_COLOUR))
    else:
        await ctx.send(embed=create_embed(":x: No songs are playing right now! :x:",
                                          "Use the `$play` command to play a song!",
                                          ERROR_COLOUR))


@bot.command(pass_context=True, aliases=['leave', 'd', 'dis'])
async def disconnect(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    await voice_client.disconnect()
    await ctx.send(embed=create_embed(":white_check_mark: Successfully disconnected from channel :white_check_mark:",
                                      "Use the `$play` command to add me back!",
                                      SUCCESS_COLOUR))


@bot.command(pass_context=True, aliases=['p'])
async def play(ctx, *args):
    sender = await ctx.guild.fetch_member(ctx.message.author.id)

    if len(args) < 1:
        await ctx.send(embed=invalid_command("$play (song)", ["`song`: Name or keywords of a song/video"]))
        return

    if sender.voice is None:
        await ctx.send(embed=create_embed(":x: You must be in a voice channel to use this command! :x:",
                                          "Please join a voice channel and try again.",
                                          ERROR_COLOUR))
        return

    data = get_video_data(' '.join(args))

    if not data:
        await ctx.send(embed=create_embed(":x: SONG NOT FOUND :x:",
                                          "Youtube servers are either broken, or your search request is too obscure",
                                          ERROR_COLOUR))
        return

    if ctx.guild.voice_client not in bot.voice_clients:
        channel = sender.voice.channel
        song_queue[ctx.guild.id] = []
        await channel.connect()

    song_queue[ctx.guild.id].append(data)
    url = "https://www.youtube.com/watch?v=" + data["id"]

    await ctx.send(embed=create_embed(":white_check_mark: Added `" + data["title"] + "` by `" + data["channel"][
        "name"] + "` to the queue :white_check_mark:",
                                      url + "\nUse the `$skip` command skip through the queue!",
                                      SUCCESS_COLOUR))

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice_client.is_playing():
        play_next(ctx, voice_client)


bot.run(token)
