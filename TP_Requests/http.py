import re, json_duplicate_keys as jdks, socket, ssl, copy, uuid
from collections import OrderedDict
from urllib.parse import urlparse

class TP_HTTP_REQUEST:
	def __init__(self, PathParams=dict(), QueryParams=dict(), URIFragment=str(), HTTPVersion="HTTP/1.1", HTTPHeaders=dict(), BodyJson=None, BodyData=dict(), BodyFiles=list(), BodyContent=str()):
		# TP_HTTP_REQUEST version
		self.__version = "23.7.31"
		self.__BodyType = None

		# initialization PathParams
		self.__PathParams = dict()
		if type(PathParams) in [dict, OrderedDict]:
			self.__PathParams = PathParams

		# initialization QueryParams
		self.__QueryParams = dict()
		if type(QueryParams) in [dict, OrderedDict]:
			self.__QueryParams = QueryParams

		# initialization URIFragment
		self.__URIFragment = str()
		if type(URIFragment) in [str]:
			self.__URIFragment = URIFragment

		# initialization HTTPVersion
		self.__HTTPVersion = "HTTP/1.1"
		if type(HTTPVersion) in [str]:
			self.__HTTPVersion = HTTPVersion

		# initialization HTTPHeaders
		self.__HTTPHeaders = dict()
		if type(HTTPHeaders) in [dict, OrderedDict]:
			self.__HTTPHeaders = HTTPHeaders

		if "User-Agent" not in self.__HTTPHeaders.keys(): self.__HTTPHeaders["User-Agent"] = "TP_Requests (http/TP_HTTP_REQUEST "+self.__version+")"
		if "Connection" not in self.__HTTPHeaders.keys(): self.__HTTPHeaders["Connection"] = "close"

		# initialization HTTPCookies
		self.__HTTPCookies = dict()
		if "Cookie" in self.__HTTPHeaders.keys():
			for cookie in str(self.__HTTPHeaders["Cookie"]).split(";"):
				if len(cookie.split("=", 1)) == 2:
					self.__HTTPCookies[cookie.split("=", 1)[0].strip()] = cookie.split("=", 1)[1].strip()
				else:
					self.__HTTPCookies[cookie.split("=", 1)[0].strip()] = ""

		# initialization BodyJson
		self.__BodyJson = None
		if type(BodyJson) in [dict, OrderedDict, list]:
			self.__BodyJson = BodyJson

		# initialization BodyData
		self.__BodyData = dict()
		if type(BodyData) in [dict, OrderedDict]:
			self.__BodyData = BodyData

		# initialization BodyFiles
		self.__BodyFiles = list()
		if type(BodyFiles) in [list]:
			self.__BodyFiles = BodyFiles

		# initialization BodyContent
		self.__BodyContent = str()
		if type(BodyContent) in [str]:
			self.__BodyContent = BodyContent

		# Requests/ Responses
		self.__HTTPRequestsResponses = list()



	# READ PathParams
	def get_path_params(self):
		return self.__PathParams

	def get_path_param(self, name):
		if name not in self.__PathParams.keys():
			return None
		return self.__PathParams[name]


	# READ QueryParams
	def get_query_params(self):
		return self.__QueryParams

	def get_query_param(self, name):
		if name not in self.__QueryParams.keys():
			return None
		return self.__QueryParams[name]


	# READ URIFragment
	def get_uri_fragment(self):
		return self.__URIFragment


	# READ HTTPVersion
	def get_http_version(self):
		return self.__HTTPVersion


	# READ HTTPHeaders
	def get_http_headers(self):
		return self.__HTTPHeaders

	def get_http_header(self, name):
		if name not in self.__HTTPHeaders.keys():
			return None
		return self.__HTTPHeaders[name]


	# READ HTTPCookies
	def get_http_cookies(self):
		return self.__HTTPCookies

	def get_http_cookie(self, name):
		if name not in self.__HTTPCookies.keys():
			return None
		return self.__HTTPCookies[name]


	# READ BodyJson
	def get_body_json_params(self):
		return self.__BodyJson

	def get_body_json_param(self, name):
		if name not in self.__BodyJson.keys():
			return None
		return self.__BodyJson[name]


	# READ BodyData
	def get_body_data_params(self):
		return self.__BodyData

	def get_body_data_param(self, name):
		if name not in self.__BodyData.keys():
			return None
		return self.__BodyData[name]


	# READ BodyFiles
	def get_body_files_params(self):
		return self.__BodyFiles

	def get_body_files_param(self, index):
		if int(index) >= len(self.__BodyFiles):
			return None
		return self.__BodyFiles[int(index)]


	# READ BodyContent
	def get_body_content(self):
		return self.__BodyContent


	# READ HTTP Requests/ Responses List
	def get_http_requests_responses(self):
		return self.__HTTPRequestsResponses



	# CREATE/ UPDATE PathParams
	def set_path_param(self, name, value):
		self.__PathParams[name] = str(value)

	def set_path_params(self, PathParamsObj):
		if type(PathParamsObj) in [dict, OrderedDict]:
			PathParamsObj = jdks.flatten(PathParamsObj)
			for name in PathParamsObj:
				self.set_path_param(name, PathParamsObj[name])


	# CREATE/ UPDATE QueryParams
	def set_query_param(self, name, value):
		self.__QueryParams[name] = str(value)

	def set_query_params(self, QueryParamsObj):
		if type(QueryParamsObj) in [dict, OrderedDict]:
			QueryParamsObj = jdks.flatten(QueryParamsObj)
			for name in QueryParamsObj:
				self.set_query_param(name, QueryParamsObj[name])


	# CREATE/ UPDATE URIFragment
	def set_uri_fragment(self, value):
		if type(value) in [str]:
			self.__URIFragment = str(value)


	# CREATE/ UPDATE HTTPVersion
	def set_http_version(self, value):
		if type(value) in [str]:
			self.__HTTPVersion = str(value)


	# CREATE/ UPDATE HTTPHeaders
	def set_http_header(self, name, value):
		self.__HTTPHeaders[name] = str(value)

	def set_http_headers(self, HTTPHeadersObj):
		if type(HTTPHeadersObj) in [dict, OrderedDict]:
			HTTPHeadersObj = jdks.flatten(HTTPHeadersObj)
			for name in HTTPHeadersObj:
				self.set_http_header(name, HTTPHeadersObj[name])


	# CREATE/ UPDATE HTTPCookies
	def set_http_cookie(self, name, value):
		self.__HTTPCookies[name] = str(value)

	def set_http_cookies(self, HTTPCookiesObj):
		if type(HTTPCookiesObj) in [dict, OrderedDict]:
			HTTPCookiesObj = jdks.flatten(HTTPCookiesObj)
			for name in HTTPCookiesObj:
				self.set_http_cookie(name, HTTPCookiesObj[name])


	# CREATE/ UPDATE BodyJson
	def set_body_json_param(self, name, value):
		self.__BodyJson[name] = value

	def set_body_json_params(self, BodyJsonObj):
		if type(BodyJsonObj) in [dict, OrderedDict, list]:
			BodyJsonObj = jdks.flatten(BodyJsonObj)
			for name in BodyJsonObj:
				self.set_body_json_param(name, BodyJsonObj[name])


	# CREATE/ UPDATE BodyData
	def set_body_data_param(self, name, value):
		self.__BodyData[name] = str(value)

	def set_body_data_params(self, BodyDataObj):
		if type(BodyDataObj) in [dict, OrderedDict]:
			BodyDataObj = jdks.flatten(BodyDataObj)
			for name in BodyDataObj:
				self.set_body_data_param(name, BodyDataObj[name])


	# CREATE/ UPDATE BodyFiles
	def set_body_files_param(self, name, value):
		self.__BodyFiles[name] = str(value)

	def set_body_files_params(self, BodyFilesObj):
		if type(BodyFilesObj) in [dict, OrderedDict]:
			BodyFilesObj = jdks.flatten(BodyFilesObj)
			for name in BodyFilesObj:
				self.set_body_files_param(name, BodyFilesObj[name])


	# CREATE/ UPDATE BodyContent
	def set_body_content(self, value):
		if type(value) in [str]:
			self.__BodyContent = str(value)



	# DELETE PathParams
	def delete_path_params(self):
		self.__PathParams = dict()

	def delete_path_param(self, PathParamsList):
		for name in PathParamsList:
			if name in self.__PathParams.keys():
				del self.__PathParams[name]


	# DELETE QueryParams
	def delete_query_params(self):
		self.__QueryParams = dict()

	def delete_query_param(self, QueryParamsList):
		for name in QueryParamsList:
			if name in self.__QueryParams.keys():
				del self.__QueryParams[name]


	# DELETE URIFragment
	def delete_uri_fragment(self):
		self.__URIFragment = str()


	# DELETE HTTPVersion
	def delete_http_version(self):
		self.__HTTPVersion = str()


	# DELETE HTTPHeaders
	def delete_http_headers(self):
		self.__HTTPHeaders = dict()

	def delete_http_header(self, HTTPHeadersList):
		for name in HTTPHeadersList:
			if name in self.__HTTPHeaders.keys():
				del self.__HTTPHeaders[name]


	# DELETE HTTPCookies
	def delete_http_cookies(self):
		self.__HTTPCookies = dict()

	def delete_http_cookie(self, HTTPCookiesList):
		for name in HTTPCookiesList:
			if name in self.__HTTPCookies.keys():
				del self.__HTTPCookies[name]


	# DELETE BodyJson
	def delete_body_json_params(self):
		self.__BodyJson = None

	def delete_body_json_param(self, BodyJsonList):
		for name in BodyJsonList:
			if name in self.__BodyJson.keys():
				del self.__BodyJson[name]


	# DELETE BodyData
	def delete_body_data_params(self):
		self.__BodyData = dict()

	def delete_body_data_param(self, BodyDataList):
		for name in BodyDataList:
			if name in self.__BodyData.keys():
				del self.__BodyData[name]


	# DELETE BodyFiles
	def delete_body_files_params(self):
		self.__BodyFiles = list()

	def delete_body_files_param(self, BodyFilesList):
		for name in BodyFilesList:
			if name in self.__BodyFiles.keys():
				del self.__BodyFiles[name]


	# DELETE BodyContent
	def delete_body_content(self):
		self.__BodyContent = str()



	# send HTTP request to server
	def request(self, method, url, update_content_length=True, injectObj=dict(), proxy_server=None):
		# Clone self Object
		httpReq = copy.deepcopy(self)

		# Parse request url
		scheme = urlparse(url).scheme
		netloc = urlparse(url).netloc
		path = urlparse(url).path

		# Handle server url
		server_hostname = netloc.split(":",1)[0]
		if len(netloc.split(":",1)) == 2:
			server_port = int(netloc.split(":",1)[1])
		else:
			if scheme == "https":
				server_port = 443
			elif self == "http":
				server_port = 80
			else:
				exit("Invalid URL")

		# Create a socket connection
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Connect to the proxy/ server
		if proxy_server != None:
			client_socket.connect((str(proxy_server["host"]), int(proxy_server["port"])))
		else:
			client_socket.connect((server_hostname, server_port))

		# Perform SSL/TLS handshake with the target server
		if scheme == "https":
			context = ssl.create_default_context()
			context.check_hostname = False
			context.verify_mode = ssl.CERT_NONE
			client_socket = context.wrap_socket(client_socket, server_side=False, server_hostname=server_hostname)

		# Prepare the HTTP request
		# rr_method
		rr_method = str(method)

		# rr_path
		path_split = path.split("/")
		for i in range(len(path_split)):
			if path_split[i] in httpReq.get_path_params().keys():
				path_split[i] = str(httpReq.get_path_params()[path_split[i]])
		rr_path = "/".join(path_split)
		if len(rr_path) == 0: rr_path += "/"

		# rr_query
		rr_query = "?" + "&".join([str(name)+"="+str(httpReq.get_query_params()[name]) for name in httpReq.get_query_params()]) if len(httpReq.get_query_params())>0 else ""

		# rr_fragment
		rr_fragment = "#" + httpReq.get_uri_fragment() if len(httpReq.get_uri_fragment())>0 else ""

		# rr_httpversion
		rr_httpversion = httpReq.get_http_version()

		# rr_body
		if type(httpReq.get_body_json_params()) in [dict, OrderedDict, list]:
			rr_body = jdks.dumps(httpReq.get_body_json_params())
			httpReq.__BodyType = "BodyJson"
		elif len(httpReq.get_body_data_params()) > 0:
			rr_body = "&".join([str(name)+"="+str(httpReq.get_body_data_params()[name]) for name in httpReq.get_body_data_params()]) if len(httpReq.get_body_data_params())>0 else ""
			httpReq.__BodyType = "BodyData"
		elif len(httpReq.get_body_files_params()) > 0:
			boundaryID = "-"*26+uuid.uuid4().hex[-24:]
			rr_body = ""
			for ParamObj in httpReq.get_body_files_params():
				if "name" in ParamObj.keys():
					httpReq.__BodyType = "BodyFiles"
					rr_body += "--"+boundaryID+"\r\n"
					rr_body += "Content-Disposition: form-data; name=\""+str(ParamObj["name"])+"\""
					if "filename" in ParamObj.keys():
						rr_body += "; filename=\""+str(ParamObj["filename"])+"\""
					rr_body += "\r\n"
					if "headers" in ParamObj.keys():
						for headerName in ParamObj["headers"]:
							rr_body += str(headerName)+": "+ParamObj["headers"][headerName] + "\r\n"
					rr_body += "\r\n"
					if "value" in ParamObj.keys():
						rr_body += str(ParamObj["value"])
					rr_body += "\r\n"

			if httpReq.__BodyType == "BodyFiles":
				rr_body += "--"+boundaryID+"--\r\n"
		elif len(httpReq.get_body_content()) > 0:
			rr_body = httpReq.get_body_content()
			httpReq.__BodyType = "BodyContent"
		else:
			rr_body = ""
			httpReq.__BodyType = None

		# rr_headers
		rr_headers = ""
		if update_content_length:
			if len(rr_body) > 0:
				httpReq.__HTTPHeaders["Content-Length"] = len(rr_body)
			elif rr_method in ["POST", "PUT"]:
				httpReq.__HTTPHeaders["Content-Length"] = 0

		if len(rr_body) > 0 and "Content-Type" not in httpReq.__HTTPHeaders.keys():
			if httpReq.__BodyType == "BodyJson":
				httpReq.__HTTPHeaders["Content-Type"] = "application/json"
			elif httpReq.__BodyType == "BodyData":
				httpReq.__HTTPHeaders["Content-Type"] = "application/x-www-form-urlencoded"
			elif httpReq.__BodyType == "BodyFiles":
				httpReq.__HTTPHeaders["Content-Type"] = "multipart/form-data; boundary="+boundaryID
			else:
				httpReq.__HTTPHeaders["Content-Type"] = "application/octet-stream"

		rr_headers = "\r\n".join([str(name)+": "+str(httpReq.get_http_headers()[name]) for name in httpReq.get_http_headers()]) if len(httpReq.get_http_headers())>0 else ""


		rawRequest = f"{rr_method} {rr_path}{rr_query}{rr_fragment} {rr_httpversion}\r\n{rr_headers}\r\n\r\n{rr_body}"

		# Send the HTTP request
		client_socket.sendall(rawRequest.encode())

		# Receive and process the server's response
		rawResponse = b""
		while True:
			chunk = client_socket.recv(4096)
			if not chunk:
				break
			rawResponse += chunk

		# Close the connections
		client_socket.close()

		# Request/ Response
		self.__HTTPRequestsResponses.append({
			"request": rawRequest,
			"response": rawResponse.decode()
		})