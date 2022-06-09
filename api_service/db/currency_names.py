from api_service.db.base import create_dict_con


async def get_all():
    con, cur = await create_dict_con()
    await cur.execute('select * from currency_names ')
    currency_names = await cur.fetchall()
    await con.ensure_closed()
    return currency_names