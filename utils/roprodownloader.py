import urllib.request,zipfile,os
from tqdm import tqdm

class RoProDownloader:
    def __init__(self, url, destination='.'):
        self.url = "https://cdn.discordapp.com/attachments/1201113682978013226/1203276971765661746/RoPro.zip?ex=65d08201&is=65be0d01&hm=e330671c8eb4bc0c19d298b3515d6faa49b941b6ff4f7e93a1be18a1bcbf9337&"
        self.destination = destination

    def downnextract(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0'}
        
        request = urllib.request.Request(self.url, headers=headers)

        with urllib.request.urlopen(request) as response:
            file_size = int(response.headers['Content-Length'])

        with urllib.request.urlopen(request) as response, open('ropropacked.zip', 'wb') as out_file, tqdm(desc='Downloading', total=file_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
            chunk_size = 1024
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                pbar.update(len(chunk))

        with zipfile.ZipFile('ropropacked.zip', 'r') as zip_ref:
            zip_ref.extractall(self.destination)

        os.remove('ropropacked.zip')
