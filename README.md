# TP_Requests

<p align="center">
    <a href="https://github.com/truocphan/TP_Requests/releases/"><img src="https://img.shields.io/github/release/truocphan/TP_Requests" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/downloads/truocphan/TP_Requests/total" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/stars/truocphan/TP_Requests" height=30></a>
	<a href="#"><img src="https://img.shields.io/github/forks/truocphan/TP_Requests" height=30></a>
	<a href="https://github.com/truocphan/TP_Requests/issues?q=is%3Aopen+is%3Aissue"><img src="https://img.shields.io/github/issues/truocphan/TP_Requests" height=30></a>
	<a href="https://github.com/truocphan/TP_Requests/issues?q=is%3Aissue+is%3Aclosed"><img src="https://img.shields.io/github/issues-closed/truocphan/TP_Requests" height=30></a>
	<a href="https://pypi.org/project/TP_Requests/" target="_blank"><img src="https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white" height=30></a>
	<a href="https://www.facebook.com/292706121240740" target="_blank"><img src="https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white" height=30></a>
	<a href="https://twitter.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" height=30></a>
	<a href="https://github.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" height=30></a>
	<a href="mailto:truocphan112017@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" height=30></a>
	<a href="https://www.buymeacoffee.com/truocphan" target="_blank"><img src="https://img.shields.io/badge/Buy_Me_A_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" height=30></a>
</p>

TP_HTTP_REQUEST:
- PathParams (dict, OrderedDict)
- QueryParams (dict, OrderedDict)
- URIFragment (Any -> str)
- HTTPVersion (Any -> str)
- HTTPHeaders (dict, OrderedDict)
- BodyJson (None, dict, OrderedDict, list)
- BodyData (dict, OrderedDict)
- BodyFiles (list)
- BodyContent (str)


get_path_params() -> (dict, OrderedDict)
get_path_param(name) -> (str, None)


get_query_params() -> (dict, OrderedDict)
get_query_param(name) -> (str, None)


get_uri_fragment() -> str


get_http_version() -> str


get_http_headers() -> (dict, OrderedDict)
get_http_header(name) -> (str, None)


get_http_cookies() -> (dict, OrderedDict)
get_http_cookie(name) -> (str, None)


get_body_json_params() -> (dict, OrderedDict)
get_body_json_param(name) -> (str, None)???


get_body_data_params() -> (dict, OrderedDict)
get_body_data_param(name) -> (str, None)


get_body_files_params() -> (list)
get_body_data_param(index) -> (dict, OrderedDict, None)???


get_body_content() -> str


get_http_requests_responses() -> list(request, response)


delete_path_params()
delete_path_param(PathParamsList)


delete_query_params()
delete_query_param(QueryParamsList)


delete_uri_fragment()


delete_http_version()


delete_http_headers()
delete_http_header(HTTPHeadersList)


delete_http_cookies()
delete_http_cookie(HTTPCookiesList)


request(self, method, url, update_content_length=True, injectObj=dict(), proxy_server=None)