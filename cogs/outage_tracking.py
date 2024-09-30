lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl, llllllllllllIII, lllllllllllIlll, lllllllllllIllI = bytes, bool, print, open, int, Exception, OSError, str, getattr, ConnectionRefusedError

from os import getenv as lIIlllIlIIIIII
from os.path import exists as IIllIlIlIIIIlI
from json import dump as IIIIIlllIlllll, load as IIIIlIIIIIlIII
from psutil import virtual_memory as lIllIllIIIIllI, cpu_percent as IllIIlIllIlIII
from socket import create_connection as IlllIlIlIIIIlI, timeout as IlIIlIllIIlIlI
from discord import TextChannel as lIllIIlIlIIlIl, Interaction as lIlIIlIIllIlII, Embed as llIIlllIIllIlI
from discord.Color import red as IIIIlIlIlIlIlI, green as lllIIlIlIIllll
from discord.errors import Forbidden as IlIlIllllIllll
from discord.ext import commands as IIlIllIIIIIlIl, tasks as lIIIlIIllIlIlI
from discord import app_commands as IlIIllIllIlIIl
from datetime import datetime as llIllIlIllIIIl, timedelta as IlllIIlIlIllll
lIIIIIlIlIllIIllIl = 'outage_channels.json'
llIlIlIlllIIlIIIII = llllllllllllIll(lIIlllIlIIIIII('BOT_OWNER_ID'))
lllIIIIIlIlllIIlll = lIIlllIlIIIIII('SERVER_ADDRESS')
IIllIIlIIlIlIIIlII = llllllllllllIll(lIIlllIlIIIIII('SERVER_PORT', '20874'))

