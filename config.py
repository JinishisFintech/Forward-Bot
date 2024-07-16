from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "b28dce0d39b0c6de758504f1ce7a47dd")
      API_ID = int(getenv("API_ID", "22663700"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7400842411:AAHcbbJDLdZ0BTMfzk0VGHG5pmNeb4720EY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002233847705:-1002212743926").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
