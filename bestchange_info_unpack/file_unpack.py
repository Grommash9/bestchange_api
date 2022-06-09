import datetime
import hashlib
import os
import threading
import time
from io import StringIO
from sqlalchemy import create_engine
import pandas as pd
from threading import Thread
from bestchange_info_unpack import config, db
import zipfile


def city_unpack(archive):
    bm_cities = archive.read('bm_cities.dat').decode('WINDOWS-1251')
    new_city_dict = dict()
    for city_data in bm_cities.split('\n'):
        new_city_dict[int(city_data.split(';')[0])] = city_data.split(';')[1]
    new_city_dict[0] = 'null'
    old_city_dict = dict()
    for city in db.city.get_all():
        old_city_dict[city['city_id']] = city['city_name']

    if new_city_dict != old_city_dict:
        for city_id, city_name in new_city_dict.items():
            db.city.insert_city({'city_id': city_id,
                                 'city_name': city_name})


def currency_codes_unpack(archive):
    bm_cycodes = archive.read('bm_cycodes.dat').decode('WINDOWS-1251')
    new_bm_cycodes = dict()
    for currency_data in bm_cycodes.split('\n'):
        new_bm_cycodes[int(currency_data.split(';')[0])] = currency_data.split(';')[1]
    old_bm_cycodes = dict()
    for currency in db.currency_codes.get_all():
        old_bm_cycodes[currency['currency_id']] = currency['currency_code']
    if new_bm_cycodes != old_bm_cycodes:
        for currency_id, currency_code in new_bm_cycodes.items():
            db.currency_codes.insert_currency({'currency_id': currency_id,
                                 'currency_code': currency_code})


def currency_names_unpack(archive):
    bm_cycodes = archive.read('bm_cy.dat').decode('WINDOWS-1251')
    new_bm_cynames = dict()
    for currency_data in bm_cycodes.split('\n'):
        new_bm_cynames[int(currency_data.split(';')[0])] = currency_data.split(';')[2]
    old_bm_cynames = dict()
    for currency in db.currency_names.get_all():
        old_bm_cynames[currency['currency_id']] = currency['currency_name']

    if new_bm_cynames != old_bm_cynames:
        for currency_id, currency_name in new_bm_cynames.items():
            db.currency_names.insert_currency({'currency_id': currency_id,
                                           'currency_name': currency_name})


def exchanges_names_unpack(archive):
    bm_exch = archive.read('bm_exch.dat').decode('WINDOWS-1251')
    new_bm_exch = dict()
    for exchange_data in bm_exch.split('\n'):
        new_bm_exch[int(exchange_data.split(';')[0])] = exchange_data.split(';')[1]
    old_new_bm_exch = dict()
    for exchange in db.exchange.get_all():
        old_new_bm_exch[exchange['exchange_id']] = exchange['exchange_name']

    if new_bm_exch != old_new_bm_exch:
        for exchange_id, exchange_name in new_bm_exch.items():
            db.exchange.insert_exchange({'exchange_id': exchange_id,
                                               'exchange_name': exchange_name})


def rates_unpack(archive):
    bm_rates = archive.read('bm_rates.dat').decode('WINDOWS-1251')
    csvStringIO = StringIO(bm_rates)
    df = pd.read_csv(csvStringIO, sep=";", header=None)
    my_conn = create_engine("mysql+mysqldb://root:root@localhost/bestchange_api_db")
    df.rename(columns={0: 'base_currency',
                       1: 'target_currency',
                       2: 'exchange_id',
                       3: 'buy_price',
                       4: 'sale_price',
                       5: 'volume',
                       6: 'unknown',
                       7: 'reviews',
                       8: 'min_order_size',
                       9: 'max_order_size',
                       10: 'city_id'}, inplace=True)
    df.to_sql("pure_rates", my_conn, if_exists='replace', index=False)



def file_unpack():
    # old_md5 = config.redis.get('list_md5')
    # current_md5 = hashlib.md5(open(os.path.join(config.BASE_DIR, 'info.zip'), 'rb').read()).hexdigest()
    #
    # if old_md5 != current_md5:
    #     config.redis.set('list_md5', current_md5)
    #     print(f'get new {datetime.datetime.now()}')


    archive = zipfile.ZipFile(os.path.join(config.BASE_DIR, 'info.zip'), 'r')
    # Let us verify the operation.
    start_time = time.time()

    city_unpack(archive)
    currency_codes_unpack(archive)
    currency_names_unpack(archive)
    exchanges_names_unpack(archive)
    rates_unpack(archive)
    db.rates.update_rate()
    print(time.time() - start_time)

    # currency_codes_dict = dict()
    # bm_cycodes = archive.read('bm_cycodes.dat').decode("utf-8")
    #
    # for currency in bm_cycodes.split('\n'):
    #     currency_data = currency.split(';')
    #     currency_codes_dict[currency_data[0]] = currency_data[1]
    #
    #
    # bm_exch_dict = dict()
    # bm_exch = archive.read('bm_exch.dat').decode('WINDOWS-1251')
    # for exchange in bm_exch.split('\n'):
    #     exchange_data = exchange.split(';')
    #     bm_exch_dict[exchange_data[0]] = exchange_data[1]
    #
    # bm_rates = archive.read('bm_rates.dat').decode('utf-8')
    # for rates in bm_rates.split('\n'):
    #
    #     rates_data = rates.split(';')
    #     base_currency, target_currency, exchange_id, buy_price, sale_price, volume, min_order_size, max_order_size, city_id =\
    #         rates_data[0], rates_data[1], rates_data[2], rates_data[3], rates_data[4], rates_data[5], rates_data[8], rates_data[9] , rates_data[10]
    #     #TRX, MONOBUAH, BitExchanger,1, 2.6411777, 14332893, 0.5763, 1, 1317.594, 1317594.0424
    #
    #
    #
    #     print(f"base_currency: {currency_codes_dict[base_currency]} "
    #           f"target_currency: {currency_codes_dict[target_currency]} "
    #           f"exchange_id: {bm_exch_dict[exchange_id]} "
    #           f"sale price: {buy_price} "
    #           f"sale price: {sale_price}"
    #           f"volume: {volume} "
    #           f"min_order_size: {min_order_size} "
    #           f"max_order_size: {max_order_size} "
    #           f"city_id {city_id}")


