class DMEnabledGroup(app_commands.Group):
    def __init__(self, **kwargs):
        super().__init__(
            **kwargs,
            allowed_contexts=app_commands.AppCommandContext(
                guild=True, dm_channel=True, private_channel=True
            ),
            allowed_installs=app_commands.AppInstallationType(
                guild=True,
                user=True,  # REQUIRED FOR DMs
            ),
        )

# now create a group with your anyname, replace AnyName with your group name in blow code:-

AnyName_group = DMEnabledGroup(
    name="AnyName",
    description="Description here"
)

# now attach this group to bot tree command by doing this blow:-
bot.tree.add_command(AnyName_group) 
# remember to replace "AnyName" with your exact group name
# now let's take an example of command to attach it,see the blow code:-

@AnyName_group.command(name="anyname", description="your command description here")
async def meme(interaction: discord.Interaction):
    await interaction.response.send_message("output")

# Now the command will work in:
# Servers
# DMs
# Group DMs
# This approach helps keep your bot organized and prevents command limits from becoming a problem as your bot grows.
# 25 is the limit for group suncommands. you can also create subgroups same limit is 25 . so then total limit of global command is 100, let's do a simple calculation blow:-
# 25(groups) x 25(sub groups) x 100 (total global command) = 62500 commands,that's toooo crazy!!
# I hope this helps!
