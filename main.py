import discord
import os
import webbrowser  
from colorama import Fore as col
from discord.ext import commands

system = os.system

def menu():
    print(f"{col.BLUE}Ingyen fejlesztő jelvényhez csináld a következőket:")
    tkn = input(f"{col.RED}Add meg a discord bot tokened: ")
    print("Várj, bot keresése folyamatban!")
    bot = commands.Bot(command_prefix=".")

    @bot.event
    async def on_ready():
        system("cls")
        print(f"{col.CYAN}Discord szerver csatlakoztató és Jelvény igénylő oldal megnyitása")
        webbrowser.open(f"https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=156766824512&scope=bot%20applications.commands")
        print(f"{col.RED}Logged in as {bot.user.name} : {bot.user.id}")
        webbrowser.open(f"https://discord.com/developers/active-developer")
           
    @bot.slash_command(description="Pong")
    async def ping(ctx):
        await ctx.respond("Pong")

    bot.run(tkn)

if __name__ == "__main__":
    menu()
