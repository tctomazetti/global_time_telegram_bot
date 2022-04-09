from distutils.core import setup
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name="GlobalTime_Bot",
    version="0.1.0",
    description="Telegram bot to search the time of the city",
    author="Tiago Tomazetti",
    packages=["src"],
    include_package_data=True,
    python_requires=">=3.4",
    install_requires=open(
        path.join(here, "requirements.txt"), encoding="utf-8"
    ).read()
)
