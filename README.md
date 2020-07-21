# url_shortener
Django REST API for URL-shortener


METHODS EXAMPLES:

[GET]   https://url-shortener-tust.herokuapp.com                  -- returns list of all URLs with their `short_url`

[POST]  https://url-shortener-tust.herokuapp.com/shortener/{URL}  -- create new `short_url` of `URL`

[GET]   https://url-shortener-tust.herokuapp.com/{short_url}      -- redirect to original `URL`

[GET]   https://url-shortener-tust.herokuapp.com/export/          -- export `.csv` file with all pairs (`URL`, `short_url`)
