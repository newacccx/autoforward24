from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "26556200"))
    API_HASH = environ.get("API_HASH", "3917b963bcc9a867097c4811af6ab39d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7642503054:AAFBZ9osd5cMdJCl1_p_WD8W9E_JZRD-d_U") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://newuser:newuser@cluster0.80t5h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "telegram")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6707921457').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
