import datetime
from Speedo import *
from Speedo.config import Config
from Speedo.helpers import *
from Speedo.utils import *
from Speedo.random_strings import *
from Speedo.version import __speedo__
from telethon import version


SPEEDO_USER = os.environ.get("YOUR_NAME")
ForGo10God = "ALIVE"
speedo_mention = f"[{SPEEDO_USER}](tg://user?id={ForGo10God})"
speedo_logo = "./Speedo/resources/pics/Speedo_logo.jpg"
cjb = "./Speedo/resources/pics/cjb.jpg"
restlo = "./Speedo/resources/pics/rest.jpeg"
shuru = "./Speedo/resources/pics/shuru.jpg"
shhh = "./Speedo/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
speedo_ver = __speedo__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "Its_Speedo"
my_group = Config.MY_GROUP or "Speedo_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/its_Speedo"
speedo_channel = f"[†hê SPEEDOBOT]({chnl_link})"
grp_link = "https://t.me/Speedo_Chat"
speedo_grp = f"[SPEEDOBOT Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# Speedo
