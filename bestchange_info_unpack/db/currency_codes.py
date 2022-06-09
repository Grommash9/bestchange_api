from bestchange_info_unpack.db.base import sync_create_con


def insert_currency(currency):
    con, cur = sync_create_con()
    cur.execute('insert into currency_codes (currency_id, currency_code) '
                      'values (%s, %s) ON DUPLICATE KEY UPDATE currency_code = %s; ',
                      (currency['currency_id'], currency['currency_code'], currency['currency_code']))
    con.commit()
    con.close()


def get_all():
    con, cur = sync_create_con()
    cur.execute('select * from currency_codes ')
    city_list = cur.fetchall()
    con.close()
    return city_list


def dell_all():
    con, cur = sync_create_con()
    cur.execute('delete from currency_codes ')
    con.commit()
    con.close()

