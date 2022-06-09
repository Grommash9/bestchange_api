from bestchange_info_unpack.db.base import sync_create_con


def insert_exchange(exchange):
    con, cur = sync_create_con()
    cur.execute('insert into exchange_names (exchange_id, exchange_name) '
                      'values (%s, %s) ON DUPLICATE KEY UPDATE exchange_name = %s; ',
                      (exchange['exchange_id'], exchange['exchange_name'], exchange['exchange_name']))
    con.commit()
    con.close()


def get_all():
    con, cur = sync_create_con()
    cur.execute('select * from exchange_names ')
    city_list = cur.fetchall()
    con.close()
    return city_list


def dell_all():
    con, cur = sync_create_con()
    cur.execute('delete from exchange_names ')
    con.commit()
    con.close()

