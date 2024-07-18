import requests
import time
import json
import allure
from datetime import datetime, timezone
from post_endpoint import Payload, CreatingFav, token, post_link, token_link
with open('test_data.json', 'r') as test_data:
    data = json.load(test_data)


payloads = Payload()
create = CreatingFav()


@allure.feature('Token lifetime')
def test_creating_favs_old_token(token):
    line = 0
    token_old = 'token=' + requests.post(
        token_link
    ).cookies['token']
    token_lifetime = 2.001
    time.sleep(token_lifetime)
    create.new_favs_3(post_link, line, token_old)
    create.check_token()
    create.check_status_is_401()


@allure.feature('Timestamp format')
def test_creating_favs_as_example(token):
    line = 0
    create.new_favs_3(post_link, line, token)
    time_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    create.show_description(line)
    create.show_status_code()
    create.show_created_at()
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()
    create.check_time(time_utc)


@allure.feature('Required fields')
def test_creating_favs_title_null(token):
    line = 1
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_title_error()
    create.check_status_is_400()


@allure.feature('Required fields')
def test_creating_favs_lat_null(token):
    line = 2
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lat_error()
    create.check_status_is_400()


@allure.feature('Required fields')
def test_creating_favs_lon_null(token):
    line = 3
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lon_error()
    create.check_status_is_400()


@allure.feature('Title field')
def test_creating_favs_one_len_title(token):
    line = 4
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_capital_title(token):
    line = 5
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_rus_title(token):
    line = 6
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_arm_title(token):
    line = 7
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_ch_title(token):
    line = 8
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_num_title(token):
    line = 9
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_dot_title(token):
    line = 10
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_hash_title(token):
    line = 11
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Title field')
def test_creating_favs_999_titles(token):
    line = 31
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()
    create.show_len_title()


@allure.feature('Title field')
def test_creating_favs_1000_titles(token):
    line = 32
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_created_at()
    create.show_status_code()
    create.check_title_len_error()
    create.check_status_is_400()


@allure.feature('Title field')
def test_creating_favs_1001_titles(token):
    line = 33
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_title_len_error()
    create.check_status_is_400()


@allure.feature('Coordinate fields')
def test_creating_favs_null_island(token):
    line = 12
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_01_data(token):
    line = 13
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_01_neg_data(token):
    line = 14
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_99_data(token):
    line = 15
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_90_data(token):
    line = 16
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_180_data(token):
    line = 17
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_901_data(token):
    line = 18
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lat_value()
    create.check_status_is_400()


@allure.feature('Coordinate fields')
def test_creating_favs_1801_data(token):
    line = 19
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lon_value()
    create.check_status_is_400()


@allure.feature('Coordinate fields')
def test_creating_favs_neg89_data(token):
    line = 20
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_neg90_data(token):
    line = 21
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_3(line))
    create.check_lat(payloads.payload_3(line))
    create.check_lon(payloads.payload_3(line))
    create.check_status_is_200()


@allure.feature('Coordinate fields')
def test_creating_favs_neg901_data(token):
    line = 22
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lat_value_neg()
    create.check_status_is_400()


@allure.feature('Coordinate fields')
def test_creating_favs_neg1801_data(token):
    line = 23
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lon_value_neg()
    create.check_status_is_400()


@allure.feature('Coordinate fields')
def test_creating_favs_neg_overdata(token):
    line = 24
    create.new_favs_3(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_lon_value_neg()
    create.check_status_is_400()


@allure.feature('Color field')
def test_creating_favs_cap_red(token):
    line = 25
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_status_is_200()


@allure.feature('Color field')
def test_creating_favs_cap_blue(token):
    line = 26
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_status_is_200()


@allure.feature('Color field')
def test_creating_favs_cap_green(token):
    line = 27
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_status_is_200()


@allure.feature('Color field')
def test_creating_favs_cap_yellow(token):
    line = 28
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_status_is_200()


@allure.feature('Color field')
def test_creating_favs_low_red(token):
    line = 29
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_status_is_200()


@allure.feature('Color field')
def test_creating_favs_cap_black(token):
    line = 30
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.show_status_code()
    create.check_color_value()
    create.check_status_is_400()


@allure.feature('Color field')
def test_creating_favs_color_null(token):
    line = 31
    create.new_favs_all(post_link, line, token)
    create.show_description(line)
    create.check_title(payloads.payload_all(line))
    create.check_lat(payloads.payload_all(line))
    create.check_lon(payloads.payload_all(line))
    create.check_color(payloads.payload_all(line))
    create.check_status_is_200()
