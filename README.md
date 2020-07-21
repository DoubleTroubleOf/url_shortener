# url_shortener
Django REST API for URL-shortener


METHODS EXAMPLES:

[GET]   http://127.0.0.1:8000                  -- returns list of all URLs with their `short_url`

[POST]  http://127.0.0.1:8000/shortener/{URL}  -- create new `short_url` of `URL`

[GET]   http://127.0.0.1:8000/{short_url}      -- redirect to original `URL`

[GET]   http://127.0.0.1:8000/export/          -- export `.csv` file with all pairs (`URL`, `short_url`)
