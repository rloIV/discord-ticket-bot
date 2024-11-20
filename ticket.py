import discord
from discord.ext import commands
from database import insert_ticket, get_open_tickets, close_ticket

class TicketCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='create_ticket')
    async def create_ticket(self, ctx):
        """Command to create a new ticket."""
        insert_ticket(ctx.author.id)
        await ctx.send(f"Ticket created for {ctx.author.mention}. Your issue will be handled shortly.")

    @commands.command(name='close_ticket')
    async def close_ticket_cmd(self, ctx, ticket_id: int):
        """Command to close an existing ticket."""
        close_ticket(ticket_id)
        await ctx.send(f"Ticket #{ticket_id} has been closed.")

    @commands.command(name='view_tickets')
    async def view_tickets(self, ctx):
        """Command for admins to view all open tickets."""
        open_tickets = get_open_tickets()
        if open_tickets:
            tickets_list = '\n'.join([f"Ticket #{ticket[0]} - User: {ticket[1]} - Status: {ticket[2]}" for ticket in open_tickets])
            await ctx.send(f"Open tickets:\n{tickets_list}")
        else:
            await ctx.send("No open tickets.")
