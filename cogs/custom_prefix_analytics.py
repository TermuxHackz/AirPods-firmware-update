lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll = bytes, bool, print, open, IOError, FileNotFoundError, str, getattr, len

from json import JSONDecodeError as IlIllllIIlIlII, load as llIlIIllIIlIIl, dump as lIlIllIIIllllI
from discord import Embed as lIIIlIIlllIlll
from discord.Color import blue as lIIlIIlIlllIII
from discord.ext import commands as lIllIIIlIlllII

class lIllllIllIlIIlIlIl(lIllIIIlIlllII.Cog):

    def __init__(llIIlllIlllIIIllIl, IlIIIlIllIIlIlllII):
        llIIlllIlllIIIllIl.IlIIIlIllIIlIlllII = IlIIIlIllIIlIlllII
        llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI = {}
        llIIlllIlllIIIllIl.IIlIlIlllIlllIIlll()

    def IIlIlIlllIlllIIlll(llIIlllIlllIIIllIl):
        try:
            with lllllllllllllII('prefixes.json', 'r') as llIIIlIIllIIlIIIll:
                llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI = llIlIIllIIlIIl(llIIIlIIllIIlIIIll)
        except llllllllllllIlI:
            llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI = {}
            llIIlllIlllIIIllIl.IIIIIIIllIIIIIlllI()
        except IlIllllIIlIlII:
            lllllllllllllIl('Error decoding prefixes.json. Using default prefixes.')
            llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI = {}
            llIIlllIlllIIIllIl.IIIIIIIllIIIIIlllI()

    def IIIIIIIllIIIIIlllI(llIIlllIlllIIIllIl):
        try:
            with lllllllllllllII('prefixes.json', 'w') as llIIIlIIllIIlIIIll:
                lIlIllIIIllllI(llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI, llIIIlIIllIIlIIIll, indent=4)
        except llllllllllllIll as lllIlIIIIIIlIllllI:
            lllllllllllllIl(f'Error saving prefixes: {lllIlIIIIIIlIllllI}')

    def lllIIIIIIIIIlIlllI(llIIlllIlllIIIllIl, lIIlllllIlIIIIIlII):
        """Get the prefix for the given guild."""
        return llllllllllllIII(llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI, llllllllllllIII(lllllllllllllll, 'fromhex')('676574').decode())(llllllllllllIIl(lIIlllllIlIIIIIlII), '!')

    @lIllIIIlIlllII.lllllIlllllIIlIlll(name='set_prefix')
    @lIllIIIlIlllII.has_permissions(administrator=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    async def IIllIIllIlllIIIllI(llIIlllIlllIIIllIl, lIlIIIIlllIIIIIIll, llllllIIIlIIIlIIIl: llllllllllllIIl=None):
        """Set a custom prefix for the server."""
        if llllllIIIlIIIlIIIl is None:
            await lIlIIIIlllIIIIIIll.send('Please provide a new prefix. Usage: `!set_prefix <new_prefix>`')
            return
        if lllllllllllIlll(llllllIIIlIIIlIIIl) > 10:
            await lIlIIIIlllIIIIIIll.send('The prefix must be 10 characters or less.')
            return
        llIIlllIlllIIIllIl.IIIlIIllIIlIIIIllI[llllllllllllIIl(lIlIIIIlllIIIIIIll.guild.id)] = llllllIIIlIIIlIIIl
        llIIlllIlllIIIllIl.IIIIIIIllIIIIIlllI()
        await lIlIIIIlllIIIIIIll.send(f'Prefix has been set to `{llllllIIIlIIIlIIIl}`')

    @lIllIIIlIlllII.lllllIlllllIIlIlll(name='get_prefix')
    async def IlIllllllllIIlIIlI(llIIlllIlllIIIllIl, lIlIIIIlllIIIIIIll):
        """Get the current prefix for the server."""
        IIIlIllIIlIlIIlllI = llIIlllIlllIIIllIl.lllIIIIIIIIIlIlllI(lIlIIIIlllIIIIIIll.guild.id)
        await lIlIIIIlllIIIIIIll.send(f'The current prefix is: `{IIIlIllIIlIlIIlllI}`')

class lIIllllIlIllIIllII(lIllIIIlIlllII.Cog):

    def __init__(llIIlllIlllIIIllIl, IlIIIlIllIIlIlllII):
        llIIlllIlllIIIllIl.IlIIIlIllIIlIlllII = IlIIIlIllIIlIlllII
        llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI = {}
        llIIlllIlllIIIllIl.llllIIIIllIIlIllIl()

    def llllIIIIllIIlIllIl(llIIlllIlllIIIllIl):
        try:
            with lllllllllllllII('analytics.json', 'r') as llIIIlIIllIIlIIIll:
                llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI = llIlIIllIIlIIl(llIIIlIIllIIlIIIll)
        except llllllllllllIlI:
            llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI = {}
        except IlIllllIIlIlII:
            lllllllllllllIl('Error decoding analytics.json. Starting with empty analytics.')
            llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI = {}

    def IlIIIIllIIlllIlIll(llIIlllIlllIIIllIl):
        try:
            with lllllllllllllII('analytics.json', 'w') as llIIIlIIllIIlIIIll:
                lIlIllIIIllllI(llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI, llIIIlIIllIIlIIIll, indent=4)
        except llllllllllllIll as lllIlIIIIIIlIllllI:
            lllllllllllllIl(f'Error saving analytics: {lllIlIIIIIIlIllllI}')

    @lIllIIIlIlllII.Cog.listener()
    async def IlIlIlllIlllIIllll(llIIlllIlllIIIllIl, lIlIIIIlllIIIIIIll):
        if lIlIIIIlllIIIIIIll.guild is None:
            return
        IlIIlIIlIlIIIllIII = lIlIIIIlllIIIIIIll.lllllIlllllIIlIlll.name
        lIIlllllIlIIIIIlII = llllllllllllIIl(lIlIIIIlllIIIIIIll.guild.id)
        if lIIlllllIlIIIIIlII not in llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI:
            llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII] = {}
        if IlIIlIIlIlIIIllIII not in llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII]:
            llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII][IlIIlIIlIlIIIllIII] = 0
        llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII][IlIIlIIlIlIIIllIII] += 1
        llIIlllIlllIIIllIl.IlIIIIllIIlllIlIll()

    @lIllIIIlIlllII.lllllIlllllIIlIlll(name='analytics')
    @lIllIIIlIlllII.has_permissions(administrator=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    async def lllllIllIIIllIIlII(llIIlllIlllIIIllIl, lIlIIIIlllIIIIIIll):
        """Show command usage analytics for the server."""
        lIIlllllIlIIIIIlII = llllllllllllIIl(lIlIIIIlllIIIIIIll.guild.id)
        if lIIlllllIlIIIIIlII in llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI and llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII]:
            llllIIIlllllllllll = lIIIlIIlllIlll(title='Command Usage Analytics', color=lIIlIIlIlllIII())
            for (lllllIlllllIIlIlll, lIllIlIlIIllIIIlll) in llllllllllllIII(llIIlllIlllIIIllIl.IllIllIlIIIIIIlllI[lIIlllllIlIIIIIlII], llllllllllllIII(lllllllllllllll, 'fromhex')('6974656d73').decode())():
                llllIIIlllllllllll.add_field(name=lllllIlllllIIlIlll, value=f'Used {lIllIlIlIIllIIIlll} times', inline=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
            await lIlIIIIlllIIIIIIll.send(embed=llllIIIlllllllllll)
        else:
            await lIlIIIIlllIIIIIIll.send('No analytics data available for this server.')

async def llIIIlIlIllIIIIlII(IlIIIlIllIIlIlllII):
    await IlIIIlIllIIlIlllII.add_cog(lIllllIllIlIIlIlIl(IlIIIlIllIIlIlllII))
    await IlIIIlIllIIlIlllII.add_cog(lIIllllIlIllIIllII(IlIIIlIllIIlIlllII))