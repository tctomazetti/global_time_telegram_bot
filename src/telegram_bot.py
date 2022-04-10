"""
Responseble for the telegram bot.
Should contain the main code of the bot.
"""
import telebot
import os
import json

from helpers import main_menu


class Token:
    """Class to get the token from the file."""

    def __init__(
        self, dirname: str = "global_time_telegram_bot", key_file: str = "key.json"
    ) -> None:
        self.dirname = dirname
        self.key_file = key_file
        self.adjust_dir()
        self.token = self.get_token()

    def adjust_dir(self) -> None:
        """Adjust the directory to the right one."""
        current_path = os.getcwd()
        generic_path = current_path.split(self.dirname)[0]
        root_path = f"{generic_path}{self.dirname}{os.sep}"
        self.key_path = f"{root_path}src{os.sep}keys{os.sep}"

    def get_token(self) -> str:
        """Get the token from the file."""
        if not os.path.exists(f"{self.key_path}{self.key_file}"):
            raise FileNotFoundError(f"Token file not found in {self.key_path}")

        with open(f"{self.key_path}{self.key_file}", "r") as f:
            data = json.load(f)
        return data["token"]


class TelegramBot:
    """Class to get the bot."""

    from src.helpers import main_menu, get_weather_by_city, get_weather_by_coordinates

    token = Token()
    bot = telebot.TeleBot(token.token)
    print("Bot is running...")

    @bot.message_handler(commands=["start"])
    def start_message(message, bot: telebot.TeleBot = bot):
        """Start message."""
        bot.send_message(message.chat.id, "Hello, I'm the Global Time Bot.")
        bot.send_message(message.chat.id, main_menu())

    @bot.message_handler(commands=["1"])
    def search_by_city(message, bot: telebot.TeleBot = bot):
        """Search by city."""
        bot.send_message(message.chat.id, "Search by city. To be implemented.")

    @bot.message_handler(commands=["2"])
    def search_by_coordinates(message, bot: telebot.TeleBot = bot):
        """Search by coordinates."""
        bot.send_message(message.chat.id, "Search by coordinates. To be implemented.")

    @bot.message_handler(func=lambda message: True)
    def defult_answer(message: str, bot: telebot.TeleBot = bot) -> None:
        """Default answer."""
        print(message)
        bot.send_message(
            message.chat.id,
            "Sorry, I don't understand you.\nI'm still learning...\nPlease, try again.",
        )
        bot.send_message(message.chat.id, main_menu())

    bot.polling()


if __name__ == "__main__":
    token = Token()
    TelegramBot()
