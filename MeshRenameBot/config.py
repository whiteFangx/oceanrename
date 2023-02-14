from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://ok:ok@cluster0.ox6obby.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "f6c33f46599246676f75e153b615dbbc"]
        API_ID = [int, 4783634]
        BOT_TOKEN = [str, "6092663926:AAE124kuVPUZclLVZjiCT4-41O6ghIyrgPw"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 5]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[123456789]]
        OWNER_ID = [int, 0]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"t.me/fuckoff"]
        FORCEJOIN_ID = [int,-1001745287248]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
