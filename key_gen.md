# Jenga Signatures

## Generate Private Key

```sh
$ openssl genrsa -out privatekey.pem 2048
```

```sh
$ openssl rsa -in privatekey.pem -outform PEM -pubout -out publickey.pem
```
