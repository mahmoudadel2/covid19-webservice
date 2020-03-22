#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"

from covid19_webservice.data import data_processor
from flask import Flask, json, current_app

from covid19_webservice.webservice import german

ds = data_processor.data_source

service = Flask(__name__)


def gen_service_start_page(service):
    output = '<b>Available endpoints are:</b><br><br>'
    for route in service.url_map.iter_rules():
        if str(route) != '/' and 'static' not in str(route):
            output += '''
            <a href="%s">%s</a>
            <br>
            ''' % (route, str(route).replace('<', '&lt;').replace('>', '&gt;'))
    return output


def translate_and_normalize(original_name):
    name_english = original_name.capitalize()
    return german.gettext(name_english).lower()


@service.route('/')
def service_get_start_page():
    return gen_service_start_page(service)


@service.route('/get/country/all')
def service_get_country_data():
    df = data_processor.get_data_frame(ds)
    return current_app.response_class(
        json.dumps(data_processor.get_country_data(df), indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/country/name/<country>')
def service_get_country_data_by_name(country):
    country = translate_and_normalize(country)
    df = data_processor.get_data_frame(ds)
    return current_app.response_class(
        json.dumps(data_processor.get_country_data(df)[country], indent=4, sort_keys=True,
                   default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/city/all')
def service_get_city_data():
    df = data_processor.get_data_frame(ds)
    response = data_processor.get_city_data(df)
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str, ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/city/name/<country>/<city>')
def service_get_city_data_by_name(country, city):
    country = translate_and_normalize(country)
    city = translate_and_normalize(city)
    df = data_processor.get_data_frame(ds)
    response = data_processor.get_city_data(df)[country][city]
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/statistics/all')
def service_get_all_statistics():
    df = data_processor.get_data_frame(ds)
    response = data_processor.get_total_statistics(df)
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/statistics/confirmed')
def service_get_confirmed():
    df = data_processor.get_data_frame(ds)
    response = {'confirmed': data_processor.get_total_statistics(df)['confirmed']}
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/statistics/recovered')
def service_get_recovered():
    df = data_processor.get_data_frame(ds)
    response = {'recovered': data_processor.get_total_statistics(df)['recovered']}
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")


@service.route('/get/statistics/deaths')
def service_get_deaths():
    df = data_processor.get_data_frame(ds)
    response = {'deaths': data_processor.get_total_statistics(df)['deaths']}
    return current_app.response_class(
        json.dumps(response, indent=4, sort_keys=True, default=str,
                   ensure_ascii=False),
        mimetype="application/json")
