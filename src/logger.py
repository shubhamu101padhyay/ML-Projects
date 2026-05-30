import logging
import os
from datetime import datetime

# 1. Sirf file ka naam create kiya
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# 2. Sirf 'logs' folder ka path banaya (bina file name ke)
logs_path = os.path.join(os.getcwd(), "logs")

# 3. 'logs' naam ka folder create kiya agar nahi hai toh
os.makedirs(logs_path, exist_ok=True)

# 4. Folder aur File name ko join karke final file path banaya
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s  %(lineno)d %(name)s - %(levelname)s - %(message)s]",
    level=logging.INFO
)

# 5. Syntax aur dunder name sahi kiya
if __name__ == "__main__":
    logging.info("Logging has started")