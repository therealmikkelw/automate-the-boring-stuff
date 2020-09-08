import requests

# This program crashes since it cannot access the system certificate file while establishing SSL context
#       - this probably has to do with some access limitation set up by IT dep.
# UPDATE: solved by locating Python's certificate file using certifi.where()
#         and appending entire chain of trust from target URL
#         see accepted answer to this question: https://stackoverflow.com/questions/51925384/unable-to-get-local-issuer-certificate-when-using-requests-in-python
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(res.status_code) # 200 = all ok, 404 = file not found
res.raise_for_status()
print(res.text[:500])

playFile = open('RomeoAndJuliet.txt', 'wb') # write binary to maintain unicode encoding of text
for chunk in res.iter_content(100000):  # 100,000 bytes per chunk of data
    playFile.write(chunk)

playFile.close()

# Reference: https://requests.readthedocs.org
