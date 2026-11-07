import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def Give_me_tips_to_avoid_climate_change(ctx):
    toawait ctx.send("Sure!,\n1. Shift to Clean Energy• Replace fossil fuels: Move away from coal, oil, and gas, and scale up renewable energy sources like solar, wind, hydroelectric, and geothermal power.• Power buildings cleanly: Switch home heating and appliances from gas to electricity, use heat pumps, and install energy-efficient LED lighting and better roof or wall insulation.• Support clean energy policy: Back government-led incentives, carbon pricing, and clean energy permitting reforms as outlined by the Citizens' Climate Lobby.2. Transform Transport• Ditch combustion engines: Walk, ride a bike, or use public transit instead of driving a personal car.• Electrify travel: Switch to an electric vehicle (EV) if you own a car.• Fly less: Cut back on commercial air travel and choose trains for shorter journeys.3. Change Diet and Reduce Waste• Eat more plant-based foods: Reduce consumption of meat (especially red meat) and dairy, which carry high carbon footprints.• Cut food waste: Plan meals carefully and compost organic waste to stop methane gas production in landfills.• Practice circular consumption: Buy fewer new goods, repair broken items, and recycle or reuse materials  lower industrial emissions.4. Protect and Restore Nature• Safeguard forests and oceans: Protect vital carbon-storing ecosystems like tropical forests, mangroves, coral reefs, and wetlands.• Plant native species: Support reforestation, urban tree-planting, and local habitat restoration.")

# cara panggil comman -> $passgen 10
bot.run("MTUwMDEwODY1MzAxMTkyNzIzMQ.GCWWmV.zw_MWVz2-jdFC_ozrTvbbllUeVcPEZUmls_3kQ")
