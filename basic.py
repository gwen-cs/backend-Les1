from dotenv import load_dotenv
import os


load_dotenv()

secret_key = os.getenv("FLASK_SECRET_KEY")

print(secret_key)