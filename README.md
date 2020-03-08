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


## Running on production


### Build an image

```
docker build -t covid19-webservice .
```

### Run the container

```
docker run -d --name covid19-webservice -p 8080:8080 covid19-webservice
```

