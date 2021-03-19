# **Status-Bot**
## **Description**
*A bot for Discord that adds the status functions of BigBlueButton.*

## <ins>Disclaimer</ins>
This version is still a PRE-RELEASE and probably not quit ready for production as for instance the bot doesn't check for permissions on some hard cmds like the bulk(clear) command.

**Use at your own risk!**

## **Key Features**
* Discord-Bot using the modern Python API wrapper [Discord.py](https://github.com/Rapptz/discord.py)
    * Python API using ``async`` and ``await``
    * Optimised in both speed and memory
* Cross platform: Windows, Mac and Linux
* Adds functionality to set your status via nickname to:
    * raising hand ✋
    * thumbs up 👍
    * thumbs down 👎

    Note: to see the full command list click [here](https://github.com/showetek/Status-Bot/blob/main/commands.md)
* also functions to reset your status, everyones status and bulking messages

## **Installing**
**Python 3.5.3 or higher is required**

To install the bot just follow these four simple steps:

1. Download this repositorie using ``git clone https://github.com/showetek/Status-Bot.git``
2. Install the required libraries using:
```sh
# Linux/macOS
python3 -m pip install -U -r requirments.txt

# Windows
py -3 -m pip install -U -r requirments.txt
```
3. Insert your bot token into the file 'token' and make sure that your bot has ``SERVER MEMBERS INTENT`` privileges
4. Run the bot using:
```sh
# Linux/macOS
python3 bot.py

# Windows
py -3 bot.py
```

## **Currently developed by:**
* [Torben Heine](https://github.com/showetek)

## **Copyright and license**
>Copyright (c) 2021, Torben Heine
>
>This project is licensed under the [GNU General Public License v3.0](https://github.com/showetek/Status-Bot/blob/main/LICENSE)

## **Libraries**
*The following external libraries are used further in the code:*

### API wrapper:
* [discord.py](https://github.com/Rapptz/discord.py)

## **Current version and Info**
    @version     0.1.4 PRE-RELEASE
    @build       Passing
