import disocrd
from discord.ext import commands, tasks
import os
import requests
from dotenv import load_dotenv

#Load env variables
load_dotenv()

#Create bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot token from env variable
TOKEN - os.getenv('DISCORD_TOKEN')

#Define the bot's commands and events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
# Raid and dungeon assistance
@bot.command(name='strategy')
async def strategy(ctx, *, content: str):
    strategies = {
        "raid1": "Here is the strategy for Raid 1: [Link]",
        "raid2": "Here is the strategy for Raid 2: [Link]",
        # Add more strategies here
    }
    await ctx.send(strategies.get(content.lower(), "Strategy not found. Please try another."))
    

# 4. Crafting and Gathering Assistance
@bot.command(name='craft')
async def craft(ctx, item: str):
    # Placeholder for crafting requests
    await ctx.send(f"Crafting request for {item} has been noted.")

@bot.command(name='gather')
async def gather(ctx, node: str):
    # Placeholder for gathering timers
    await ctx.send(f"Gathering timer for {node} has been set.")

# 5. Market Board Tracker
@bot.command(name='price')
async def price(ctx, *, item: str):
    response = requests.get(f"https://api.example.com/market?item={item}")
    if response.status_code == 200:
        data = response.json()
        price = data['price']
        await ctx.send(f"The current market price for {item} is {price} gil.")
    else:
        await ctx.send("Item not found or API error.")


# 6. Announcements and News
@tasks.loop(hours=1)
async def fetch_news():
    channel = bot.get_channel(int(os.getenv("NEWS_CHANNEL_ID")))
    # Placeholder for fetching news
    news = "Latest news from FFXIV: [Link]"
    await channel.send(news)

# 9. Custom Commands
@bot.command(name='links')
async def links(ctx):
    useful_links = {
        "wiki": "https://ffxiv.fandom.com/wiki/",
        "lodestone": "https://na.finalfantasyxiv.com/lodestone/",
        # Add more links here
    }
    response = "\n".join([f"{key}: {value}" for key, value in useful_links.items()])
    await ctx.send(response)

# 10. Integration with Other Tools (e.g., Google Calendar)
@bot.command(name='calendar')
async def calendar(ctx):
    # Placeholder for Google Calendar integration
    await ctx.send("Here is the link to the shared Google Calendar: [Link]")

# Run the bot
bot.run(TOKEN)