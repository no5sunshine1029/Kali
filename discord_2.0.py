import os


def clear(): return os.system('clear')


def install(package):
    os.system(f"poetry add {package}")


clear()
install('git+https://github.com/Rapptz/discord.py')
clear()
