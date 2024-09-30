lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll, lllllllllllIllI, lllllllllllIlIl, lllllllllllIlII, lllllllllllIIll = bytes, bool, print, ValueError, float, open, int, Exception, isinstance, map, str, enumerate, getattr

from discord.ui import Button as IIlIIIIIIllllI, View as IlIIlllIlIlllI, Modal as lIIIlIIIIIIllI, button as lIIIlIlllIIIll, TextInput as IllIIIlIIlIIIl
from discord import Interaction as IIllIlIIIlIlII
from discord.ButtonStyle import red as llIlllIllIlIIl, blurple as lIIIIIIIIlIlIl, green as IlIlIIlIIIIIII, grey as IlIIIlllllllll
from discord.TextStyle import short as lIIIllllIIIIll
from wavelink.YouTubeTrack import search as IllIllllllIIIl
from json import load as lIIIIllIIIllIl
from wavelink.NodePool import get_node as lllIIllllIIlII, create_node as lllIIllIIIIIlI
from asyncio import sleep as lIlIllIIIllllI
from wavelink import LavalinkException as IIllIlllIlIIIl, Vibrato as IllIIlIIllIIII, Rotation as llllIIlIIllIII, LowPass as lllIlllllIlIIl, Karaoke as IIllIlIlIlIllI, Distortion as lllIlllIlIllIl, Equalizer as lIIIlIlIIIllll, ChannelMix as lIIIIlIllIlllI, Tremolo as llIIIllllIIIlI, Player as lIlllIlIlIIllI, Timescale as IIIlIllIIIllIl
from random import choice as lllIIIlIIIlIlI
from discord.ext import commands as IlIlIIIllIIIll

