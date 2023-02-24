# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "27449839"))
API_HASH = os.getenv("API_HASH", "8c8ea28d8a537279c444dc338adb0952")
SESSION = os.getenv("SESSION", "BQAss6ZTo2Ft4HLk-he9yhcHiC61bPJ-eimT5BF5rCkNrTkoCsHm2oJ-cOQT07FStJE_6nlmvnqHLyYnnxSY1-_nccKmHJJfnv8P5exrHfbikkTJHI2iPR5pJdlFkJyK3WDB2U-zaXhTRAosknfWH6OppkvMbVFzwss8w3YjK4vuiBB4JRCxaQNY_sQgL0K1_rhI9prkytXhtc3T8rx5TWzTRkM8d9_PbCXiPFeQDjvHtdjV919D95ShXn4gbnYHAQp158H5ECDEyB5q1SSQqcWGDOvlwdjlzWsDfGkg7Daw83-tXaSZp84WTX9takT0LNlBQrHYnd0zV2QyxiZUC9IoAAAAAVjGw0oA")
OWNER = os.getenv("OWNER", "5784388426")
SUPPORT = os.getenv("SUPPORT", "TheDeadlyBots")
SUDO_USERS = list(map(int, os.getenv("5784388426").split()))
