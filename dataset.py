import discord, json, sys

from discord.ext import commands
from alive_progress import alive_bar
from datetime import datetime

bot = commands.Bot(command_prefix=' ')
config = json.load(open('config.json'))

class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

@bot.event
async def on_ready():
    start = datetime.now().timestamp()

    messages = []
    for g in bot.guilds:
        for c in g.text_channels:
            try:
                with alive_bar(title=f"Getting messages from {bcolors.BLUE}{g} {bcolors.CYAN}#{c}{bcolors.ENDC}") as bar:
                    async for m in c.history(limit=None):
                        if m.author.bot: continue

                        cnt = m.content.lower()
                        if cnt:
                            cnt = cnt.replace("\n", " ")
                            while "  " in cnt:
                                cnt = cnt.replace("  ", " ")
                            if cnt:
                                messages.append(cnt.split(" "))
                        bar()
            except Exception as a:
                print(f"{bcolors.BLUE}{g} {bcolors.CYAN}#{c}{bcolors.ENDC}: {bcolors.FAIL}{a}{bcolors.ENDC}")

    messages_parsed = {}
    with alive_bar(len(messages), title='Handling got messages') as bar:
        for x in messages:
            for i in range(len(x)-1):
                if x[i] not in messages_parsed:
                    messages_parsed[x[i]] = []
                if (
                    x[i+1] not in messages_parsed[x[i]]
                and x[i] != x[i+1]
                ):
                    messages_parsed[x[i]].append(x[i+1])
            bar()

    print("Saving dataset...")
    with open(f"dataset.json", "w") as f:
        json.dump(messages_parsed, f)

    t = datetime.now().timestamp()-start
    print(f"Done! Time: {bcolors.CYAN}{t}{bcolors.ENDC} seconds")

    sys.exit(0)


bot.run(config['token'])