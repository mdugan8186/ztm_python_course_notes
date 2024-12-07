# ==== password API ====

# requests is like having a browser without having a browser, we can manually request something like we have a browser and get some data back
import requests


# you should always hash a password and NEVER store a password in plain text. we will use SHA1 with this password
url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)  # <Response [200]>


# to prevent someone from guessing your password with the hashed password this API uses a technique called k-anonymity. this is a modern technique that big companies use that allows someone to receive information about us yet still not know who we are. the way this works is that we only give the first 5 characters of our hash password. in this case CBFDA of the hashed password. what this is going to do is is the API has a list of all the passwords that have been leaked. however all these passwords are hashed with the SHA1 algorithm  so its going to look in its data base of all  these passwords and pick all of the hashed passwords that have the first 5 characters that match what we entered. this way with the response we're going to get all the passwords that sre hashed that have the characters that we entered. on our end when we receive that response we can check the rest of the the hash function. this way the API is never going to know our full hash


# hashed password for password123  CBFDAC6008F9CAB4083784CBD1874F76618D2A97
