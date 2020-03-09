#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"

from covid19_webservice.data import data_processor
from flask import Flask, json, current_app

df = data_processor.data
service = Flask(__name__)


def gen_api_start_page(service):
    output = '<b>Available endpoints are:</b><br><br>'
    for route in service.url_map.iter_rules():
        if str(route) != '/' and 'static' not in str(route):
            output += '''
            <a href="%s">%s</a>
            <br>
            ''' % (route, route)
    return output


@service.route('/')
def api_get_start_page():
    return gen_api_start_page(service)


@service.route('/get/country/all')
def api_get_country_data():
    return current_app.response_class(
        json.dumps(data_processor.get_country_data(df), indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/country/name/<country>')
def api_get_country_data_by_name(country):
    return current_app.response_class(
        json.dumps(data_processor.get_country_data(df)[country], indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/city/all')
def api_get_city_data():
    response = data_processor.get_city_data(df)
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/city/name/<country>/<city>')
def api_get_city_data_by_name(country, city):
    response = data_processor.get_city_data(df)[country][city]
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/statistics/total')
def api_get_total_statistics():
    response = data_processor.get_total_statistics(df)
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")
