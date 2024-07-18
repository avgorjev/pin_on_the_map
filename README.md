# Place pin on the map

POST-request to create user favorites on the map (REST API)

Example request:
```
curl -X POST -s https://*** \
-d "title=title&lat=34.854359&lon=77.490324" \
-b "token=***"
```

Response example:
```
{
"id": 1584938475643,
"title": "title",
"lat": 34.854359,

"lon": 77.490324,
"color": null,
"created_at": "2024-06-18T02:13:55+00:00"
}
```

### The Allure report for test cases is available on this [page](https://avgorjev.github.io/pin_on_the_map/)

![Creating pins on the map](https://github.com/avgorjev/pin_on_the_map/actions/workflows/test.yml/badge.svg)
