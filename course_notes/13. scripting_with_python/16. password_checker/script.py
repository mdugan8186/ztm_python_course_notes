# ==== password checker ====

import requests
import hashlib

# password123


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {
                           res.status_code}, check the API and try again')
    return res


def pwned_api_check(password):
    # check password if it exists in API response
    # print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1password


# check that the request_api_data code is working
# request_api_data('123')

# check that pwned_api_check works
# pwned_api_check('123')
