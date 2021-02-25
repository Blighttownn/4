from pyowm import OWM
import discord
from config import token
client = discord.Client()


def weatherDet(place):
    owm = OWM("0daf1e3463914472f26d510ae197bd02")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    det = w.detailed_status
    return det
def weatherHum(place):
    owm = OWM("0daf1e3463914472f26d510ae197bd02")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    hum=w.humidity
    return hum

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):
    city = message.content.split()[1]

    if message.author == client.user:
        return

    if message.content.startswith('!weather'):
        await message.channel.send(f'Погода сегодня:\nОблачность: {weatherDet(city)}\nВлажность: {weatherHum(city)}')

client.run(token)

