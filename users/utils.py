import random
import shutil
import string
from pathlib import Path

from fastapi import UploadFile, File

PATH_MEDIA = Path('media')


async def upload_file(file: UploadFile = File(...), upload_dir: Path = 'salom'):
    try:
        PATH_MEDIA.mkdir(parents=True, exist_ok=True)
        _, ext = file.filename.rsplit('.', 1)

        new_file = f'{_}_{"".join(random.choices(string.ascii_letters + string.digits, k=7))}.{ext}'

        if upload_dir:
            new_dir = PATH_MEDIA / upload_dir
            new_dir.mkdir(parents=True, exist_ok=True)
            new_file = f'{upload_dir}/{new_file}'

        file_path = PATH_MEDIA / new_file
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return {"file_path": file.filename}
    finally:
        file.file.close()
