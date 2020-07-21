# url_shortener
Django REST API for URL-shortener


METHODS EXAMPLES:

[GET]   https://url-shortener-tust.herokuapp.com                  -- returns list of all URLs with their `short_url`

[POST]  https://url-shortener-tust.herokuapp.com/shortener/{URL}  -- generate `hash` and create new `short_url` of `URL`

[GET]   https://url-shortener-tust.herokuapp.com/{hash}           -- redirect to original `URL`

[GET]   https://url-shortener-tust.herokuapp.com/export/          -- export `.csv` file with all pairs (`URL`, `short_url`)


=============================================================================================================================
=============================================================================================================================
==========


Example:
URL = https://github.com/DoubleTroubleOf/url_shortener

POST :: https://url-shortener-tust.herokuapp.com/shortener/https://github.com/DoubleTroubleOf/url_shortener

hash = iyAatM

short_url = https://url-shortener-tust.herokuapp.com/iyAatM
