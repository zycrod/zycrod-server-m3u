from fastapi import FastAPI, Response
app=FastAPI(title='ZYCROD Server M3U')

@app.get('/health')
def health():
    return {'status':'ok'}

@app.get('/playlist/live.m3u')
def playlist():
    return Response('#EXTM3U\n', media_type='audio/x-mpegurl')
