import urllib.request, os, base64
BASE='https://raw.githubusercontent.com/emiliofos/fos-carrusel-20260914/main/wb/'
os.makedirs('/home/user/carousel', exist_ok=True)
def run_slide(n, count):
    for i in range(count):
        url=f'{BASE}s{n}_{i:02d}.py'
        code=urllib.request.urlopen(url, timeout=60).read().decode()
        exec(code, {'__name__':'__main__'})
    b64=open(f'/home/user/carousel/slide-0{n}.b64').read()
    raw=base64.b64decode(b64)
    path=f'/home/user/carousel/slide-0{n}.jpg'
    open(path,'wb').write(raw)
    print('decoded', n, len(raw), path)
    return path
print('runner ready')
