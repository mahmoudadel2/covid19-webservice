#!/usr/bin/env python
__author__ = 'Mahmoud Adel <mahmoud.adel2@gmail.com>'
__license__ = "The MIT License (MIT)"


import pandas as pd


data_source = 'https://interaktiv.morgenpost.de/corona-virus-karte-infektionen-deutschland-weltweit/data/Coronavirus.current.csv'
country_data = dict()
city_data = dict()
totals_data = dict()


def get_data_frame(ds):
    data = pd.read_csv(ds, encoding='utf-8')
    data['updated'] = pd.to_datetime(data['updated'], unit='ms')
    data.fillna("Null", inplace=True)
    return data


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
    city_dict = get_city_data(df)
    for country in city_dict.keys():
        country_data[country] = dict()
        counter = 0
        country_data[country]['confirmed'] = 0
        country_data[country]['recovered'] = 0
        country_data[country]['deaths'] = 0
        for city in city_dict[country].keys():
            country_data[country]['confirmed'] += city_dict[country][city]['confirmed']
            country_data[country]['recovered'] += city_dict[country][city]['recovered']
            country_data[country]['deaths'] += city_dict[country][city]['deaths']
            if city_dict[country][city]['confirmed'] > counter:
                counter = city_dict[country][city]['confirmed']
                top = city
        country_data[country]['updated'] = city_dict[country][top]['updated']
        country_data[country]['lon'] = city_dict[country][top]['lon']
        country_data[country]['lat'] = city_dict[country][top]['lat']

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


def get_total_statistics(df):
    country_dict = get_country_data(df)
    totals_data['confirmed'] = 0
    totals_data['recovered'] = 0
    totals_data['deaths'] = 0
    for country in country_dict.keys():
        totals_data['confirmed'] += country_dict[country]['confirmed']
        totals_data['recovered'] += country_dict[country]['recovered']
        totals_data['deaths'] += country_dict[country]['deaths']
    return totals_data
