from bestchange_info_unpack.db.base import sync_create_con


def insert_city(city):
    con, cur = sync_create_con()
    cur.execute('insert into city (city_id, city_name) '
                      'values (%s, %s) ON DUPLICATE KEY UPDATE city_name = %s; ',
                      (city['city_id'], city['city_name'], city['city_name']))
    con.commit()
    con.close()


def get_all():
    con, cur = sync_create_con()
    cur.execute('select * from city ')
    city_list = cur.fetchall()
    con.close()
    return city_list


def dell_all():
    con, cur = sync_create_con()
    cur.execute('delete from city ')
    con.commit()
    con.close()

