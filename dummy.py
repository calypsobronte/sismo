import json
import random
import os
from apistar import App, Route
from apistar import http

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

mydataDummy = [
    {
        'lugar': 'Bucaramanga',
        'magnitud': round(random.uniform(2,6), 2)
    },    
    {
        'lugar': 'Medellin',
        'magnitud': round(random.uniform(2,6), 2)
    },    
    {
        'lugar': 'Cali',
        'magnitud': round(random.uniform(2,6), 2)
    },    
    {
        'lugar': 'Bogotá',
        'magnitud': round(random.uniform(2,6), 2)
    },    
    {
        'lugar': 'Barranquilla',
        'magnitud': round(random.uniform(2,6), 2)
    },
    ]


def welcome(app: App, name=None):
    return app.render_template('index.html', name=name)

def api():
    #content = mydataDummy
    #headers = {'Content-Type': 'text/plain'}
    #return http.Response(content, headers=headers)
    data = mydataDummy[random.randint(0,4)]
    return data

#@app.route('/map')
def map():
    return app.render_template('map.html')


def city(city='medellin'):
    data = {
            'city_place': city,
            'city_magnitud': round(random.uniform(2,6), 2)
            },
    return data[0]

    


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/api', method='GET', handler=api),
    Route('/map', method='GET', handler=map),
    Route('/city', method='POST', handler=city),
]

app = App(routes=routes, template_dir=TEMPLATE_DIR, static_dir=STATIC_DIR)


if __name__ == '__main__':
    app.serve('0.0.0.0', 5000, debug=True)
