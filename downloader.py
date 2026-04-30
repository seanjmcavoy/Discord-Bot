import os
import tempfile
import time
from yt_dlp.utils import DownloadError
import discord
import yt_dlp
#keep below 8MB
#use mp4 if possible for iphones lol
primary_format = (
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


def downloader(link, name):
    temp_dir_path = "./temp"
    if name == "":
        name = str(int(round(time.time()* 1000)))

    try:
        os.makedirs(temp_dir_path, exist_ok=True)
    except OSError as e:
        print(f"Mkdir failure: {e}")
        return None

    with tempfile.TemporaryDirectory(dir=temp_dir_path) as tmpdir:
        ydl_opts = {
            'format': f"{primary_format}",
            'merge_output_format': 'mp4',
            'restrict_filenames': True,
            'postprocessor_args': {
                'ffmpeg': [
                    '-threads', '1',
                    '-preset', 'ultrafast',
                ]
            },
            'quiet': True,
            'no_warnings': True,
            "max_filesize": 8 * 1024 * 1024,
            'outtmpl': os.path.join(tmpdir, f'{name}.%(ext)s'),
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
        except DownloadError as e:
            print(f"Download Error: {e}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None

        files_to_send: list[discord.File] = []
        try:
            for send_file in os.listdir(tmpdir):
                with open(os.path.join(tmpdir, send_file), 'rb') as f:
                    files_to_send.append(discord.File(f, filename=f'{send_file}'))
            return files_to_send
        except Exception as e:
            print(f"Error: {e}")
            return None

