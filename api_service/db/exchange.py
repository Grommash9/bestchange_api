from api_service.db.base import create_dict_con


async def get_all():
    con, cur = await create_dict_con()
    await cur.execute('select * from exchange_names ')
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


