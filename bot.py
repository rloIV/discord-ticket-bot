import discord
from discord.ext import commands
import config
from ticket import TicketCommands
from database import create_db

# Create database and tables
create_db()

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    bot.add_cog(TicketCommands(bot))

bot.run(config.TOKEN)
