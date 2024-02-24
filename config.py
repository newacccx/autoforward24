from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "6381607"))
    API_HASH = environ.get("API_HASH", "9799ad1623afe9bad664501f984b71fe")
    BOT_TOKEN = environ.get("BOT_TOKEN", "5123698683:AAHOhqg_k9tx48LNGk7B4JdaOJD3nkKLM-g") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://newuser:newuser@cluster0.80t5h.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "telegram")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1258695344').split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
