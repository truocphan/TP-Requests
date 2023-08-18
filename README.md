# TP_Requests

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