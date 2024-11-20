import discord
from discord.ext import commands
from database import insert_ticket, get_open_tickets, close_ticket

class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_ticket(self, ctx):
        """Create a new ticket."""
        insert_ticket(ctx.author.id)
        await ctx.send(f"Ticket created for {ctx.author.mention}.")

    @commands.command()
    async def close_ticket(self, ctx, ticket_id: int):
        """Close a specific ticket."""
        close_ticket(ticket_id)
        await ctx.send(f"Ticket #{ticket_id} closed.")

    @commands.command()
    async def view_tickets(self, ctx):
        """View open tickets."""
        open_tickets = get_open_tickets()
        if open_tickets:
            tickets = '\n'.join([f"Ticket #{ticket[0]} - User: {ticket[1]} - Status: {ticket[2]}" for ticket in open_tickets])
            await ctx.send(f"Open tickets:\n{tickets}")
        else:
            await ctx.send("No open tickets.")

def setup(bot):
    bot.add_cog(TicketCog(bot))