class llIIIlIIlllIIllllI(IIlIllIIIIIlIl.Cog):

    def __init__(llIlIlIlIIlllIlIIl, IlllllllIIIIIIIIlI):
        llIlIlIlIIlllIlIIl.IlllllllIIIIIIIIlI = IlllllllIIIIIIIIlI
        llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII = llIlIlIlIIlllIlIIl.IlIlIIlIIlIlIIIlII()
        llIlIlIlIIlllIlIIl.IIlIlIllIlIIlIIIlI = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
        llIlIlIlIIlllIlIIl.IlIlllIIIlIIIIllll.start()

    def llIllIIIIllIlllIIl(llIlIlIlIIlllIlIIl):
        llIlIlIlIIlllIlIIl.IlIlllIIIlIIIIllll.cancel()

    def IlIlIIlIIlIlIIIlII(llIlIlIlIIlllIlIIl):
        if IIllIlIlIIIIlI(lIIIIIlIlIllIIllIl):
            with lllllllllllllII(lIIIIIlIlIllIIllIl, 'r') as IllIlIlIIlllIlIlll:
                return IIIIlIIIIIlIII(IllIlIlIIlllIlIlll)
        return {}

    def IIIIlIllIlllIIlIll(llIlIlIlIIlllIlIIl):
        with lllllllllllllII(lIIIIIlIlIllIIllIl, 'w') as IllIlIlIIlllIlIlll:
            IIIIIlllIlllll(llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII, IllIlIlIIlllIlIlll, indent=2)

    @lIIIlIIllIlIlI.loop(minutes=5)
    async def IlIlllIIIlIIIIllll(llIlIlIlIIlllIlIIl):
        IIIIIlIIIIlllIIIII = llIlIlIlIIlllIlIIl.IlllllIIIllIIIIlll()
        IllIIlllIlIlllllIl = IllIIlllIlIlllllIl()
        lllIIIlllIIIIIIllI = lIllIllIIIIllI().percent
        if not IIIIIlIIIIlllIIIII:
            await llIlIlIlIIlllIlIIl.lIlllllIlIIlIIIIlI(f'Cannot connect to server')
        elif llIlIlIlIIlllIlIIl.IIlIlIllIlIIlIIIlI:
            await llIlIlIlIIlllIlIIl.IllIlllIIIlIIIlIll(f'Connection to server restored')
        if IllIIlllIlIlllllIl > 90 or lllIIIlllIIIIIIllI > 90:
            await llIlIlIlIIlllIlIIl.lIlllllIlIIlIIIIlI(f'High server load detected: CPU {IllIIlllIlIlllllIl}%, Memory {lllIIIlllIIIIIIllI}%')

    def IlllllIIIllIIIIlll(llIlIlIlIIlllIlIIl):
        try:
            with IlllIlIlIIIIlI((lllIIIIIlIlllIIlll, IIllIIlIIlIlIIIlII), timeout=10):
                return llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        except (IlIIlIllIIlIlI, lllllllllllIllI, llllllllllllIIl):
            return llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)

    @IlIlllIIIlIIIIllll.before_loop
    async def lIIIIlIIlIIIlIIlll(llIlIlIlIIlllIlIIl):
        await llIlIlIlIIlllIlIIl.IlllllllIIIIIIIIlI.wait_until_ready()

    async def llIlIIllllIIlIIlIl(llIlIlIlIIlllIlIIl, IllllllIlIIlIllIlI: lIlIIlIIllIlII) -> llllllllllllllI:
        return IllllllIlIIlIllIlI.user.guild_permissions.manage_guild or IllllllIlIIlIllIlI.user.guild_permissions.manage_channels or IllllllIlIIlIllIlI.user.guild_permissions.administrator or (IllllllIlIIlIllIlI.user.id == llIlIlIlllIIlIIIII)

    @IlIIllIllIlIIl.command(name='set_outage_channel', description='Set the channel for bot outage notifications')
    async def lIIIIIlllIIIlIlIII(llIlIlIlIIlllIlIIl, IllllllIlIIlIllIlI: lIlIIlIIllIlII, IlIlIIlIIIIlllIlII: lIllIIlIlIIlIl):
        if not await llIlIlIlIIlllIlIIl.llIlIIllllIIlIIlIl(IllllllIlIIlIllIlI):
            await IllllllIlIIlIllIlI.response.send_message("You don't have the necessary permissions to use this command.", ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
            return
        llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII[llllllllllllIII(IllllllIlIIlIllIlI.IIllIIlIllIllIIIll)] = IlIlIIlIIIIlllIlII.id
        llIlIlIlIIlllIlIIl.IIIIlIllIlllIIlIll()
        await IllllllIlIIlIllIlI.response.send_message(f'Outage notifications will now be sent to {IlIlIIlIIIIlllIlII.mention}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @lIIIIIlllIIIlIlIII.lIllIlIIIIIIIllIIl
    async def IlIIllIllIIlIlIlII(llIlIlIlIIlllIlIIl, IllllllIlIIlIllIlI: lIlIIlIIllIlII, lIllIlIIIIIIIllIIl: IlIIllIllIlIIl.AppCommandError):
        await IllllllIlIIlIllIlI.response.send_message(f'An error occurred: {llllllllllllIII(lIllIlIIIIIIIllIIl)}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    def lIIIIlIlllIIIlIIII(llIlIlIlIIlllIlIIl, IIllIIlIllIllIIIll):
        return llIlIlIlIIlllIlIIl.IlllllllIIIIIIIIlI.get_channel(lllllllllllIlll(llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII, lllllllllllIlll(lllllllllllllll, 'fromhex')('676574').decode())(llllllllllllIII(IIllIIlIllIllIIIll)))

    @IlIIllIllIlIIl.command(name='delete_outage_channel', description='Delete the configured outage notification channel')
    async def lIIIllIlIllIIIlllI(llIlIlIlIIlllIlIIl, IllllllIlIIlIllIlI: lIlIIlIIllIlII):
        if not await llIlIlIlIIlllIlIIl.llIlIIllllIIlIIlIl(IllllllIlIIlIllIlI):
            await IllllllIlIIlIllIlI.response.send_message("You don't have the necessary permissions to use this command.", ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
            return
        IIllIIlIllIllIIIll = llllllllllllIII(IllllllIlIIlIllIlI.IIllIIlIllIllIIIll)
        if IIllIIlIllIllIIIll in llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII:
            del llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII[IIllIIlIllIllIIIll]
            llIlIlIlIIlllIlIIl.IIIIlIllIlllIIlIll()
            await IllllllIlIIlIllIlI.response.send_message('The outage notification channel has been removed.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
        else:
            await IllllllIlIIlIllIlI.response.send_message('There is no outage notification channel set for this server.', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @lIIIllIlIllIIIlllI.lIllIlIIIIIIIllIIl
    async def IIllIllIlllIIIllll(llIlIlIlIIlllIlIIl, IllllllIlIIlIllIlI: lIlIIlIIllIlII, lIllIlIIIIIIIllIIl: IlIIllIllIlIIl.AppCommandError):
        await IllllllIlIIlIllIlI.response.send_message(f'An error occurred: {llllllllllllIII(lIllIlIIIIIIIllIIl)}', ephemeral=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))

    @IIlIllIIIIIlIl.command(name='report_outage')
    @IIlIllIIIIIlIl.is_owner()
    async def IlIlIIIIlllllIIllI(llIlIlIlIIlllIlIIl, IlIlIllIlIIIIIIlIl, *, lIIIIIlllllllllIIl: llllllllllllIII):
        """Manually report a bot outage (Bot Owner Only)"""
        try:
            await llIlIlIlIIlllIlIIl.lIlllllIlIIlIIIIlI(lIIIIIlllllllllIIl)
            await IlIlIllIlIIIIIIlIl.send('Outage reported.')
        except llllllllllllIlI as lIlIIIlIIIIlIlllll:
            await IlIlIllIlIIIIIIlIl.send(f'An error occurred while reporting the outage: {llllllllllllIII(lIlIIIlIIIIlIlllll)}')

    @IIlIllIIIIIlIl.command(name='report_resolution')
    @IIlIllIIIIIlIl.is_owner()
    async def IlIIlIlllIIlIIIlII(llIlIlIlIIlllIlIIl, IlIlIllIlIIIIIIlIl, *, lIIIIIlllllllllIIl: llllllllllllIII):
        """Manually report a bot outage resolution (Bot Owner Only)"""
        try:
            await llIlIlIlIIlllIlIIl.IllIlllIIIlIIIlIll(lIIIIIlllllllllIIl)
            await IlIlIllIlIIIIIIlIl.send('Resolution reported.')
        except llllllllllllIlI as lIlIIIlIIIIlIlllll:
            await IlIlIllIlIIIIIIlIl.send(f'An error occurred while reporting the resolution: {llllllllllllIII(lIlIIIlIIIIlIlllll)}')

    async def lIlllllIlIIlIIIIlI(llIlIlIlIIlllIlIIl, lIIIIIlllllllllIIl):
        llIlIlIlIIlllIlIIl.IIlIlIllIlIIlIIIlI = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1)
        for (IIllIIlIllIllIIIll, lIIlIIlIlllIIlIIlI) in lllllllllllIlll(llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII, lllllllllllIlll(lllllllllllllll, 'fromhex')('6974656d73').decode())():
            IlIlIIlIIIIlllIlII = llIlIlIlIIlllIlIIl.IlllllllIIIIIIIIlI.get_channel(lIIlIIlIlllIIlIIlI)
            if IlIlIIlIIIIlllIlII:
                try:
                    lllIIlIlIlIllIIllI = llIIlllIIllIlI(title='Bot Outage', description=lIIIIIlllllllllIIl, color=IIIIlIlIlIlIlI())
                    lllIIlIlIlIllIIllI.add_field(name='Status', value='🔴 Issue Detected', inline=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
                    lllIIlIlIlIllIIllI.add_field(name='Time', value=f"{llIllIlIllIIIl.utcnow().strftime('%d %B %Y %H:%M')} UTC", inline=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
                    await IlIlIIlIIIIlllIlII.send(embed=lllIIlIlIlIllIIllI)
                except IlIlIllllIllll:
                    lllllllllllllIl(f'Unable to send outage report to channel {lIIlIIlIlllIIlIIlI} in guild {IIllIIlIllIllIIIll}: Missing permissions')
                except llllllllllllIlI as lIlIIIlIIIIlIlllll:
                    lllllllllllllIl(f'Error sending outage report to channel {lIIlIIlIlllIIlIIlI} in guild {IIllIIlIllIllIIIll}: {llllllllllllIII(lIlIIIlIIIIlIlllll)}')

    async def IllIlllIIIlIIIlIll(llIlIlIlIIlllIlIIl, lIIIIIlllllllllIIl):
        llIlIlIlIIlllIlIIl.IIlIlIllIlIIlIIIlI = llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0)
        for (IIllIIlIllIllIIIll, lIIlIIlIlllIIlIIlI) in lllllllllllIlll(llIlIlIlIIlllIlIIl.IIIIIlllIlIIIIlIII, lllllllllllIlll(lllllllllllllll, 'fromhex')('6974656d73').decode())():
            IlIlIIlIIIIlllIlII = llIlIlIlIIlllIlIIl.IlllllllIIIIIIIIlI.get_channel(lIIlIIlIlllIIlIIlI)
            if IlIlIIlIIIIlllIlII:
                try:
                    lllIIlIlIlIllIIllI = llIIlllIIllIlI(title='Bot Status Update', description=lIIIIIlllllllllIIl, color=lllIIlIlIIllll())
                    lllIIlIlIlIllIIllI.add_field(name='Status', value='🟢 Issue Resolved', inline=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
                    lllIIlIlIlIllIIllI.add_field(name='Time', value=f"{llIllIlIllIIIl.utcnow().strftime('%d %B %Y %H:%M')} UTC", inline=llllllllllllllI(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 0))
                    await IlIlIIlIIIIlllIlII.send(embed=lllIIlIlIlIllIIllI)
                except IlIlIllllIllll:
                    lllllllllllllIl(f'Unable to send resolution report to channel {lIIlIIlIlllIIlIIlI} in guild {IIllIIlIllIllIIIll}: Missing permissions')
                except llllllllllllIlI as lIlIIIlIIIIlIlllll:
                    lllllllllllllIl(f'Error sending resolution report to channel {lIIlIIlIlllIIlIIlI} in guild {IIllIIlIllIllIIIll}: {llllllllllllIII(lIlIIIlIIIIlIlllll)}')

async def IIllllIllIlIlllllI(IlllllllIIIIIIIIlI):
    await IlllllllIIIIIIIIlI.add_cog(llIIIlIIlllIIllllI(IlllllllIIIIIIIIlI))