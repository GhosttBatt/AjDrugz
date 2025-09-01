import re
import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables
load_dotenv()

# Required credentials
API_ID = int(getenv("API_ID", "26204186"))
API_HASH = getenv("API_HASH", "c277a7f93583f68d0fdfdcb68f5fc6c0")
BOT_TOKEN = getenv("BOT_TOKEN", "8209706073:AAEto_JFyBRJ7EhF2Jx3LzcH0MN6MOMpUC8")

# Bot and owner info
OWNER_USERNAME = getenv("OWNER_USERNAME", "li_xiaoyu_fan")
BOT_USERNAME = getenv("BOT_USERNAME", "Vc_music_x_bot")
BOT_NAME = getenv("BOT_NAME", "AjDrugz")
ASSUSERNAME = getenv("ASSUSERNAME", "music_assist")

# MongoDB
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ghosttbatt:Ghost2021@ghosttbatt.ocbirts.mongodb.net/?retryWrites=true&w=majority")

# Limits and IDs
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", "-1002275616383"))
OWNER_ID = int(getenv("OWNER_ID", "1281282633")) #7597135577 AJ-id

# Heroku
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
DEEP_API = getenv("DEEP_API")

# Git
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/GhosttBatt/HB-Drugz")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# Maximum Limit Allowed for users to save playlists on bot's server
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "3000"))

# Support
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/aj_bioo")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ARORA_X_MIRACHLE_NETWORK")
MUST_JOIN= getenv("MUST_JOIN", "aj_bioo")

# Assistant settings
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

# Song download limits
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

#Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST","False")
#Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", None)


# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# Playlist limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 2500))

# Telegram file limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# Session strings
STRING1 = getenv("STRING_SESSION", "BQCLLuYAGoFAM1P-3aKnlRPu0sJacpeJJg1FAD2eoG_tmqCHw403s4E9wLw7qPFuKJlcB_eexiFEumUUmKOXvgUsjYjGDHYYcrk4KxYgL7Y3RwFdytGuxHGYXJ_-HNNtD8-0hZcXle4A4L90SKbof0D5gfnbFxtsguv2v31i0Yk-uWN34QBb98VDm42xVJtnBQrXnukpk6xJZ-q8SifzqN682FdDkpD4IckmrdmtDMF3mrx69Hub4cgMxGGKJM8H4CXZi5O53oJp3wRi0B_mCSV_ziiLuCu5TMhND3zAeqOQEnJE31nAPrG-2lR3blfOoz04mZVxK46jP8LuKjhW3atR9Xu_8wAAAAHZWYemAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)

# Miscellaneous
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

DEBUG_IGNORE_LOG =True

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/qnx4wo.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/qnx4wo.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STATS_IMG_URL = "https://files.catbox.moe/qnx4wo.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/13afb9ee5c5da17930f1e.png"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/6c741a6bc1e1663ac96fc.jpg"

# Helper function
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

# Calculate total duration limit in seconds
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# Validate URLs
if SUPPORT_CHANNEL and not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHANNEL url is invalid. It must start with https://"
    )

if SUPPORT_CHAT and not re.match(r"(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - Your SUPPORT_CHAT url is invalid. It must start with https://"
    )
