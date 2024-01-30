import json
import requests

from base64 import b64encode

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

payload = {
    "countryCode": "KE",
    "accountId": "0570182740362",
    "date": "2024-01-30"
}

# message = f"{payload['accountId']}{payload['countryCode']}{payload['date']}".encode('utf-8')
message = f"{payload['countryCode']}{payload['accountId']}".encode('utf-8')

digest = SHA256.new()
digest.update(message)

privateKey = False

with open("privatekey.pem") as pfile:
    privateKey = RSA.importKey(pfile.read())

signer = PKCS1_v1_5.new(privateKey)
sigBytes = signer.sign(digest)
signBase64 = b64encode(sigBytes)

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJSUzUxMiJ9.eyJ0b2tlblR5cGUiOiJNRVJDSEFOVCIsImVudiI6IlVBVCIsImV4cCI6MTcwNjU5OTk3NiwiaWF0IjoxNzA2NTk5MDc2LCJhY2NvdW50IjoiN0NDNUNENzFCMTdDQ0NEOUNFNzcyQzZFNEE5Mzk5MzVGQUQwNUQ5MUVGNzI3MzkyM0ZDODNFOTc1ODk0NkY5NDI4MzU5Q0E5QjVFREUyNDkzRkUzMkQ1Q0UzQzI4NkI0UWxDbGkwNURCc0pKelRtZjdRSHNZK05ZOGdYSHBabXBFVjZ4bE5HeDNnbmZIMHBuSTc4QnYyWDhhcHBzcmNYcDE3M2svcE9RcXhUWE5qMHdQSVVJZFlUY0NpU2J3OWtVZUZRV0o5UXdRaW44K2FyQ0NpSzAyNVpvM3RpUUt3dmNtbmNSZzFZUHNQcUloVm1PcGJSU0xXN1QwdEdZdFZua0dUNHloTVhhVXI1d2dBMFlMT1E4RkJLdzFZYW1RMVVzOTFqMlg0NExHYmlia0I5Ukc4bHhpbWtmQlVBa3J6bUpibEgwTzRzbE91Y1NQMUhmUHF2RlpEVFhDNWJWOHdXajNNMmMxSXN3SmNuUUgxQ1lCaExGT3V1cTNhcmM3eEg3MnoxZDdTb0NzWXVyZDJjZ2RMNlY1aG1GVE53WFpVZ1VZdXFVSFcrRjFHRUxoRTN0RUh3d3htNFd1Wkc2WDN0aGFrUnhyTGlDNjNSU2RXRnJrUUVrY1VYcEdYT0g4OUNYRld4RGJLQlhqbjVVN3FYOWkxU2d3emFqdE8yYm15d2FiS2JEeC92bkpMalBnWVEwUjRzdmFBdERRY090RG9IUyJ9.JEWYZKm4hUWf9pxWMaGeZ-_r-46GUwBCaPqHLMF1Su93s4bo3wDVUBV2jEV0ggz3ai5xP-WRWqA-UMZla4G5nCpeR50yjdQ9pMPej_EW7Gi73DC9sXK8u015XuZzRECcpv-rfEbJ3bstT4EZsk93O4JLSw7CA9x60GvjvGSQD34A-A5xqHoxSBpf4BwOuyVIVdfIg81zvHhpXD527bQDj5hO7kzcRj4-diSUWOLiFKHpfKxkQlz0BjFSzp-6qKplTBGOMUBMHGH6godY7OIVsmEmm79KZZw5y_l95dS4g5I9Q-5viZTREr3jpZjyJ_Un3QJNtlDo1xWLBijjZBff7g',
    'signature': signBase64
}

params = {}

url = "https://uat.finserve.africa/v3-apis/account-api/v3.0/accounts/balances/KE/0570182740362"
#url = 'https://uat.finserve.africa/v3-apis/account-api/v3.0/accounts/accountBalance/query'
response = requests.get(url, headers=headers, data=json.dumps(payload))
print(response.text)