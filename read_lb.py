################################################
# Simple script to get response from given url #
# and count by the response body content.      #
################################################
import pprint

import requests

TARGET_URL = "http://192.168.99.100/"
COUNTED_STATS = {}

_CNT_INIT = 50
_ERROR_ID = "Error"

COUNTED_STATS[_ERROR_ID] = 0  # initialize Errors (when response status code is not 200)
CNT = _CNT_INIT

while True:
    response = requests.get(TARGET_URL)

    if response.status_code != 200:
        COUNTED_STATS[_ERROR_ID] += 1
    else:
        COUNTED_STATS[response.text] = COUNTED_STATS.get(response.text, 0) + 1

    CNT -= 1
    if not CNT:
        CNT = _CNT_INIT
        pprint.pprint(COUNTED_STATS)
