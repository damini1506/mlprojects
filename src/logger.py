import logging
import os
from datetime import datetime

# 1. Define the filename ONLY (No path info here)
# It's cleaner to keep the extension here
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2. Define the folder path (Just the 'logs' directory)
logs_path = os.path.join(os.getcwd(), "logs")

# 3. Create the 'logs' folder if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# 4. Join them together: folder + filename
# Use the variable directly, don't wrap it in another f-string
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

