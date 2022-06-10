from api_service.db.base import create_dict_con


async def get_for_pair(base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size):
    con, cur = await create_dict_con()
    await cur.execute("select volume, IF(buy_price != '1', buy_price, sale_price) as price, "
                        'min_order_size, max_order_size, exchange_names.exchange_name as exchange_name, '
                        "exchange_names.exchange_id as exchange_id, IF(city_id != 0, city_id, null) as city_id, updated_at "
                        'from rates '
                        'join exchange_names '
                        'on exchange_names.exchange_id = rates.exchange_id '
                        'where base_currency = %s and target_currency = %s and volume > %s and volume < %s '
                      'and min_order_size > %s and max_order_size < %s',
                      (base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


async def get_pair_in_city(base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size, city_id):
    con, cur = await create_dict_con()
    await cur.execute("select volume, IF(buy_price != '1', buy_price, sale_price) as price, "
                        'min_order_size, max_order_size, exchange_names.exchange_name as exchange_name, '
                        "exchange_names.exchange_id as exchange_id, IF(city_id != 0, city_id, null) as city_id, updated_at "
                        'from rates '
                        'join exchange_names '
                        'on exchange_names.exchange_id = rates.exchange_id '
                        'where base_currency = %s and target_currency = %s and volume > %s and volume < %s '
                      'and min_order_size > %s and max_order_size < %s and city_id = %s ',
                      (base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size, city_id))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


async def get_all_from_city(city_id):
    con, cur = await create_dict_con()
    await cur.execute("select volume, IF(buy_price != '1', buy_price, sale_price) as price, "
                        'min_order_size, max_order_size, exchange_names.exchange_name as exchange_name, '
                        "exchange_names.exchange_id as exchange_id, IF(city_id != 0, city_id, null) as city_id,"
                      "base_currency_name.currency_id as base_currency_id, target_currency_name.currency_currency_idname as target_currency_id, "
                      "base_currency_name.currency_name as base_currency, target_currency_name.currency_name as target_currency, updated_at "
                        'from rates '
                        'join exchange_names '
                        'on exchange_names.exchange_id = rates.exchange_id '
                        'join currency_names as base_currency_name '
                        'on base_currency_name.currency_id = rates.base_currency '
                          'join currency_names as target_currency_name '
                          'on target_currency_name.currency_id = rates.target_currency '
                        'where city_id = %s ',
                      (city_id,))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


async def get_rate_for_pair(base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size):
    con, cur = await create_dict_con()
    await cur.execute("select volume as v, IF(buy_price != '1', buy_price, sale_price) as p, "
                        'min_order_size as mins, max_order_size as maxs, '
                        "exchange_id as e_id, IF(city_id != 0, city_id, null) as c, updated_at as t "
                        'from rates '
                        'where base_currency = %s and target_currency = %s and volume > %s and volume < %s '
                      'and min_order_size > %s and max_order_size < %s',
                      (base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


async def get_all_rate_pair_in_city(city_id):
    con, cur = await create_dict_con()
    await cur.execute("select volume as v, IF(buy_price != '1', buy_price, sale_price) as p, "
                      'min_order_size as mins, max_order_size as maxs, exchange_id as e_id, '
                      "city_id as c, updated_at as t "
                      'from rates '
                      'where city_id = %s ',
                      (city_id,))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list


async def get_rate_pair_in_city(base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size, city_id):
    con, cur = await create_dict_con()
    await cur.execute("select volume as v, IF(buy_price != '1', buy_price, sale_price) as p, "
                        'min_order_size as mins, max_order_size as maxs, '
                        "exchange_id as e_id, city_id as c, updated_at as t "
                        'from rates '
                        'where base_currency = %s and target_currency = %s and volume > %s and volume < %s '
                      'and min_order_size > %s and max_order_size < %s and city_id = %s ',
                      (base_currency, target_currency, min_volume, max_volume, min_order_size, max_order_size, city_id))
    exchange_list = await cur.fetchall()
    await con.ensure_closed()
    return exchange_list
