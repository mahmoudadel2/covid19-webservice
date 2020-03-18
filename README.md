# covid19-webservice
Simple Python webservice to provide the latest statistics about Coronavirus COVID-19 in JSON format.

## Running local/dev


### Prerequisites

```
pip install -r requirements.txt
```

### Start the webservice

```
python -m covid19_webservice
```


## Running on Heroku


### Build an image and push

```
heroku container:login
heroku container:push web
```

### Run the container on Heroku

```
heroku container:release web
```


## Usage

I've listed the available endpoints in the webservice home page, e.g. `http://localhost:8080/`



## Examples

Getting a country by name (German):

```
curl http://localhost:8080/get/country/name/Ägypten
{
    "confirmed": 49, 
    "deaths": 1, 
    "lat": 26.0, 
    "lon": 30.0, 
    "recovered": 1, 
    "updated": "2020-03-08 19:03:11"
}
```

Getting a city by name (German):

```
curl http://localhost:8080/get/city/name/Deutschland/Bayern
{
    "confirmed": 200, 
    "deaths": 0, 
    "lat": 48.768814, 
    "lon": 11.658164999999999, 
    "recovered": 14, 
    "updated": "2020-03-08 17:00:00"
}
```
