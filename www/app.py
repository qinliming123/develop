import asyncio
from aiohttp import web

#创建函数，用于管理URL，主要用于后面URL的绑定
async def index(request):
    #返回值用于构建响应
    return web.Response(body='<h1>Welcome</h1>'.encode('utf-8'),content_type='text/html')

#创建web服务器，用于处理URL和http协议
async def init(loop):
    app = web.Application()
    app.router.add_route('GET','/',index)
    #调用协程创建监听服务
    srv = await loop.create_server(app._make_handler(),'127.0.0.1',8000)
    print('http://127.0.0.1:8000')
    return srv

#创建协程
loop = asyncio.get_event_loop()
#运行协程，直至函数结束
loop.run_until_complete(init(loop))
loop.run_forever()
