#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__version__ = 0.1
__license__ = "The MIT License (MIT)"

import pandas as pd
from flask import Flask, json, current_app

infrastructure_provider = '**place_holder**'
data_source = 'https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/data/Coronavirus.current.csv'
data = pd.read_csv(data_source)
country_data = dict()
city_data = dict()
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
data['updated'] = pd.to_datetime(data['updated'], unit='ms')
data.fillna("Null", inplace=True)
app = Flask(__name__)


def gen_api_start_page(app):
    output = str()
    for route in app.url_map.iter_rules():
        if str(route) != '/' and 'static' not in str(route):
            output += '''
            <a href="%s">%s</a>
            <br>
            ''' % (route, route)
    output += '''
    <br><br>
    <b>Powered By %s
    ''' % infrastructure_provider

    return output


def get_country_data(df):
    country_df = df.loc[df['parent'] == 'global']
    country_raw_data = zip(country_df.label, country_df.updated, country_df.lat, country_df.lon, country_df.confirmed,
                           country_df.recovered, country_df.deaths)
    for entry in country_raw_data:
        country_data[entry[0]] = dict()
        country_data[entry[0]]['updated'] = entry[1]
        country_data[entry[0]]['lat'] = entry[2]
        country_data[entry[0]]['lon'] = entry[3]
        country_data[entry[0]]['confirmed'] = entry[4]
        country_data[entry[0]]['recovered'] = entry[5]
        country_data[entry[0]]['deaths'] = entry[6]
    return country_data


def get_city_data(df):
    city_df = df.loc[df['parent'] != 'global']
    city_raw_data = zip(city_df.parent, city_df.label, city_df.updated, city_df.lat, city_df.lon, city_df.confirmed,
                        city_df.recovered, city_df.deaths)
    for entry in city_raw_data:
        if entry[0] not in city_data.keys():
            city_data[entry[0]] = dict()
        city_data[entry[0]][entry[1]] = dict()
        city_data[entry[0]][entry[1]]['updated'] = entry[2]
        city_data[entry[0]][entry[1]]['lat'] = entry[3]
        city_data[entry[0]][entry[1]]['lon'] = entry[4]
        city_data[entry[0]][entry[1]]['confirmed'] = entry[5]
        city_data[entry[0]][entry[1]]['recovered'] = entry[6]
        city_data[entry[0]][entry[1]]['deaths'] = entry[7]
    return city_data


@app.route('/')
def api_get_start_page():
    return gen_api_start_page(app)


@app.route('/get/country/all')
def api_get_country_data():
    return current_app.response_class(
        json.dumps(get_country_data(data), indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


@app.route('/get/city/all')
def api_get_city_data():
    return current_app.response_class(
        json.dumps(get_city_data(data), indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")



@app.route('/get/country_by_name/<country>')
def api_get_country_data_by_name(country):
    return current_app.response_class(
        json.dumps(get_country_data(data)[country], indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


@app.route('/get/city_by_name/<country>/<city>')
def api_get_city_data_by_name(country, city):
    return current_app.response_class(
        json.dumps(get_city_data(data)[country][city], indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


if __name__ == '__main__':
    app.run()
