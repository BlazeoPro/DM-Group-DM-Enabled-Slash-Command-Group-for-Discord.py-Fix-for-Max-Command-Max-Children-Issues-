# DM-Group-DM-Enabled-Slash-Command-Group-for-Discord.py-Fix-for-Max-Command-Max-Children-Issues-
When building large bots with discord.py, you may run into errors like “maximum command limit reached” or “max children exceeded” while organizing slash commands. These issues often appear when you try to add many commands directly to the root command tree.
One good solution is to organize commands into groups that also work in Servers, DMs, and Group DMs.
The small class below creates a custom command group that automatically enables commands for:
Servers (Guilds)
Direct Messages (DMs)
Group DMs
User installs
This is useful if your bot has utility commands, fun commands, or tools that should work even when the bot is not in a server.
By using this custom group class, you can:
Keep your command structure clean
Avoid hitting root command limits
Allow users to use slash commands in DMs or private channels
