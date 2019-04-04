#创建一个全局连接池，连接池由全局变量_pool存储

import asyncio,logging
import aiomysql

async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host = kw.get('host','localhost'),
        port = kw.get('port',3306),
        user = kw['user'],
        password = kw['paaaword'],
        db = kw['db'],
        charset = kw.get('charset','utf-8'),
        autocommit = kw.get('autocommit',10),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )


#select函数
async def select(sql, args, size=None):
    logging.log(sql,args)
    global __pool
    with(await __pool) as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        await cur.excute(sql.replace('?','%s'),args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs