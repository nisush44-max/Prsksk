from os import environ

API_ID = int(environ.get("API_ID", "37502609"))
API_HASH = environ.get("API_HASH", "cd4e39a4344aad8946b904292abbdf14")
BOT_TOKEN = environ.get("BOT_TOKEN", "8611961334:AAGAdtZtIqo9u083Wo_eEnAgcGJKCmYoXFk")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003835007743"))
ADMINS = int(environ.get("ADMINS", "8363262755"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://synaxbots:synaxbotsalways#123@cluster0.nessphe.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = environ.get('NEW_REQ_MODE', 'false').strip().lower() in ('1', 'true', 'yes', 'on')
