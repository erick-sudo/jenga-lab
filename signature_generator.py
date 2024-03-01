import json
import requests

from base64 import b64encode

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

payload = {
    "countryCode": "KE",
    "accountId": "0570182740362",
    "date": "2024-01-31"
}

# message = f"{payload['accountId']}{payload['countryCode']}{payload['date']}".encode('utf-8')
message = f"{payload['countryCode']}{payload['accountId']}".encode('utf-8')

digest = SHA256.new()
digest.update(message)

privateKey = False

with open("jenga-private-key.pem") as pfile:
    privateKey = RSA.importKey(pfile.read())

signer = PKCS1_v1_5.new(privateKey)
sigBytes = signer.sign(digest)
signBase64 = b64encode(sigBytes)

print(signBase64)

# headers = {
#     'Content-Type': 'application/json',
#     'Authorization': 'Bearer eyJhbGciOiJSUzUxMiJ9.eyJ0b2tlblR5cGUiOiJNRVJDSEFOVCIsImVudiI6IlVBVCIsImV4cCI6MTcwNjY2MTI2MSwiaWF0IjoxNzA2NjYwMzYxLCJhY2NvdW50IjoiQ0I5QjIzM0JFOTMzMEVGMzY2MTRGMzMwQkE3NTg4RjFDNEE1OURDMDM0QjVFNkZFOERCOTdERTI5NkU0MzYyM0JERkQ4MDI1QjQzNUNFQTNERjEzRUU1QUFEODZBNkE1anZ4RTlFUm9pSXIrQlh2WEd1Q2lZKzZKaU5Eci9XVFM3ek5acURDb2VaOHNXbUFGcHlQWEJjNDFveDI0ZW5vdGpuNnRZSTB6ZGdKekpoYy9JTkNxOE02amx6RGhDMW5VYUdhRGxNM1JaWGFUcUZsRElZOXpHTExGRVlyZzNPaGgwOXdIWE55b0xQVzRPS1FwL25vR0lib2dZQU5DaHdBbkxiTG9oTWpSaVBOVm5LL0ZkbUlpaGw1VjhnZDJmazBMcENLK0swTzZEUzIwdXd5VDBrTVVrWm5EY3czNlA2dExoT1JwWnpWL21STlJ2RGNuTGExZlRJaEZFQzR2UE9UT1pBckhiN0I4WkYvL2JOaGpOTE9ySjdQVVcrVU9UTThhYldUb052Q2tlVHZBM3lJZVByNE9uUTRmTzlFWVhPSVM2bWwxOXBYK1RybUtuL0NGdStmTDFFZGJjcGxQTm1Ld1FKMnJ1S2pNaVlOOTMrNWR6UmFNOVgyc2JyNXdWaU9OK0J0OUpXeXBzY2VtQnpKN0diaytxcndJV0J4RDNETVRhNmFmdzJaUzN1dnhQTEtHNVpWYVZDU1c5c3hUaGZXciJ9.MnhI0SUHG4l3kg2JuCUcwV5fWG5tDoYyzzpIiBsMlEyAGldXg1sLxtbNnS6hM9NXTmZd3y_d3P28LqzvI0J7HatGiiP4wk45nxCHOJU9RQwsO6ScPK1FEZEzJoAlnjwWuzxB8ryEBFGyjcUuRBwmENaDkkiS84qC3uDRrQQr4appBmYodI6jeDJkvhv1-il2hAT8yWufnGELjVgEqzVlilzKrSEcbu7NBXyO6bLHeRxuQA_7s6_k99ffVtpLGljzTTnxYTTINYPhifJ7JAdMTkK3gKRYlVIJs3DIlmHFBpeszPHUqbY7fFCxcQ2DYMV0W_wh8jtK5Ml2Lrji9KhcCg',
#     'signature': signBase64
# }

# params = {}

# url = "https://uat.finserve.africa/v3-apis/account-api/v3.0/accounts/balances/KE/0570182740362"
# #url = 'https://uat.finserve.africa/v3-apis/account-api/v3.0/accounts/accountBalance/query'
# response = requests.get(url, headers=headers) #, data=json.dumps(payload))
# print(response.text)