# ==== password checker 3 ====

# the file path for this is:
# michaeldugan@Michaels-MacBook-Pro ztm_python_course_notes % cd course_notes/13.\ scripting_with_python/18.\ password_checker_3

import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {
                res.status_code}, check the API and try again'
        )
    return res


def get_passwords_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    # print(first5_char, tail)
    # print(response)
    return get_passwords_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {
                  count} times... you should probably change your password!')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'


main(sys.argv[1:])
