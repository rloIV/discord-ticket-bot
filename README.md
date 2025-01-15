# Discord Ticket Bot

## Overview

This is a Discord bot designed to manage a ticketing system for your server. The bot allows users to create, view, and close support tickets. It uses Python and `discord.py` for functionality and SQLite for database management.

---

## Features

- **Create Ticket:** Users can create new tickets for support.
- **View Tickets:** Admins can view all open tickets.
- **Close Ticket:** Admins can close resolved tickets.
- **Database Support:** Tickets are stored in an SQLite database.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- `discord.py` library

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rloIV/discord-ticket-bot.git
   cd discord-ticket-bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install discord.py
   ```

3. **Set Up Configuration:**
   - Rename `config.py.example` to `config.py`.
   - Add your bot's token and server-specific details:
     ```python
     TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
     DATABASE = 'tickets.db'
     GUILD_ID = 123456789012345678  # Replace with your Discord server ID
     CATEGORY_NAME = 'Tickets'      # Replace with your ticket category
     ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

---

## File Structure

- `bot.py`: Main entry point for the bot.
- `config.py`: Configuration file for storing bot token and settings.
- `database.py`: Handles SQLite database interactions.
- `ticket.py`: Cog for managing ticket-related commands.
- `ticket_cog.py`: Alternative implementation of ticket commands.

---

## Usage

### Commands

#### User Commands:
- `!create_ticket`:
  Creates a new ticket for the user.

#### Admin Commands:
- `!view_tickets`:
  Displays all open tickets.
- `!close_ticket <ticket_id>`:
  Closes a ticket with the specified `ticket_id`.

---

## Example

### Create a Ticket
1. User types `!create_ticket` in a text channel.
2. Bot responds with:
   ```
   Ticket created for @username. Your issue will be handled shortly.
   ```

### View Tickets (Admin Only)
1. Admin types `!view_tickets` in a text channel.
2. Bot responds with a list of open tickets:
   ```
   Open tickets:
   Ticket #1 - User: 123456789 - Status: open
   Ticket #2 - User: 987654321 - Status: open
   ```

### Close a Ticket (Admin Only)
1. Admin types `!close_ticket <ticket_id>`.
2. Bot confirms ticket closure:
   ```
   Ticket #1 has been closed.
   ```

---

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows best practices and is well-documented.

---

## Acknowledgements

- [discord.py Documentation](https://discordpy.readthedocs.io/)
- SQLite Documentation

