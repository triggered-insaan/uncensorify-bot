from .bot import bot, getMe

if __name__ == "__main__":
    bot.loop.run_until_complete(getMe(bot))
    print("Bot started 🚀")
    bot.run_until_disconnected()
