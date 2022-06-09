import time

from bestchange_info_unpack.db.base import sync_create_con


def update_rate():
    con, cur = sync_create_con()
    cur.execute('INSERT ignore INTO rates (base_currency, target_currency, exchange_id, buy_price, sale_price, volume, min_order_size, max_order_size, city_id) '
                'SELECT base_currency, target_currency, exchange_id, buy_price, sale_price, volume, min_order_size, max_order_size, city_id FROM pure_rates ')
    con.commit()
    con.close()


def get_all():
    con, cur = sync_create_con()
    cur.execute('select * from rates ')
    city_list = cur.fetchall()
    con.close()
    return city_list


def dell_all():
    con, cur = sync_create_con()
    cur.execute('delete from rates ')
    con.commit()
    con.close()

