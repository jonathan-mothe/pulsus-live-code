# Preparando o ambiente python

```python3 -m venv venv```

```pip install -r requeriments.txt```


# Endpoints

GET - (http://127.0.0.1:5000/devices)
POST - (http://127.0.0.1:5000/devices/add)

## Corpo da requisição (POST)
```
{
	"id":27,
	"location_lat":29.55555,
	"location_long":28.3333
}
```
