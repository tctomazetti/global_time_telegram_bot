"""
Responseble for the telegram bot.
Should contain the main code of the bot.
"""
import telebot
import os
import json


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


if __name__ == "__main__":
    token = Token()
    print(token.token)
