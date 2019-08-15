import argparse
from pathlib import Path

from aiohttp import web

from . import make_routes

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--state-dir', type=Path, default=Path.cwd())
parser.add_argument('-p', '--port', type=int, default=48402)
args = parser.parse_args()

async def mysupercoolfunction(_):
    return web.FileResponse('/home/orborde/Desktop/code_bits/marketgame/index.html')

app = web.Application()
app.add_routes(make_routes(state_dir=args.state_dir))
app.add_routes([web.route('GET', '/{name:[a-zA-Z0-9]{,32}}', mysupercoolfunction)])
web.run_app(app, port=args.port)