class lIllllllllIlIIIIIl(IlIIlllIlIlllI):

    def __init__(IlIIIIlIIIlllllIIl, lIIIIIIIIllIIlIllI, lllIIIllllIlIIlIlI):
        super().__init__(timeout=None)
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI = lIIIIIIIIllIIlIllI
        IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI = lllIIIllllIlIIlIlI

    @IllIIlIIllIlllIllI(label='Add to Playlist', style=IlIlIIlIIIIIII)
    async def llIIllllIlIlIlIlIl(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        lIllIIIlIlIIIlllII = lIllIlIIIIIlIIIlll(IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI)
        await llIllllIlIIIIIlIIl.response.send_modal(lIllIIIlIlIIIlllII)

    @IllIIlIIllIlllIllI(label='View Playlist', style=lIIIIIIIIlIlIl)
    async def lllllllIllIlIIIIlI(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        IllIlllIIIlIIlIIll = lllllllllllIIll('\n', lllllllllllIIll(lllllllllllllll, 'fromhex')('6a6f696e').decode())([f'{i + 1}. {IlIIIIIlIIIIIIllII.title}' for (i, IlIIIIIlIIIIIIllII) in lllllllllllIlII(IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI)])
        await llIllllIlIIIIIlIIl.response.send_message(f'Current Playlist:\n{IllIlllIIIlIIlIIll}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

class lIllIlIIIIIlIIIlll(lIIIlIIIIIIllI, title='Add to Playlist'):

    def __init__(IlIIIIlIIIlllllIIl, lllIIIllllIlIIlIlI):
        super().__init__()
        IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI = lllIIIllllIlIIlIlI
    llIIllIIllIllllIll = IllIIIlIIlIIIl(label='Song URL or Search Query', style=lIIIllllIIIIll)

    async def IlIIIIIIIlIlIlIIll(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII):
        lllllIIIllIIIIllIl = IlIIIIlIIIlllllIIl.llIIllIIllIllllIll.value
        try:
            IllllIllIlIllIlIIl = await IllIllllllIIIl(lllllIIIllIIIIllIl)
            if IllllIllIlIllIlIIl:
                lllllllllllIIll(IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI, lllllllllllIIll(lllllllllllllll, 'fromhex')('617070656e64').decode())(IllllIllIlIllIlIIl[0])
                await llIllllIlIIIIIlIIl.response.send_message(f'Added {IllllIllIlIllIlIIl[0].title} to the playlist!', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
            else:
                await llIllllIlIIIIIlIIl.response.send_message('No tracks found for the given query.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        except llllllllllllIII as lIllIllIlIIlIIIlII:
            await llIllllIlIIIIIlIIl.response.send_message(f'An error occurred: {lllllllllllIlIl(lIllIllIlIIlIIIlII)}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

class IIIIlllIllllIIIlIl(IlIIlllIlIlllI):

    def __init__(IlIIIIlIIIlllllIIl, lIIIIIIIIllIIlIllI, lllIIIllllIlIIlIlI):
        super().__init__(timeout=None)
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI = lIIIIIIIIllIIlIllI
        IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI = lllIIIllllIlIIlIlI

    @IllIIlIIllIlllIllI(label='⏸️', style=IlIIIlllllllll)
    async def IIIIIIIIIlIIlIlllI(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        if not llIllllIlIIIIIlIIl.guild.voice_client or not llIllllIlIIIIIlIIl.guild.voice_client.is_playing():
            return await llIllllIlIIIIIlIIl.response.send_message('Nothing is playing.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        await llIllllIlIIIIIlIIl.guild.voice_client.pause()
        await llIllllIlIIIIIlIIl.response.send_message('Paused the current song.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @IllIIlIIllIlllIllI(label='▶️', style=IlIIIlllllllll)
    async def lllIlllIlIIIllllII(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        if not llIllllIlIIIIIlIIl.guild.voice_client or not llIllllIlIIIIIlIIl.guild.voice_client.is_paused():
            return await llIllllIlIIIIIlIIl.response.send_message('Nothing is paused.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        await llIllllIlIIIIIlIIl.guild.voice_client.resume()
        await llIllllIlIIIIIlIIl.response.send_message('Resumed the current song.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @IllIIlIIllIlllIllI(label='⏭️', style=IlIIIlllllllll)
    async def IlllllIIIIllIIlllI(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        if not llIllllIlIIIIIlIIl.guild.voice_client or not llIllllIlIIIIIlIIl.guild.voice_client.is_playing():
            return await llIllllIlIIIIIlIIl.response.send_message('Nothing is playing.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        await llIllllIlIIIIIlIIl.guild.voice_client.stop()
        if IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI:
            lIlIIlIlIIIlllllII = lllllllllllIIll(IlIIIIlIIIlllllIIl.lllIIIllllIlIIlIlI, lllllllllllIIll(lllllllllllllll, 'fromhex')('706f70').decode())(0)
            await llIllllIlIIIIIlIIl.guild.voice_client.lIlIIIlIIlIllIIllI(lIlIIlIlIIIlllllII)
            await llIllllIlIIIIIlIIl.response.send_message(f'Skipped to next song: {lIlIIlIlIIIlllllII.title}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        else:
            await llIllllIlIIIIIlIIl.response.send_message('Skipped the current song. Playlist is empty.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @IllIIlIIllIlllIllI(label='⏹️', style=llIlllIllIlIIl)
    async def IlIIlllIlIlIIllllI(IlIIIIlIIIlllllIIl, llIllllIlIIIIIlIIl: IIllIlIIIlIlII, IllIIlIIllIlllIllI: IIlIIIIIIllllI):
        if not llIllllIlIIIIIlIIl.guild.voice_client:
            return await llIllllIlIIIIIlIIl.response.send_message('Not connected to a voice channel.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        await llIllllIlIIIIIlIIl.guild.voice_client.disconnect()
        await llIllllIlIIIIIlIIl.response.send_message('Disconnected from the voice channel.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

class IIllllIlIIlllIIIlI(IlIlIIIllIIIll.Cog):

    def __init__(IlIIIIlIIIlllllIIl, lIIIIIIIIllIIlIllI):
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI = lIIIIIIIIllIIlIllI
        IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI = {}
        IlIIIIlIIIlllllIIl.lIlIIlllIIIlllllII = IlIIIIlIIIlllllIIl.IllIllIIIIllIIIIlI()
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI.loop.create_task(IlIIIIlIIIlllllIIl.IlllIIIIlIIlIIlIIl())
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI.loop.create_task(IlIIIIlIIIlllllIIl.llIIIIlIIlIlIllllI())

    def IllIllIIIIllIIIIlI(IlIIIIlIIIlllllIIl):
        with llllllllllllIlI('lavalink_servers.json', 'r') as IIllllIllIIIlIIIII:
            return lIIIIllIIIllIl(IIllllIllIIIlIIIII)['servers']

    async def IlllIIIIlIIlIIlIIl(IlIIIIlIIIlllllIIl):
        await IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI.wait_until_ready()
        for IlllIIlIIIllIllIlI in IlIIIIlIIIlllllIIl.lIlIIlllIIIlllllII:
            try:
                await lllIIllIIIIIlI(bot=IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI, identifier=IlllIIlIIIllIllIlI['identifier'], host=IlllIIlIIIllIllIlI['host'], port=IlllIIlIIIllIllIlI['port'], password=IlllIIlIIIllIllIlI['password'])
                lllllllllllllIl(f"Successfully connected to Lavalink server: {IlllIIlIIIllIllIlI['identifier']}")
                return
            except llllllllllllIII as lIllIllIlIIlIIIlII:
                lllllllllllllIl(f"Failed to connect to Lavalink server {IlllIIlIIIllIllIlI['identifier']}: {lIllIllIlIIlIIIlII}")
        lllllllllllllIl('Failed to connect to any Lavalink server.')

    async def llIIIIlIIlIlIllllI(IlIIIIlIIIlllllIIl):
        while llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
            await lIlIllIIIllllI(300)
            await IlIIIIlIIIlllllIIl.lIllIIlllIIlllllII()

    async def lIllIIlllIIlllllII(IlIIIIlIIIlllllIIl):
        lIlIIlIllIIIIIIIll = lllIIllllIIlII()
        if not lIlIIlIllIIIIIIIll or not lIlIIlIllIIIIIIIll.is_connected():
            lllllllllllllIl('Current node is unavailable. Attempting to connect to a different node.')
            await IlIIIIlIIIlllllIIl.IlllIIIIlIIlIIlIIl()
        else:
            try:
                await IllIllllllIIIl('test')
                lllllllllllllIl(f'Health check passed for node: {lIlIIlIllIIIIIIIll.identifier}')
            except llllllllllllIII as lIllIllIlIIlIIIlII:
                lllllllllllllIl(f'Health check failed for node {lIlIIlIllIIIIIIIll.identifier}: {lIllIllIlIIlIIIlII}')
                await IlIIIIlIIIlllllIIl.IlllIIIIlIIlIIlIIl()

    @IlIlIIIllIIIll.command()
    async def lIlIIIlIIlIllIIllI(IlIIIIlIIIlllllIIl, lllllIlIIllIIIIIll, *, lllllIIIllIIIIllIl: lllllllllllIlIl):
        if not lllllIlIIllIIIIIll.author.voice:
            return await lllllIlIIllIIIIIll.send('You need to be in a voice channel to use this command.')
        if not lllllIlIIllIIIIIll.voice_client:
            try:
                IlIlllIlIIIlIlIIIl = await lllllIlIIllIIIIIll.author.voice.channel.connect(cls=lIlllIlIlIIllI)
            except llllllllllllIII as lIllIllIlIIlIIIlII:
                return await lllllIlIIllIIIIIll.send(f'Failed to connect to the voice channel: {lIllIllIlIIlIIIlII}')
        else:
            IlIlllIlIIIlIlIIIl = lllllIlIIllIIIIIll.voice_client
        if not lllIIllllIIlII():
            await lllllIlIIllIIIIIll.send('No Lavalink nodes are available. Attempting to reconnect...')
            await IlIIIIlIIIlllllIIl.IlllIIIIlIIlIIlIIl()
            if not lllIIllllIIlII():
                return await lllllIlIIllIIIIIll.send('Failed to connect to a Lavalink node. Please try again later.')
        try:
            IllllIllIlIllIlIIl = await IllIllllllIIIl(lllllIIIllIIIIllIl)
        except IIllIlllIlIIIl as lIllIllIlIIlIIIlII:
            return await lllllIlIIllIIIIIll.send(f'There was an error with the Lavalink server: {lIllIllIlIIlIIIlII}')
        except llllllllllllIII as lIllIllIlIIlIIIlII:
            return await lllllIlIIllIIIIIll.send(f'An unexpected error occurred while searching for the track: {lIllIllIlIIlIIIlII}')
        if not IllllIllIlIllIlIIl:
            return await lllllIlIIllIIIIIll.send('No songs found.')
        IlIIIIIlIIIIIIllII = IllllIllIlIllIlIIl[0]
        if lllllIlIIllIIIIIll.guild.id not in IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI:
            IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id] = []
        lllllllllllIIll(IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id], lllllllllllIIll(lllllllllllllll, 'fromhex')('617070656e64').decode())(IlIIIIIlIIIIIIllII)
        if not IlIlllIlIIIlIlIIIl.is_playing():
            await IlIlllIlIIIlIlIIIl.lIlIIIlIIlIllIIllI(IlIIIIIlIIIIIIllII)
            await lllllIlIIllIIIIIll.send(f'Now playing: {IlIIIIIlIIIIIIllII.title}', view=IIIIlllIllllIIIlIl(IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI, IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id]))
        else:
            await lllllIlIIllIIIIIll.send(f'Added to playlist: {IlIIIIIlIIIIIIllII.title}', view=lIllllllllIlIIIIIl(IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI, IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id]))

    @IlIlIIIllIIIll.command()
    async def lllIIIllllIlIIlIlI(IlIIIIlIIIlllllIIl, lllllIlIIllIIIIIll):
        if lllllIlIIllIIIIIll.guild.id not in IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI or not IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id]:
            return await lllllIlIIllIIIIIll.send('The playlist is empty.')
        IllIlllIIIlIIlIIll = lllllllllllIIll('\n', lllllllllllIIll(lllllllllllllll, 'fromhex')('6a6f696e').decode())([f'{i + 1}. {IlIIIIIlIIIIIIllII.title}' for (i, IlIIIIIlIIIIIIllII) in lllllllllllIlII(IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id])])
        await lllllIlIIllIIIIIll.send(f'Current Playlist:\n{IllIlllIIIlIIlIIll}', view=lIllllllllIlIIIIIl(IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI, IlIIIIlIIIlllllIIl.llllIIlIlIllIlIIlI[lllllIlIIllIIIIIll.guild.id]))

    @IlIlIIIllIIIll.command()
    async def lIllIIIIIlIlIIIlIl(IlIIIIlIIIlllllIIl, lllllIlIIllIIIIIll, lIllIIIIIlIlIIIlIl: llllllllllllIIl):
        if not lllllIlIIllIIIIIll.voice_client or not lllllllllllIlll(lllllIlIIllIIIIIll.voice_client, lIlllIlIlIIllI):
            return await lllllIlIIllIIIIIll.send('Not connected to a voice channel.')
        await lllllIlIIllIIIIIll.voice_client.set_volume(lIllIIIIIlIlIIIlIl)
        await lllllIlIIllIIIIIll.send(f'Volume set to {lIllIIIIIlIlIIIlIl}%')

    @IlIlIIIllIIIll.command()
    async def filter(IlIIIIlIIIlllllIIl, lllllIlIIllIIIIIll, IIlllIllllIllllIlI: lllllllllllIlIl=None, *IIIIlIllIIIlIIlIll):
        if not lllllIlIIllIIIIIll.voice_client or not lllllllllllIlll(lllllIlIIllIIIIIll.voice_client, lIlllIlIlIIllI):
            return await lllllIlIIllIIIIIll.send('Not connected to a voice channel.')
        IlIIIIIlIlIIlIlIIl = {'equalizer': lIIIlIlIIIllll, 'karaoke': IIllIlIlIlIllI, 'timescale': IIIlIllIIIllIl, 'tremolo': llIIIllllIIIlI, 'vibrato': IllIIlIIllIIII, 'rotation': llllIIlIIllIII, 'distortion': lllIlllIlIllIl, 'channelmix': lIIIIlIllIlllI, 'lowpass': lllIlllllIlIIl}
        if IIlllIllllIllllIlI is None:
            IlIIlIllIIIIIlIIIl = lllllllllllIIll(', ', lllllllllllIIll(lllllllllllllll, 'fromhex')('6a6f696e').decode())(IlIIIIIlIlIIlIlIIl.keys())
            return await lllllIlIIllIIIIIll.send(f'Available filters: {IlIIlIllIIIIIlIIIl}\nUsage: !filter <filter_name> [args]\nExample: !filter equalizer 1.0 0.5 1.2')
        if lllllllllllIIll(IIlllIllllIllllIlI, lllllllllllIIll(lllllllllllllll, 'fromhex')('6c6f776572').decode())() not in IlIIIIIlIlIIlIlIIl:
            IlIIlIllIIIIIlIIIl = lllllllllllIIll(', ', lllllllllllIIll(lllllllllllllll, 'fromhex')('6a6f696e').decode())(IlIIIIIlIlIIlIlIIl.keys())
            return await lllllIlIIllIIIIIll.send(f'Invalid filter. Available filters: {IlIIlIllIIIIIlIIIl}')
        IlllIIlIllIIIlllIl = IlIIIIIlIlIIlIlIIl[lllllllllllIIll(IIlllIllllIllllIlI, lllllllllllIIll(lllllllllllllll, 'fromhex')('6c6f776572').decode())()]
        try:
            if not IIIIlIllIIIlIIlIll:
                await lllllIlIIllIIIIIll.voice_client.set_filter(None)
                return await lllllIlIIllIIIIIll.send(f'Reset {IIlllIllllIllllIlI} filter.')
            lIIIllIIIIlIlIlllI = IlllIIlIllIIIlllIl(*lllllllllllIllI(llllllllllllIll, IIIIlIllIIIlIIlIll))
            await lllllIlIIllIIIIIll.voice_client.set_filter(lIIIllIIIIlIlIlllI)
            await lllllIlIIllIIIIIll.send(f"Applied {IIlllIllllIllllIlI} filter with args: {lllllllllllIIll(', ', lllllllllllIIll(lllllllllllllll, 'fromhex')('6a6f696e').decode())(IIIIlIllIIIlIIlIll)}")
        except lllllllllllllII:
            await lllllIlIIllIIIIIll.send(f'Error: Invalid arguments for {IIlllIllllIllllIlI} filter. Please provide numeric values.')
        except llllllllllllIII as lIllIllIlIIlIIIlII:
            await lllllIlIIllIIIIIll.send(f'Error applying filter: {lllllllllllIlIl(lIllIllIlIIlIIIlII)}')

class IIIIIIIllIIlIIIIIl(IlIlIIIllIIIll.Cog):

    def __init__(IlIIIIlIIIlllllIIl, lIIIIIIIIllIIlIllI):
        IlIIIIlIIIlllllIIl.lIIIIIIIIllIIlIllI = lIIIIIIIIllIIlIllI

    @IlIlIIIllIIIll.command()
    async def lIIlIIIIIIIIIlIIlI(IlIIIIlIIIlllllIIl, lllllIlIIllIIIIIll, IlIIIllIlllIllllII: lllllllllllIlIl=None):
        lIIlIIIIIlIlIlllIl = ['rock', 'paper', 'scissors']
        if IlIIIllIlllIllllII is None:
            return await lllllIlIIllIIIIIll.send('Please provide your choice: rock, paper, or scissors. For example: `!rps rock`')
        IlIIIllIlllIllllII = lllllllllllIIll(IlIIIllIlllIllllII, lllllllllllIIll(lllllllllllllll, 'fromhex')('6c6f776572').decode())()
        if IlIIIllIlllIllllII not in lIIlIIIIIlIlIlllIl:
            return await lllllIlIIllIIIIIll.send('Invalid choice. Please choose rock, paper, or scissors.')
        IlIllIlIIllIIlllIl = lllIIIlIIIlIlI(lIIlIIIIIlIlIlllIl)
        await lllllIlIIllIIIIIll.send(f'I choose {IlIllIlIIllIIlllIl}!')
        if IlIIIllIlllIllllII == IlIllIlIIllIIlllIl:
            IlIlIIlllIllIIIlII = "It's a tie!"
        elif IlIIIllIlllIllllII == 'rock' and IlIllIlIIllIIlllIl == 'scissors' or (IlIIIllIlllIllllII == 'paper' and IlIllIlIIllIIlllIl == 'rock') or (IlIIIllIlllIllllII == 'scissors' and IlIllIlIIllIIlllIl == 'paper'):
            IlIlIIlllIllIIIlII = 'You win!'
        else:
            IlIlIIlllIllIIIlII = 'I win!'
        await lllllIlIIllIIIIIll.send(IlIlIIlllIllIIIlII)

async def IlllIlIllIllllIIII(lIIIIIIIIllIIlIllI):
    await lIIIIIIIIllIIlIllI.add_cog(IIllllIlIIlllIIIlI(lIIIIIIIIllIIlIllI))
    await lIIIIIIIIllIIlIllI.add_cog(IIIIIIIllIIlIIIIIl(lIIIIIIIIllIIlIllI))