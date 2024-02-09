import json_duplicate_keys as jdks, socket, ssl, copy, time
from collections import OrderedDict
from urllib.parse import urlparse
from TP_HTTP_Request_Response_Parser import *

class TP_HTTP_REQUEST:
	def __init__(self, rawRequest, separator="||", parse_index="$", dupSign_start="{{{", dupSign_end="}}}", ordered_dict=False):
		self.__separator = separator
		self.__parse_index = parse_index
		self.__dupSign_start = dupSign_start
		self.__dupSign_end = dupSign_end
		self.__ordered_dict = ordered_dict

		# TP_HTTP_REQUEST version
		self.__version = "2024.2.9"

		RequestParser = TP_HTTP_REQUEST_PARSER(rawRequest, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, ordered_dict=self.__ordered_dict)

		self.__RequestMethod = RequestParser.request_method
		self.__RequestPath = RequestParser.request_path
		self.__PathParams = RequestParser.request_pathParams
		self.__QueryParams = RequestParser.request_queryParams
		self.__URIFragment = RequestParser.request_fragment
		self.__HTTPVersion = RequestParser.request_httpVersion
		self.__HTTPHeaders = RequestParser.request_headers
		self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)
		self.__RequestBody = RequestParser.request_body


		if self.__HTTPHeaders.get("User-Agent") == "JSON_DUPLICATE_KEYS_ERROR":
			self.__HTTPHeaders.set("User-Agent", "TP_Requests (http/TP_HTTP_REQUEST "+self.__version+")")
		if self.__HTTPHeaders.get("Connection") == "JSON_DUPLICATE_KEYS_ERROR":
			self.__HTTPHeaders.set("Connection", "close")


		if self.__HTTPHeaders.get("Cookie") != "JSON_DUPLICATE_KEYS_ERROR":
			for cookie in self.__HTTPHeaders.get("Cookie").split(";"):
				if len(cookie.split("=", 1)) == 2:
					self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip())
				else:
					self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "")


	# READ RequestMethod
	def get_request_method(self):
		return self.__RequestMethod

	# CREATE/ UPDATE RequestMethod
	def set_request_method(self, value):
		if type(value) == str:
			self.__RequestMethod = value


	# READ RequestPath
	def get_request_path(self):
		return self.__RequestPath


	# READ PathParams
	def get_path_params(self):
		return self.__PathParams

	def get_path_param(self, name):
		return self.get_path_params().get(name)

	# UPDATE PathParams
	def update_path_param(self, name, value):
		if type(value) == str:
			self.get_path_params().update(name, value)

	def update_path_params(self, PathParamsObj):
		if type(PathParamsObj) in [dict, OrderedDict]:
			for name in PathParamsObj:
				self.update_path_param(name, PathParamsObj[name])


	# READ QueryParams
	def get_query_params(self):
		return self.__QueryParams

	def get_query_param(self, name):
		return self.get_query_params().get(name)

	# CREATE QueryParams
	def set_query_param(self, name, value):
		if type(value) == str:
			self.get_query_params().set(name, value)

	def set_query_params(self, QueryParamsObj):
		if type(QueryParamsObj) in [dict, OrderedDict]:
			for name in QueryParamsObj:
				self.set_query_param(name, QueryParamsObj[name])

	# UPDATE QueryParams
	def update_query_param(self, name, value):
		if type(value) == str:
			self.get_query_params().update(name, value)

	def update_query_params(self, QueryParamsObj):
		if type(QueryParamsObj) in [dict, OrderedDict]:
			for name in QueryParamsObj:
				self.update_query_param(name, QueryParamsObj[name])

	# DELETE QueryParams
	def delete_query_params(self):
		self.__QueryParams = jdks.loads("{}", ordered_dict=self.__ordered_dict)

	def delete_query_param(self, QueryParamsList):
		for name in QueryParamsList:
			self.get_query_params().delete(name)


	# READ URIFragment
	def get_uri_fragment(self):
		return self.__URIFragment

	# CREATE/ UPDATE URIFragment
	def set_uri_fragment(self, value):
		if type(value) == str:
			self.__URIFragment = value

	# DELETE URIFragment
	def delete_uri_fragment(self):
		self.__URIFragment = str()


	# READ HTTPVersion
	def get_http_version(self):
		return self.__HTTPVersion

	# CREATE/ UPDATE HTTPVersion
	def set_http_version(self, value):
		if type(value) == str:
			self.__HTTPVersion = value


	# READ HTTPHeaders
	def get_http_headers(self):
		return self.__HTTPHeaders

	def get_http_header(self, name):
		return self.get_http_headers().get(name)

	# CREATE HTTPHeaders
	def set_http_header(self, name, value):
		if type(value) == str:
			self.get_http_headers().set(name, value)

			if name == "Cookie":
				self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)
				for cookie in self.__HTTPHeaders.get("Cookie").split(";"):
					if len(cookie.split("=", 1)) == 2:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip())
					else:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "")

	def set_http_headers(self, HTTPHeadersObj):
		if type(HTTPHeadersObj) in [dict, OrderedDict]:
			for name in HTTPHeadersObj:
				self.set_http_header(name, HTTPHeadersObj[name])

	# UPDATE HTTPHeaders
	def update_http_header(self, name, value):
		if type(value) == str:
			self.get_http_headers().update(name, value)
			if name == "Cookie" and self.get_http_headers().get(name) != "JSON_DUPLICATE_KEYS_ERROR":
				self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)
				for cookie in self.__HTTPHeaders.get("Cookie").split(";"):
					if len(cookie.split("=", 1)) == 2:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip())
					else:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "")

	def update_http_headers(self, HTTPHeadersObj):
		if type(HTTPHeadersObj) in [dict, OrderedDict]:
			for name in HTTPHeadersObj:
				self.update_http_header(name, HTTPHeadersObj[name])

	# DELETE HTTPHeaders
	def delete_http_headers(self):
		self.__HTTPHeaders = jdks.loads("{}", ordered_dict=self.__ordered_dict)
		self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)

	def delete_http_header(self, HTTPHeadersList):
		for name in HTTPHeadersList:
			self.get_http_headers().delete(name)

			if name == "Cookie":
				self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)


	# READ HTTPCookies
	def get_http_cookies(self):
		return self.__HTTPCookies

	def get_http_cookie(self, name):
		return self.get_http_cookies().get(name)

	# CREATE HTTPCookies
	def set_http_cookie(self, name, value):
		if type(value) == str:
			self.get_http_cookies().set(name, value)

			if self.get_http_headers().get("Cookie") == "JSON_DUPLICATE_KEYS_ERROR":
				self.get_http_headers().set("Cookie", "; ".join([jdks.normalize_key(cname)+"="+self.get_http_cookies().get(cname) for cname in self.get_http_cookies().getObject()]))
			else:
				self.get_http_headers().update("Cookie", "; ".join([jdks.normalize_key(cname)+"="+self.get_http_cookies().get(cname) for cname in self.get_http_cookies().getObject()]))

	def set_http_cookies(self, HTTPCookiesObj):
		if type(HTTPCookiesObj) in [dict, OrderedDict]:
			for name in HTTPCookiesObj:
				self.set_http_cookie(name, HTTPCookiesObj[name])

	# UPDATE HTTPCookies
	def update_http_cookie(self, name, value):
		if type(value) == str:
			self.get_http_cookies().update(name, value)

			if self.get_http_headers().get("Cookie") == "JSON_DUPLICATE_KEYS_ERROR":
				self.get_http_headers().set("Cookie", "; ".join([jdks.normalize_key(cname)+"="+self.get_http_cookies().get(cname) for cname in self.get_http_cookies().getObject()]))
			else:
				self.get_http_headers().update("Cookie", "; ".join([jdks.normalize_key(cname)+"="+self.get_http_cookies().get(cname) for cname in self.get_http_cookies().getObject()]))

	def update_http_cookies(self, HTTPCookiesObj):
		if type(HTTPCookiesObj) in [dict, OrderedDict]:
			for name in HTTPCookiesObj:
				self.update_http_cookie(name, HTTPCookiesObj[name])

	# DELETE HTTPCookies
	def delete_http_cookies(self):
		self.__HTTPCookies = jdks.loads("{}", ordered_dict=self.__ordered_dict)
		self.get_http_headers().delete("Cookie")

	def delete_http_cookie(self, HTTPCookiesList):
		for name in HTTPCookiesList:
			self.get_http_cookies().delete(name)

		if len(self.__HTTPCookies) == 0:
			self.get_http_headers().delete("Cookie")


	# READ RequestBody
	def get_request_body(self):
		return self.__RequestBody

	def get_request_body_param(self, name):
		if self.get_request_body().get("dataType") in [None, "unknown"]:
			return self.get_request_body().get("data")
		else:
			return self.get_request_body().get(self.__separator.join(["data", name]), separator=self.__separator, parse_index=self.__parse_index)

	# CREATE RequestBody
	def set_request_body_param(self, name, value):
		if self.get_request_body().get("dataType") != None:
			if self.get_request_body().get("dataType") == "unknown":
				if type(value) == str:
					self.get_request_body().update("data", value)
			else:
				self.get_request_body().set(self.__separator.join(["data", name]), value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, ordered_dict=self.__ordered_dict)

	def set_request_body_params(self, RequestBodyObj):
		if type(RequestBodyObj) in [dict, OrderedDict]:
			for name in RequestBodyObj:
				self.set_request_body_param(name, RequestBodyObj[name])

	# UPDATE RequestBody
	def update_request_body_param(self, name, value):
		if self.get_request_body().get("dataType") != None:
			if self.get_request_body().get("dataType") == "unknown":
				if type(value) == str:
					self.get_request_body().update("data", value)
			else:
				self.get_request_body().update(self.__separator.join(["data", name]), value, separator=self.__separator, parse_index=self.__parse_index)

	def update_request_body_params(self, RequestBodyObj):
		if type(RequestBodyObj) in [dict, OrderedDict]:
			for name in RequestBodyObj:
				self.update_request_body_param(name, RequestBodyObj[name])

	# DELETE RequestBody
	def delete_request_body(self):
		if self.get_request_body().get("dataType") != None:
			if self.get_request_body().get("dataType") == "unknown":
				self.get_request_body().update("data", "")
			else:
				self.get_request_body().update("data", {})

	def delete_request_body_param(self, name):
		if self.get_request_body().get("dataType") != None:
			if self.get_request_body().get("dataType") == "unknown":
				self.get_request_body().update("data", "")
			else:
				self.get_request_body().delete(self.__separator.join(["data", name]), separator=self.__separator, parse_index=self.__parse_index)

	def delete_request_body_params(self, RequestBodyList):
		for name in RequestBodyList:
			self.delete_request_body_param(name)



	# send HTTP request to server
	def sendRequest(self, Host, Port, Scheme, injectObj=dict(), Timeout=10, update_content_length=True, proxy_server=None):
		# Clone self Object
		httpReq = copy.deepcopy(self)

		if type(injectObj) in [dict, OrderedDict]:
			# Inject RequestMethod object
			if "RequestMethod" in injectObj:
				httpReq.set_request_method(injectObj["RequestMethod"])

			# Inject PathParams object
			if "PathParams" in injectObj:
				httpReq.update_path_params(injectObj["PathParams"])

			# Inject QueryParams object
			if "QueryParams" in injectObj:
				httpReq.update_query_params(injectObj["QueryParams"])

			# Inject URIFragment object
			if "URIFragment" in injectObj:
				httpReq.set_uri_fragment(injectObj["URIFragment"])

			# Inject HTTPVersion object
			if "HTTPVersion" in injectObj:
				httpReq.set_http_version(injectObj["HTTPVersion"])

			# Inject HTTPHeaders object
			if "HTTPHeaders" in injectObj:
				httpReq.update_http_headers(injectObj["HTTPHeaders"])

			# Inject HTTPCookies object
			if "HTTPCookies" in injectObj:
				httpReq.update_http_cookies(injectObj["HTTPCookies"])

			# Inject RequestBody object
			if "RequestBody" in injectObj:
				httpReq.update_request_body_params(injectObj["RequestBody"])


		# Prepare the HTTP request
		# rr_method
		rr_method = httpReq.get_request_method()

		# rr_path
		path_split = httpReq.get_request_path().split("/")
		for i in range(len(path_split)):
			if httpReq.get_path_param(path_split[i]) != "JSON_DUPLICATE_KEYS_ERROR":
				path_split[i] = httpReq.get_path_param(path_split[i])
		rr_path = "/".join(path_split)
		if len(rr_path) == 0: rr_path += "/"

		# rr_query
		rr_query = "?"+"&".join([jdks.normalize_key(name)+"="+httpReq.get_query_param(name) for name in httpReq.get_query_params().getObject()]) if len(httpReq.get_query_params().getObject())>0 else ""

		# rr_fragment
		rr_fragment = "#"+httpReq.get_uri_fragment() if len(httpReq.get_uri_fragment())>0 else ""

		# rr_httpversion
		rr_httpversion = httpReq.get_http_version()

		# rr_body
		if httpReq.get_request_body().get("dataType") == "json":
			rr_body = jdks.JSON_DUPLICATE_KEYS(httpReq.get_request_body().get("data")).dumps()
		elif httpReq.get_request_body().get("dataType") == "form-urlencoded":
			rr_body = "&".join([jdks.normalize_key(name)+"="+httpReq.get_request_body().get("data")[name] for name in httpReq.get_request_body().get("data")])
		elif httpReq.get_request_body().get("dataType") == "multipart":
			rr_body = ""
			for name in httpReq.get_request_body().get("data"):
				rr_body += "--"+httpReq.get_request_body().get("boundary")+"\r\n"
				rr_body += "Content-Disposition: form-data; name=\""+jdks.normalize_key(name)+"\""
				if httpReq.get_request_body_param(self.__separator.join([name, "filename"])) != "JSON_DUPLICATE_KEYS_ERROR":
					rr_body += "; filename=\""+httpReq.get_request_body_param(self.__separator.join([name, "filename"]))+"\""
				rr_body += "\r\n"
				if httpReq.get_request_body_param(self.__separator.join([name, "headers"])) != "JSON_DUPLICATE_KEYS_ERROR" and type(httpReq.get_request_body_param(self.__separator.join([name, "headers"]))) in [dict, OrderedDict]:
					for headerName in httpReq.get_request_body_param(self.__separator.join([name, "headers"])):
						rr_body += jdks.normalize_key(headerName)+": "+httpReq.get_request_body_param(self.__separator.join([name, "headers"]))[headerName] + "\r\n"
				rr_body += "\r\n"
				if httpReq.get_request_body_param(self.__separator.join([name, "value"])) != "JSON_DUPLICATE_KEYS_ERROR":
					rr_body += httpReq.get_request_body_param(self.__separator.join([name, "value"]))
				rr_body += "\r\n"

			rr_body += "--"+httpReq.get_request_body().get("boundary")+"--\r\n"
		elif httpReq.get_request_body().get("dataType") == "unknown":
			rr_body = httpReq.get_request_body().get("data")
		else:
			rr_body = ""

		# rr_headers
		rr_headers = ""
		if update_content_length:
			if len(rr_body) > 0:
				if httpReq.get_http_header("Content-Length") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Length", str(len(rr_body)))
				else:
					httpReq.update_http_header("Content-Length", str(len(rr_body)))
			elif rr_method in ["POST", "PUT", "PATCH"]:
				if httpReq.get_http_header("Content-Length") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Length", "0")
				else:
					httpReq.update_http_header("Content-Length", "0")

		if len(rr_body) > 0 and httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
			if httpReq.get_request_body().get("dataType") == "json":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/json")
				else:
					httpReq.update_http_header("Content-Type", "application/json")
			elif httpReq.get_request_body().get("dataType") == "form-urlencoded":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/x-www-form-urlencoded")
				else:
					httpReq.update_http_header("Content-Type", "application/x-www-form-urlencoded")
			elif httpReq.get_request_body().get("dataType") == "multipart":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "multipart/form-data; boundary="+httpReq.get_request_body().get("boundary"))
				else:
					httpReq.update_http_header("Content-Type", "multipart/form-data; boundary="+httpReq.get_request_body().get("boundary"))
			elif httpReq.get_request_body().get("dataType") == "unknown":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/octet-stream")
				else:
					httpReq.update_http_header("Content-Type", "application/octet-stream")

		rr_headers = "\r\n".join([jdks.normalize_key(name)+": "+str(httpReq.get_http_header(name)) for name in httpReq.get_http_headers().getObject()]) if len(httpReq.get_http_headers().getObject())>0 else ""
		if len(rr_headers) > 0: rr_headers = "\r\n"+rr_headers


		rawRequest = f"{rr_method} {rr_path}{rr_query}{rr_fragment} {rr_httpversion}{rr_headers}\r\n\r\n{rr_body}"


		# Create a socket connection
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client_socket.settimeout(Timeout)


		# Connect to the proxy/ server
		if proxy_server != None:
			try:
				client_socket.connect((proxy_server["host"], proxy_server["port"]))
			except Exception as e:
				exit(e)
		else:
			client_socket.connect((Host, Port))


		# Perform SSL/TLS handshake with the target server
		if Scheme == "https":
			context = ssl.create_default_context()
			context.check_hostname = False
			context.verify_mode = ssl.CERT_NONE
			client_socket = context.wrap_socket(client_socket, server_side=False, server_hostname=Host)

		request_timestamp = int(time.time()*1000)

		# Send the HTTP request
		client_socket.sendall(rawRequest.encode())

		# Receive and process the server's response
		rawResponse = b""
		while True:
			chunk = client_socket.recv(4096)
			if not chunk:
				break
			rawResponse += chunk

		response_timestamp = int(time.time()*1000)

		# Close the connections
		client_socket.close()

		return {
			"rawRequest": rawRequest,
			"rawResponse": rawResponse.decode(),
			"request_timestamp": request_timestamp,
			"response_timestamp": response_timestamp
		}