import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enables reading messages

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}! 👋')
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True  # Required to kick members

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}! 👋')

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    try:
        await member.kick(reason=reason)
        await ctx.send(f'👢 {member.mention} has been kicked. Reason: {reason}')
    except Exception as e:
        await ctx.send(f"⚠️ Failed to kick {member.mention}. Error: {e}")

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 You don't have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❗ Please mention a user to kick. Example: `!kick @user`")
    else:
        await ctx.send(f"❌ Error: {error}")

bot.run('MTM3NTUwMzcxOTQ5NTYzMDk2OQ.G6iKve.uvHs1uEdPDn7doBx_d4yGgEkBLxTzjdp6xTpJA')






