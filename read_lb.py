################################################
# Simple script to get response from given url #
# and count by the response body content.      #
################################################
import pprint

import requests

TARGET_URL = "http://192.168.99.100/"
REPORT = {}

_CNT_INIT = 50
_ERROR_ID = "Error"

REPORT[_ERROR_ID] = 0  # initialize Errors (when response status code is not 200)
print_cnt = _CNT_INIT

while True:
    response = requests.get(TARGET_URL)

    if response.status_code != 200:
        REPORT[_ERROR_ID] += 1
    else:
        REPORT[response.text] = REPORT.get(response.text, 0) + 1

    response.close()  # Explicit calling due intermittent resource exhaustion

    print_cnt -= 1
    if not print_cnt:
        pprint.pprint(REPORT)
        print_cnt = _CNT_INIT
