# app/core/config.py

# In a real app, load this from environment variables or a secure vault
SECRET_KEY = "a_very_secret_key_that_should_be_long_and_random"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30