from pathlib import Path
import logging 
import traceback 

logging.basicConfig(level=logging.INFO, filename="deleter.log", filemode="w", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

cwd = Path.cwd()
pattrn = "*.trashed-*"
matching_files = cwd.glob(pattrn)

for file in matching_files:
    try:
        file.unlink()
        print(f"File '{file} has been deleted'")
        logger.info(f"File '{file}' has been deleted")
    except Exception as e:
        print(f"File '{file}' could not be deleted because of an error. Please check the log file")
        logger.error(f"Error deleting `{file}` {traceback.format_exc()}")