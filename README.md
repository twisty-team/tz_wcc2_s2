# Ndao atakalo
Techzara wcc 2nd edition, week 2

A REST API that allow people to exchange their toys.

# Prerequisites
You'll need python 3 in order to run the project.
To install the dependencies, run (preferably in a virtual environment):
```sh
pip3 install -r requirements.txt
```

# How to run
Before the first run, you'll need to setup the database.
```sh
python3 manage.py migrate
```
Then, run the project by typing in the terminal :
``` sh
python3 manage.py runserver
```
The server will be launch on 127.0.0.1:8000 by default but you can specify
a host and a port as following :
```sh
python3 manage.py runserver 0.0.0.0:3000
```

# API reference
## Base url
The default base url is [localhost:8000](http://localhost:8000), but if you specified a custom host when
you run the project, the specified host is the base url.

## Authentication
The only endpoint that require authentication is the endpoint for deactivation an exchange.
The authorization token need to be provided in an Authorization header as you can see in the
endpoints section further below.

## Errors
Errors are returned as JSON objects in the following base format : 
```json
{
    "error": "400 Bad Request",
    "message": "This exchange is already inactive"
}
```

## Endpoints
* `POST /api/exchanges`
    * Create a new exchange using the `user_name`, `contact`, `desired_toy`, `toy_to_change` and `pictures` of the toy to change from a formdata. `user_name` and `contact` must be unique. It it's the first time a user post an exchange, a `token` is returned. This token will be used to deactivate an exchange.
    * Example request :

```curl
curl --location --request POST 'localhost:3000/api/exchanges' \ 
--form 'user_name="genos"' \
--form 'contact="0384238111"' \
--form 'desired_toy="Toupis"' \
--form 'toy_to_change="Kalesa"' \
--form 'pictures=@"/home/gracy/Pictures/st,small,507x507-pad,600x600,f8f8f8.jpg"' \
--form 'pictures=@"/home/gracy/Pictures/mpv-shot0064.jpg"'
```

```json
{
    "token": "ES2ARI0Z15BVYKFHMVJOJIVAWIGI1KY1",
    "message": "Store this token somewhere secure as you will need to provide it in an Authorization header in order to deactivate an exchange.",
    "exchange_id": 14
}
```
* `GET /api/exchanges`
    * Return a list of active exchanges.
    * You can provide an optional query parameter to specify a page : `GET /exchanges?page=2`
    * Example request : 
```
curl --location --request GET 'localhost:3000/api/exchanges?page=2'
```
```json
{
    "count": 12,
    "next": null,
    "previous": "http://localhost:3000/api/exchanges",
    "results": [
        {
            "id": 11,
            "pictures": [
                {
                    "image_url": "/media/uploads/293492135_2440118852797767_8639598829188177040_n_w4VFO5A.jpg"
                }
            ],
            "owner": {
                "name": "rakoto",
                "contact": "0384238111"
            },
            "toy_to_change": "Cheval en bois",
            "desired_toy": "Yo-yo",
            "active": true
        },
        {
            "id": 12,
            "pictures": [
                {
                    "image_url": "/media/uploads/293492135_2440118852797767_8639598829188177040_n_axV3y7k.jpg"
                }
            ],
            "owner": {
                "name": "rabe",
                "contact": "0344238110"
            },
            "toy_to_change": "Kalesa",
            "desired_toy": "Toupis",
            "active": true
        },
    ]
}
```
* `PATCH /api/exchanges/{exchange_id}`
    * Deactivate an exchange based on `exchange_id`
    * Example request :
```curl
curl --location --request PATCH 'localhost:3000/api/exchanges/14' \
--header 'Authorization: Bearer WUZ6C9V75DBUVN351H029JPXIIFCQ5YB '
```
```json
{
    "message": "exchange deactivated successfuly",
    "exchange_id": 14
}
```

# Authors

* [tbgracy](https://github.com/tbgracy)

* [rhja](https://github.com/radoheritiana)