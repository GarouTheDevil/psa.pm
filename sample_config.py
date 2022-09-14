import os 

class Config(object):

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1478357602").split())
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    LOG_CHAN = int(os.environ.get("LOG_CHAN", "-1001145342921"))
    UPDATE_CHANNEL = "DevilBotz"
    USERNAME = os.environ.get("USERNAME", "Stay007") 
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    ADL_BOT_RQ = {}
