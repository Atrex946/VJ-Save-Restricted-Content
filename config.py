import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29412591"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "bc5652168138eeaf562cac0752c4b48e")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://williamfod55:<JFrYkVAvsJcTguin>@cluster.ootgpxb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster")