from bestchange_info_unpack.db.base import sync_create_con


def insert_currency(currency):
    con, cur = sync_create_con()
    cur.execute('insert into currency_names (currency_id, currency_name) '
                      'values (%s, %s) ON DUPLICATE KEY UPDATE currency_name = %s; ',
                      (currency['currency_id'], currency['currency_name'], currency['currency_name']))
    con.commit()
    con.close()


def get_all():
    con, cur = sync_create_con()
    cur.execute('select * from currency_names ')
    city_list = cur.fetchall()
    con.close()
    return city_list


def dell_all():
    con, cur = sync_create_con()
    cur.execute('delete from currency_names ')
    con.commit()
    con.close()

