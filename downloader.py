import io
import logging
import os
import tempfile
import time
from yt_dlp.utils import DownloadError
import discord
import yt_dlp
#keep below 8MB
#use mp4 if possible for iphones lol

primary_formats = (
    "bv*[filesize<8M][ext=mp4][vcodec~='^((he|a)vc|h26[45])'] +ba*[filesize<2M][ext=m4a] / "
    "bv*[filesize<8M][ext=mp4][vcodec~='^((he|a)vc|h26[45])'] +ba*[filesize<2M][ext=mp4] / "
    "bv*[filesize<7M][ext=mp4][vcodec~='^((he|a)vc|h26[45])'] +ba*[filesize<3M] / "
    "bv*[filesize<6M][ext=mp4][vcodec~='^((he|a)vc|h26[45])'] +ba*[filesize<4M] /"
    "v*[filesize<7M][vcodec~='^((he|a)vc|h26[45])'] + a*[filesize<3M] / "
    "b[filesize<10M] / "
    "bv*[filesize<7M]+ba*[filesize<3M] / "
    "bv*+ba / "
    "b"
    )
logger = logging.getLogger(__name__)

def downloader(link, name):
    temp_dir_path = "./temp"
    if name == "":
        name = str(int(round(time.time()* 1000)))
    logger.info("download requested: link=%s name=%s", link, name)

    try:
        os.makedirs(temp_dir_path, exist_ok=True)
    except OSError as e:
        logger.error("failed to create temp dir: %s: %s", temp_dir_path, e)
        raise

    with tempfile.TemporaryDirectory(dir=temp_dir_path) as tmpdir:
        ydl_opts = {
            'format': f"{primary_formats}",
            'merge_output_format': 'mp4',
            'restrict_filenames': True,
            'remote_components': ['ejs:github'],
            'postprocessor_args': {
                'ffmpeg': [
                    '-threads', '1',
                    '-preset', 'ultrafast',
                ]
            },
            'logger': logger,
            "max_filesize": 10 * 1024 * 1024,
            'outtmpl': os.path.join(tmpdir, f'{name}.%(ext)s'),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except DownloadError as e:
            logger.error(f"yt-dlp: {e}")
            raise
        except Exception as e:
            logger.error(f"Error: {e}")
            raise

        send_file = f"{name}.mp4"
        try:
            with open(os.path.join(tmpdir, send_file), 'rb') as f:
                data = f.read()
            buffer = io.BytesIO(data)
            buffer.seek(0)
            return discord.File(buffer, filename=f'{send_file}')
        except Exception as e:
            logger.error(f"File was not found: {e}")
            raise

