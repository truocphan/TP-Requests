# TP-Requests

<p align="center">
	<a href="https://github.com/truocphan/TP-Requests/releases/"><img src="https://img.shields.io/github/release/truocphan/TP-Requests" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/downloads/truocphan/TP-Requests/total" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/stars/truocphan/TP-Requests" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/forks/truocphan/TP-Requests" height=30></a>
	<a href="https://github.com/truocphan/TP-Requests/issues?q=is%3Aopen+is%3Aissue"><img src="https://img.shields.io/github/issues/truocphan/TP-Requests" height=30></a>
	<a href="https://github.com/truocphan/TP-Requests/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/truocphan/TP-Requests" height=30></a>
	<br>
	<a href="#"><img src="https://img.shields.io/pypi/v/TP-Requests" height=30></a>
	<a href="#"><img src="https://img.shields.io/pypi/dm/TP-Requests" height=30></a>
</p>

## Installation
#### From PyPI:
```console
pip install TP-Requests
```
#### From Source:
```console
git clone https://github.com/truocphan/TP-Requests.git --branch <Branch/Tag>
cd TP-Requests
python setup.py build
python setup.py install
```

## Basic Usage
```
from TP_Requests.http import TP_HTTP_REQUEST

rawRequest = """GET /v1/promo/extension HTTP/2
Host: d2y7f743exec8w.cloudfront.net
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en-US;q=0.9,en;q=0.8
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.97 Safari/537.36
Connection: close
Cache-Control: max-age=0

"""

httpRequest = TP_HTTP_REQUEST(rawRequest)

httpRequest.RequestParser.request_method = "POST"

print(httpRequest.sendRequest(Host="d2y7f743exec8w.cloudfront.net", Port=443, Scheme="https", proxy_server={"host":"127.0.0.1","port":8080}).dumps(indent=4))
```