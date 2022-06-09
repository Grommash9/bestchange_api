import datetime
import time

from bestchange_info_unpack.db.base import sync_create_con


def update_rate():
    con, cur = sync_create_con()
    cur.execute('INSERT INTO rates'
        '(base_currency,'
         'target_currency,'
         'exchange_id,'
         'buy_price,'
         'sale_price,'
         'volume,'
         'min_order_size,'
         'max_order_size,'
         'city_id,'
         'updated_at) '
'  SELECT base_currency,'
         'target_currency,'
         'exchange_id,'
         'buy_price,'
         'sale_price,'
         'volume,'
         'min_order_size,'
         'max_order_size,'
         'city_id,'
         'CURRENT_TIMESTAMP()'
  'FROM pure_rates '
'ON DUPLICATE KEY UPDATE '
     'rates.buy_price = pure_rates.buy_price,'
     'rates.sale_price = pure_rates.sale_price,'
     'rates.volume = pure_rates.volume,'
     'rates.min_order_size = pure_rates.min_order_size,'
     'rates.max_order_size = pure_rates.max_order_size,'
     'rates.updated_at = CURRENT_TIMESTAMP() ')
    cur.execute(f'DELETE FROM rates WHERE updated_at < (NOW() - INTERVAL 2 MINUTE)')
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

