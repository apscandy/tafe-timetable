import os
import discord
from discord import client
from discord.ext import commands
from dotenv import load_dotenv, find_dotenv
from tafe import TafeScrape
from quote import Quote

bot = commands.Bot(command_prefix='!')


class DiscordBot:

    @staticmethod
    @bot.command(name="timetable")
    async def times(ctx, *info):
        """
        Outputs the timetable data to discord
        
        TODO:
            Add filter to check the length of the message must be <= 1024 else an error is raised, ERROR: 400 Bad Request (error code: 50035): Invalid Form Body
             In embeds.0.fields.0.value: Must be 1024 or fewer in length. 
        """
        info = " ".join(info)
        tafe_timetable = TafeScrape(info)
        try:
            embed = discord.Embed(title="Your timetable results", description=info) #,color=Hex code
            embed.add_field(name="Timetable", value=tafe_timetable.get_timetable_output())
            await ctx.send(embed=embed)
            #await ctx.send(tafe_timetable.get_timetable_output())
        except Exception as e:
            await ctx.send(e)

    @staticmethod
    @bot.command(name="find")
    async def search(ctx, *info):
        """Outputs the search results data to discord"""
        info = " ".join(info)
        tafe_search = TafeScrape(info)
        try:
            embed = discord.Embed(title="All classes found in Brisbane campuses", description=f"Search resalts for: {info}") #,color=Hex code
            embed.add_field(name="Classes", value=tafe_search.get_search_output())
            await ctx.send(embed=embed)
            #await ctx.send(tafe_search.get_search_output())
        except Exception as e:
            await ctx.send(e)

    @staticmethod
    @bot.command(name="quote")
    async def _quote(ctx, quote_request):
        """Outputs the quote request data to discord"""
        get_quote = Quote(quote_request)
        embed = discord.Embed(title="Quote...") #,color=Hex code
        embed.add_field(name="Your quote", value=get_quote.quotes())
        await ctx.send(embed=embed)
        #await ctx.send(get_quote.quotes())

    @staticmethod
    @bot.command(name="commands")
    async def _quote(ctx):
        """help"""
        await ctx.send('find\ntimeable\nquote [today/random]')


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    bot.run(os.getenv('DISCORD_KEY_SPRING'), reconnect=True)