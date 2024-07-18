import json
import pytest
import requests
import os
with open('test_data.json', 'r') as test_data:
    data = json.load(test_data)

post_link = os.environ['api_post']
token_link = os.environ['api_token']

@pytest.fixture()
def token():
    response_token = requests.post(token_link)
    return 'token=' + response_token.cookies['token']


class Payload:
    def payload_3(self, line):
        self.payload = {
            'title': data[line]['title'],
            'lat': data[line]['lat'],
            'lon': data[line]['lon'],
        }
        return self.payload

    def payload_all(self, line):
        self.payload = {
            'title': data[line]['title'],
            'lat': data[line]['lat'],
            'lon': data[line]['lon'],
            'color': data[line]['color'],
        }
        return self.payload


class CreatingFav:


    def new_favs(self, post_link, payload, token):
        self.response = requests.post(
            post_link,
            data=payload,
            headers={'Cookie': token}
        )
        return self.response

    def new_favs_3(self, post_link, line, token):
        self.response = requests.post(
            post_link,
            data=Payload().payload_3(line),
            headers={'Cookie': token}
        )
        return self.response

    def new_favs_all(self, post_link, line, token):
        self.response = requests.post(
            post_link,
            data=Payload().payload_all(line),
            headers={'Cookie': token}
        )
        return self.response



    def check_token(self):
        assert self.response.json()['error']['message'] == "Передан несуществующий или «протухший» 'token'"


    def check_status_is_401(self):
        assert self.response.status_code == 401

    def check_status_is_200(self):
        assert self.response.status_code == 200

    def check_status_is_400(self):
        assert self.response.status_code == 400

    def check_title(self, payload):
        assert self.response.json()['title'] == payload['title']

    def check_lat(self, payload):
        assert self.response.json()['lat'] == payload['lat']

    def check_lon(self, payload):
        assert self.response.json()['lon'] == payload['lon']

    def check_color(self, payload):
        assert self.response.json()['color'] == payload['color']

    def check_time(self, time_utc):
        assert self.response.json()['created_at'] == time_utc

    def check_title_error(self):
        assert self.response.json()['error']['message'] == "Параметр 'title' является обзательным"

    def check_lat_error(self):
        assert self.response.json()['error']['message'] == "Параметр 'lat' является обязательным"

    def check_lon_error(self):
        assert self.response.json()['error']['message'] == "Параметр 'lon' является обязательным"

    def check_title_len_error(self):
        assert self.response.json()['error']['message'] == "Параметр 'title' должен содержать не более 999 символов"

    def check_lat_value(self):
        assert self.response.json()['error']['message'] == "Параметр 'lat' должен быть не более 90"

    def check_lon_value(self):
        assert self.response.json()['error']['message'] == "Параметр 'lon' должен быть не более 180"

    def check_lat_value_neg(self):
        assert self.response.json()['error']['message'] == "Параметр 'lat' должен быть не менее -90"

    def check_lon_value_neg(self):
        assert self.response.json()['error']['message'] == "Параметр 'lon' должен быть не менее -180"

    def check_color_value(self):
        assert self.response.json()['error'][
                   'message'] == "Параметр 'color' может быть одним из следующих значений: BLUE, GREEN, RED, YELLOW"

    def show_description(self, line):
        print('test_data:', data[line]['description'])

    def show_status_code(self):
        print('status_code:', self.response.status_code)

    def show_created_at(self):
        print('created_at:', self.response.json()['created_at'])

    def show_len_title(self):
        print('len_title:', len(self.response.json()['title']))
