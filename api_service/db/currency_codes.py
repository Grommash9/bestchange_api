from api_service.db.base import create_dict_con


async def get_all():
    con, cur = await create_dict_con()
    await cur.execute('select * from currency_codes ')
    currency_codes = await cur.fetchall()
    await con.ensure_closed()
    return currency_codes
