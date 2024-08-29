import os
from datetime import date


VERSION = "0.0.16 Preview"
UPDATE_NUMBER = 0
YEAR = int(date.today().year)
AUTHOR = "AZ Studio"
FEEDBACK_URL = "https://github.com/AZ-Studio-2023/RedstoneLauncher/issues"
HELP_URL = "https://azteam.cn"



MINECRAFT_ICON = "resource/image/core/minecraft.png"
FORGE_ICON = "resource/image/core/forge.png"
FABRIC_ICON = "resource/image/core/fabric.png"
MICROSOFT_ACCOUNT = "resource/image/account/Microsoft.png"
LEGACY_ACCOUNT = "resource/image/account/legacy.png"
THIRD_PARTY_ACCOUNT = "resource/image/account/third_party.png"
JAVA_RUNTIME = "resource/image/java.png"
SNAPSHOT = "resource/image/block/obsidian.png"
RELEASE = "resource/image/block/grass_block.png"

ARIA2C_PATH = 'resource/aria2/aria2c.exe'
RPC_PORT = 6800
DEFAULT_GAME_PATH = os.path.join(os.path.expanduser('~'), "AppData", "Roaming", ".minecraft")
PLU_URL = ""

LAUNCH_DATA = {}

PROCESS_DATA = []

DOWNLOAD_DATA = []

def setLaunchData(data):
    global LAUNCH_DATA
    LAUNCH_DATA = data

def getLaunchData():
    global LAUNCH_DATA
    return LAUNCH_DATA
def setProcessData(data):
    global PROCESS_DATA
    PROCESS_DATA = data

def getProcessData():
    global PROCESS_DATA
    return PROCESS_DATA

def setDownloadData(data):
    global DOWNLOAD_DATA
    DOWNLOAD_DATA = data

def getDownloadData():
    global DOWNLOAD_DATA
    return DOWNLOAD_DATA




