import json_duplicate_keys as jdks, socket, ssl, copy, uuid
from collections import OrderedDict
from urllib.parse import urlparse
from TP_HTTP_Request_Response_Parser import *

class TP_HTTP_REQUEST:
	def __init__(self, PathParams=dict(), QueryParams=dict(), URIFragment=str(), HTTPVersion="HTTP/1.1", HTTPHeaders=dict(), BodyJson=None, BodyData=dict(), BodyFiles=dict(), BodyContent=str(), dupSign_start="{{{", dupSign_end="}}}", separator="||", parse_index="$", _isDebug_=False):
		self.__dupSign_start = dupSign_start if type(dupSign_start) == str else "{{{"
		self.__dupSign_end = dupSign_end if type(dupSign_end) == str else "}}}"
		self.__separator = separator if type(separator) == str else"||"
		self.__parse_index = parse_index if type(parse_index) == str else "$"
		self.___isDebug_ = _isDebug_ if type(_isDebug_) == bool else False

		# TP_HTTP_REQUEST version
		self.__version = "2023.8.20"

		# Body content type
		self.__BodyType = None

		# initialization PathParams
		"""
		{
			"PathParams_name1": PathParams_value1,
			"PathParams_name2": PathParams_value2,
			...
		}
		"""
		self.__PathParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if type(PathParams) in [dict, OrderedDict]:
			self.__PathParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(PathParams))
		elif type(PathParams) == jdks.JSON_DUPLICATE_KEYS:
			self.__PathParams = copy.deepcopy(PathParams)

		# initialization QueryParams
		"""
		{
			"QueryParams_name1": QueryParams_value1,
			"QueryParams_name2": QueryParams_value2,
			...
		}
		"""
		self.__QueryParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if type(QueryParams) in [dict, OrderedDict]:
			self.__QueryParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(QueryParams))
		elif type(QueryParams) == jdks.JSON_DUPLICATE_KEYS:
			self.__QueryParams = copy.deepcopy(QueryParams)

		# initialization URIFragment
		"""
		"URIFragment"
		"""
		self.__URIFragment = str()
		if type(URIFragment) == str:
			self.__URIFragment = URIFragment

		# initialization HTTPVersion
		"""
		"HTTP/1.1"
		"""
		self.__HTTPVersion = "HTTP/1.1"
		if type(HTTPVersion) == str:
			self.__HTTPVersion = HTTPVersion

		# initialization HTTPHeaders
		"""
		{
			"HTTPHeaders_name1": HTTPHeaders_value1,
			"HTTPHeaders_name2": HTTPHeaders_value2,
			...
		}
		"""
		self.__HTTPHeaders = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if type(HTTPHeaders) in [dict, OrderedDict]:
			self.__HTTPHeaders = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(HTTPHeaders))
		elif type(HTTPHeaders) == jdks.JSON_DUPLICATE_KEYS:
			self.__HTTPHeaders = copy.deepcopy(HTTPHeaders)

		if self.__HTTPHeaders.get("User-Agent", separator=self.__separator, parse_index=self.__parse_index) == "JSON_DUPLICATE_KEYS_ERROR":
			self.__HTTPHeaders.set("User-Agent", "TP_Requests (http/TP_HTTP_REQUEST "+self.__version+")", separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)
		if self.__HTTPHeaders.get("Connection", separator=self.__separator, parse_index=self.__parse_index) == "JSON_DUPLICATE_KEYS_ERROR":
			self.__HTTPHeaders.set("Connection", "close", separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)

		# initialization HTTPCookies
		"""
		{
			"HTTPCookies_name1": HTTPCookies_value1,
			"HTTPCookies_name2": HTTPCookies_value2,
			...
		}
		"""
		self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index) != "JSON_DUPLICATE_KEYS_ERROR":
			for cookie in str(self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index)).split(";"):
				if len(cookie.split("=", 1)) == 2:
					self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip(), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)
				else:
					self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "", separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)

		# initialization BodyJson
		"""
		{
			"BodyJson_name1": BodyJson_value1,
			"BodyJson_name2": BodyJson_value2,
			...
		}
		"""
		self.__BodyJson = None
		if type(BodyJson) in [dict, OrderedDict, list]:
			self.__BodyJson = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(BodyJson))
		elif type(BodyJson) == jdks.JSON_DUPLICATE_KEYS:
			self.__BodyJson = copy.deepcopy(BodyJson)

		# initialization BodyData
		"""
		{
			"BodyData_name1": BodyData_value1,
			"BodyData_name2": BodyData_value2,
			...
		}
		"""
		self.__BodyData = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if type(BodyData) in [dict, OrderedDict]:
			self.__BodyData = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(BodyData))
		elif type(BodyData) == jdks.JSON_DUPLICATE_KEYS:
			self.__BodyData = copy.deepcopy(BodyData)

		# initialization BodyFiles
		"""
		{
			"BodyFiles_name1": {
				"filename": "",
				"headers": {
					"BodyFiles_headerName1": BodyFiles_headerValue1,
					"BodyFiles_headerName2": BodyFiles_headerValue2,
					...
				},
				"value": value
			},
			"BodyFiles_name2": {
				"filename": "",
				"headers": {
					"BodyFiles_headerName1": BodyFiles_headerValue1,
					"BodyFiles_headerName2": BodyFiles_headerValue2,
					...
				},
				"value": value
			},
			...
		}
		"""
		self.__BodyFiles = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		if type(BodyFiles) in [dict, OrderedDict]:
			self.__BodyFiles = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS(BodyFiles))
		elif type(BodyFiles) == jdks.JSON_DUPLICATE_KEYS:
			self.__BodyFiles = copy.deepcopy(BodyFiles)

		# initialization BodyContent
		"""
		"BodyContent"
		"""
		self.__BodyContent = str()
		if type(BodyContent) == str:
			self.__BodyContent = BodyContent

		# Requests/ Responses
		self.__HTTPRequestsResponses = list()


	# READ PathParams
	def get_path_params(self):
		if type(self.__PathParams) == jdks.JSON_DUPLICATE_KEYS:
			return self.__PathParams
		else:
			self.__PathParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			return self.__PathParams

	def get_path_param(self, name):
		return str(self.get_path_params().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_))


	# READ QueryParams
	def get_query_params(self):
		if type(self.__QueryParams) == jdks.JSON_DUPLICATE_KEYS:
			return self.__QueryParams
		else:
			self.__QueryParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			return self.__QueryParams

	def get_query_param(self, name):
		return str(self.get_query_params().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_))


	# READ URIFragment
	def get_uri_fragment(self):
		if type(self.__URIFragment) == str:
			return self.__URIFragment
		else:
			self.__URIFragment = str()
			return self.__URIFragment


	# READ HTTPVersion
	def get_http_version(self):
		if type(self.__HTTPVersion) == str:
			return self.__HTTPVersion
		else:
			self.__HTTPVersion = "HTTP/1.1"
			return self.__HTTPVersion


	# READ HTTPHeaders
	def get_http_headers(self):
		if type(self.__HTTPHeaders) == jdks.JSON_DUPLICATE_KEYS:
			return self.__HTTPHeaders
		else:
			self.__HTTPHeaders = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			return self.__HTTPHeaders

	def get_http_header(self, name):
		return str(self.get_http_headers().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_))


	# READ HTTPCookies
	def get_http_cookies(self):
		if type(self.__HTTPCookies) == jdks.JSON_DUPLICATE_KEYS:
			return self.__HTTPCookies
		else:
			self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			return self.__HTTPCookies

	def get_http_cookie(self, name):
		return str(self.get_http_cookies().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_))


	# READ BodyJson
	def get_body_json_params(self):
		if type(self.__BodyJson) == jdks.JSON_DUPLICATE_KEYS:
			return self.__BodyJson
		else:
			self.__BodyJson = None
			return self.__BodyJson

	def get_body_json_param(self, name):
		if type(self.get_body_json_params()) == jdks.JSON_DUPLICATE_KEYS:
			return self.get_body_json_params().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)
		return "JSON_DUPLICATE_KEYS_ERROR"


	# READ BodyData
	def get_body_data_params(self):
		if type(self.__BodyData) == jdks.JSON_DUPLICATE_KEYS:
			return self.__BodyData
		else:
			self.__BodyData = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			return self.__BodyData

	def get_body_data_param(self, name):
		return str(self.get_body_data_params().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_))


	# READ BodyFiles
	def get_body_files_params(self):
		JDKSObject = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

		if type(self.__BodyFiles) == jdks.JSON_DUPLICATE_KEYS:
			for name in self.__BodyFiles.getObject():
				JDKSObject.set(name, dict(), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
				if type(self.__BodyFiles.get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)) in [dict, OrderedDict]:
					if self.__BodyFiles.get(self.__separator.join([name,"filename"]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
						JDKSObject.set(self.__separator.join([name,"filename"]), self.__BodyFiles.get(self.__separator.join([name,"filename"]), separator=self.__separator, parse_index=self.__parse_index), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

					if self.__BodyFiles.get(self.__separator.join([name,"headers"]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
						JDKSObject.set(self.__separator.join([name,"headers"]), dict(), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
						if type(self.__BodyFiles.get(self.__separator.join([name,"headers"]), separator=self.__separator, parse_index=self.__parse_index)) in [dict, OrderedDict]:
							for h in self.__BodyFiles.get(self.__separator.join([name,"headers"]), separator=self.__separator, parse_index=self.__parse_index):
								JDKSObject.set(self.__separator.join([name,"headers",h]), self.__BodyFiles.get(self.__separator.join([name,"headers",h]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

					if self.__BodyFiles.get(self.__separator.join([name,"value"]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
						JDKSObject.set(self.__separator.join([name,"value"]), self.__BodyFiles.get(self.__separator.join([name,"value"]), separator=self.__separator, parse_index=self.__parse_index), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

		self.__BodyFiles = JDKSObject
		return JDKSObject


	def get_body_files_param(self, name):
		return self.get_body_files_params().get(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)


	# READ BodyContent
	def get_body_content(self):
		if type(self.__BodyContent) == str:
			return self.__BodyContent
		else:
			self.__BodyContent = str()
			return self.__BodyContent


	# READ HTTP Requests/ Responses List
	def get_http_requests_responses(self):
		if type(self.__HTTPRequestsResponses) == list:
			return self.__HTTPRequestsResponses
		else:
			self.__HTTPRequestsResponses = list()
			return self.__HTTPRequestsResponses



	# CREATE PathParams
	def set_path_param(self, name, value):
		self.get_path_params().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_path_params(self, PathParamsObj):
		if type(PathParamsObj) in [dict, OrderedDict]:
			for name in PathParamsObj:
				self.set_path_param(name, PathParamsObj[name])

	# UPDATE PathParams
	def update_path_param(self, name, value):
		self.get_path_params().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_path_params(self, PathParamsObj):
		if type(PathParamsObj) in [dict, OrderedDict]:
			for name in PathParamsObj:
				self.update_path_param(name, PathParamsObj[name])


	# CREATE QueryParams
	def set_query_param(self, name, value):
		self.get_query_params().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_query_params(self, QueryParamsObj):
		if type(QueryParamsObj) in [dict, OrderedDict]:
			for name in QueryParamsObj:
				self.set_query_param(name, QueryParamsObj[name])

	# UPDATE QueryParams
	def update_query_param(self, name, value):
		self.get_query_params().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_query_params(self, QueryParamsObj):
		if type(QueryParamsObj) in [dict, OrderedDict]:
			for name in QueryParamsObj:
				self.update_query_param(name, QueryParamsObj[name])


	# CREATE/ UPDATE URIFragment
	def set_uri_fragment(self, value):
		self.__URIFragment = str(value)


	# CREATE/ UPDATE HTTPVersion
	def set_http_version(self, value):
		self.__HTTPVersion = str(value)


	# CREATE HTTPHeaders
	def set_http_header(self, name, value):
		self.get_http_headers().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
		if name == "Cookie":
			self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			if self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
				for cookie in str(self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index)).split(";"):
					if len(cookie.split("=", 1)) == 2:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip(), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
					else:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "", separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_http_headers(self, HTTPHeadersObj):
		if type(HTTPHeadersObj) in [dict, OrderedDict]:
			for name in HTTPHeadersObj:
				self.set_http_header(name, HTTPHeadersObj[name])

	# UPDATE HTTPHeaders
	def update_http_header(self, name, value):
		self.get_http_headers().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)
		if name == "Cookie":
			self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
			if self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) != "JSON_DUPLICATE_KEYS_ERROR":
				for cookie in str(self.__HTTPHeaders.get("Cookie", separator=self.__separator, parse_index=self.__parse_index)).split(";"):
					if len(cookie.split("=", 1)) == 2:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), cookie.split("=", 1)[1].strip(), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
					else:
						self.__HTTPCookies.set(cookie.split("=", 1)[0].strip(), "", separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def update_http_headers(self, HTTPHeadersObj):
		if type(HTTPHeadersObj) in [dict, OrderedDict]:
			for name in HTTPHeadersObj:
				self.update_http_header(name, HTTPHeadersObj[name])


	# CREATE HTTPCookies
	def set_http_cookie(self, name, value):
		self.get_http_cookies().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

		if self.get_http_headers().get("Cookie", separator=self.__separator, parse_index=self.__parse_index) == "JSON_DUPLICATE_KEYS_ERROR":
			self.get_http_headers().set("Cookie", "; ".join([jdks.normalize_key(cname, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"="+self.get_http_cookies().get(cname, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) for cname in self.get_http_cookies().getObject()]), separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)
		else:
			self.get_http_headers().update("Cookie", "; ".join([jdks.normalize_key(cname, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"="+self.get_http_cookies().get(cname, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) for cname in self.get_http_cookies().getObject()]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def set_http_cookies(self, HTTPCookiesObj):
		if type(HTTPCookiesObj) in [dict, OrderedDict]:
			for name in HTTPCookiesObj:
				self.set_http_cookie(name, HTTPCookiesObj[name])

	# UPDATE HTTPCookies
	def update_http_cookie(self, name, value):
		self.get_http_cookies().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

		self.get_http_headers().update("Cookie", "; ".join([jdks.normalize_key(cname, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"="+self.get_http_cookies().get(cname, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_) for cname in self.get_http_cookies().getObject()]), separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_http_cookies(self, HTTPCookiesObj):
		if type(HTTPCookiesObj) in [dict, OrderedDict]:
			for name in HTTPCookiesObj:
				self.update_http_cookie(name, HTTPCookiesObj[name])


	# CREATE BodyJson
	def set_body_json_param(self, name, value):
		if type(self.get_body_json_params()) != jdks.JSON_DUPLICATE_KEYS:
			self.__BodyJson = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

		self.get_body_json_params().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_body_json_params(self, BodyJsonObj):
		if type(BodyJsonObj) in [dict, OrderedDict]:
			for name in BodyJsonObj:
				self.set_body_json_param(name, BodyJsonObj[name])

	# UPDATE BodyJson
	def update_body_json_param(self, name, value):
		self.get_body_json_params().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_body_json_params(self, BodyJsonObj):
		if type(BodyJsonObj) in [dict, OrderedDict]:
			for name in BodyJsonObj:
				self.update_body_json_param(name, BodyJsonObj[name])


	# CREATE BodyData
	def set_body_data_param(self, name, value):
		self.get_body_data_params().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_body_data_params(self, BodyDataObj):
		if type(BodyDataObj) in [dict, OrderedDict]:
			for name in BodyDataObj:
				self.set_body_data_param(name, BodyDataObj[name])

	# UPDATE BodyData
	def update_body_data_param(self, name, value):
		self.get_body_data_params().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_body_data_params(self, BodyDataObj):
		if type(BodyDataObj) in [dict, OrderedDict]:
			for name in BodyDataObj:
				self.update_body_data_param(name, BodyDataObj[name])


	# CREATE BodyFiles
	def set_body_files_param(self, name, value):
		self.get_body_files_params().set(name, value, separator=self.__separator, parse_index=self.__parse_index, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end, _isDebug_=self.___isDebug_)

	def set_body_files_params(self, BodyFilesObj):
		if type(BodyFilesObj) in [dict, OrderedDict]:
			for name in BodyFilesObj:
				self.set_body_files_param(name, BodyFilesObj[name])

	# UPDATE BodyFiles
	def update_body_files_param(self, name, value):
		self.get_body_files_params().update(name, value, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

	def update_body_files_params(self, BodyFilesObj):
		if type(BodyFilesObj) in [dict, OrderedDict]:
			for name in BodyFilesObj:
				self.update_body_files_param(name, BodyFilesObj[name])


	# CREATE/ UPDATE BodyContent
	def set_body_content(self, value):
		self.__BodyContent = str(value)



	# DELETE PathParams
	def delete_path_params(self):
		self.__PathParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

	def delete_path_param(self, PathParamsList):
		for name in PathParamsList:
			self.get_path_params().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)


	# DELETE QueryParams
	def delete_query_params(self):
		self.__QueryParams = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

	def delete_query_param(self, QueryParamsList):
		for name in QueryParamsList:
			self.get_query_params().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)


	# DELETE URIFragment
	def delete_uri_fragment(self):
		self.__URIFragment = str()


	# DELETE HTTPVersion
	def delete_http_version(self):
		self.__HTTPVersion = str()


	# DELETE HTTPHeaders
	def delete_http_headers(self):
		self.__HTTPHeaders = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

	def delete_http_header(self, HTTPHeadersList):
		for name in HTTPHeadersList:
			self.get_http_headers().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

			if name == "Cookie":
				self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))


	# DELETE HTTPCookies
	def delete_http_cookies(self):
		self.__HTTPCookies = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))
		self.get_http_headers().delete("Cookie", separator=self.__separator, parse_index=self.__parse_index)

	def delete_http_cookie(self, HTTPCookiesList):
		for name in HTTPCookiesList:
			self.get_http_cookies().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)

		if len(self.__HTTPCookies) == 0:
			self.get_http_headers().delete("Cookie", separator=self.__separator, parse_index=self.__parse_index)


	# DELETE BodyJson
	def delete_body_json_params(self):
		self.__BodyJson = None

	def delete_body_json_param(self, BodyJsonList):
		if type(self.get_body_json_params()) == jdks.JSON_DUPLICATE_KEYS:
			for name in BodyJsonList:
				self.get_body_json_params().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)
		else:
			self.__BodyJson = None


	# DELETE BodyData
	def delete_body_data_params(self):
		self.__BodyData = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

	def delete_body_data_param(self, BodyDataList):
		for name in BodyDataList:
			self.get_body_data_params().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)


	# DELETE BodyFiles
	def delete_body_files_params(self):
		self.__BodyFiles = copy.deepcopy(jdks.JSON_DUPLICATE_KEYS({}))

	def delete_body_files_param(self, BodyFilesList):
		for name in BodyFilesList:
			self.get_body_files_params().delete(name, separator=self.__separator, parse_index=self.__parse_index, _isDebug_=self.___isDebug_)


	# DELETE BodyContent
	def delete_body_content(self):
		self.__BodyContent = str()



	# send HTTP request to server
	def request(self, method, url, injectObj=dict(), update_content_length=True, proxy_server=None):
		# Clone self Object
		httpReq = copy.deepcopy(self)

		# Parse request url
		scheme = urlparse(url).scheme
		netloc = urlparse(url).netloc
		path = urlparse(url).path

		if type(injectObj) in [dict, OrderedDict]:
			# Inject PathParams object
			if "PathParams" in injectObj.keys():
				httpReq.update_path_params(injectObj["PathParams"])

			# Inject QueryParams object
			if "QueryParams" in injectObj.keys():
				httpReq.update_query_params(injectObj["QueryParams"])

			# Inject URIFragment object
			if "URIFragment" in injectObj.keys():
				httpReq.set_uri_fragment(injectObj["URIFragment"])

			# Inject HTTPHeaders object
			if "HTTPHeaders" in injectObj.keys():
				httpReq.update_http_headers(injectObj["HTTPHeaders"])

			# Inject HTTPCookies object
			if "HTTPCookies" in injectObj.keys():
				httpReq.update_http_cookies(injectObj["HTTPCookies"])

			# Inject BodyJson object
			if "BodyJson" in injectObj.keys():
				httpReq.update_body_json_params(injectObj["BodyJson"])

			# Inject BodyData object
			if "BodyData" in injectObj.keys():
				httpReq.update_body_data_params(injectObj["BodyData"])

			# Inject BodyFiles object
			if "BodyFiles" in injectObj.keys():
				httpReq.update_body_files_params(injectObj["BodyFiles"])

			# Inject BodyContent object
			if "BodyContent" in injectObj.keys():
				httpReq.set_body_content(injectObj["BodyContent"])


		# Prepare the HTTP request
		# rr_method
		rr_method = method
		if type(method) not in [str]:
			rr_method = str(method)

		# rr_path
		path_split = path.split("/")
		for i in range(len(path_split)):
			if httpReq.get_path_param(path_split[i]) != "JSON_DUPLICATE_KEYS_ERROR":
				path_split[i] = httpReq.get_path_param(path_split[i])
		rr_path = "/".join(path_split)
		if len(rr_path) == 0: rr_path += "/"

		# rr_query
		rr_query = "?"+"&".join([jdks.normalize_key(name, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"="+httpReq.get_query_param(name) for name in httpReq.get_query_params().getObject()]) if len(httpReq.get_query_params().getObject())>0 else ""

		# rr_fragment
		rr_fragment = "#"+httpReq.get_uri_fragment() if len(httpReq.get_uri_fragment())>0 else ""

		# rr_httpversion
		rr_httpversion = httpReq.get_http_version()

		# rr_body
		if type(httpReq.get_body_json_params()) == jdks.JSON_DUPLICATE_KEYS:
			rr_body = httpReq.get_body_json_params().dumps()
			httpReq.__BodyType = "BodyJson"
		elif len(httpReq.get_body_data_params().getObject()) > 0:
			rr_body = "&".join([jdks.normalize_key(name, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"="+httpReq.get_body_data_param(name) for name in httpReq.get_body_data_params().getObject()])
			httpReq.__BodyType = "BodyData"
		elif len(httpReq.get_body_files_params().getObject()) > 0:
			boundaryID = "-"*26+uuid.uuid4().hex[-24:]
			rr_body = ""
			for name in httpReq.get_body_files_params().getObject():
					httpReq.__BodyType = "BodyFiles"
					rr_body += "--"+boundaryID+"\r\n"
					rr_body += "Content-Disposition: form-data; name=\""+jdks.normalize_key(name, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+"\""
					if httpReq.get_body_files_param(httpReq.__separator.join([name,"filename"])) != "JSON_DUPLICATE_KEYS_ERROR":
						rr_body += "; filename=\""+httpReq.get_body_files_param(httpReq.__separator.join([name,"filename"]))+"\""
					rr_body += "\r\n"
					if httpReq.get_body_files_param(httpReq.__separator.join([name,"headers"])) != "JSON_DUPLICATE_KEYS_ERROR" and type(httpReq.get_body_files_param(httpReq.__separator.join([name,"headers"]))) in [dict, OrderedDict]:
						for headerName in httpReq.get_body_files_param(httpReq.__separator.join([name,"headers"])):
							rr_body += jdks.normalize_key(headerName, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+": "+httpReq.get_body_files_param(httpReq.__separator.join([name,"headers"]))[headerName] + "\r\n"
					rr_body += "\r\n"
					if httpReq.get_body_files_param(httpReq.__separator.join([name,"value"])) != "JSON_DUPLICATE_KEYS_ERROR":
						rr_body += httpReq.get_body_files_param(httpReq.__separator.join([name,"value"]))
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
				if httpReq.get_http_header("Content-Length") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Length", len(rr_body))
				else:
					httpReq.update_http_header("Content-Length", len(rr_body))
			elif rr_method in ["POST", "PUT", "PATCH"]:
				if httpReq.get_http_header("Content-Length") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Length", 0)
				else:
					httpReq.update_http_header("Content-Length", 0)

		if len(rr_body) > 0 and httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
			if httpReq.__BodyType == "BodyJson":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/json")
				else:
					httpReq.update_http_header("Content-Type", "application/json")
			elif httpReq.__BodyType == "BodyData":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/x-www-form-urlencoded")
				else:
					httpReq.update_http_header("Content-Type", "application/x-www-form-urlencoded")
			elif httpReq.__BodyType == "BodyFiles":
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "multipart/form-data; boundary="+boundaryID)
				else:
					httpReq.update_http_header("Content-Type", "multipart/form-data; boundary="+boundaryID)
			else:
				if httpReq.get_http_header("Content-Type") == "JSON_DUPLICATE_KEYS_ERROR":
					httpReq.set_http_header("Content-Type", "application/octet-stream")
				else:
					httpReq.update_http_header("Content-Type", "application/octet-stream")

		rr_headers = "\r\n".join([jdks.normalize_key(name, dupSign_start=self.__dupSign_start, dupSign_end=self.__dupSign_end)+": "+httpReq.get_http_header(name) for name in httpReq.get_http_headers().getObject()]) if len(httpReq.get_http_headers().getObject())>0 else ""
		if len(rr_headers) > 0: rr_headers = "\r\n"+rr_headers


		rawRequest = f"{rr_method} {rr_path}{rr_query}{rr_fragment} {rr_httpversion}{rr_headers}\r\n\r\n{rr_body}"


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
			try:
				client_socket.connect((str(proxy_server["host"]), int(proxy_server["port"])))
			except Exception as e:
				exit("Invalid proxy_server")
		else:
			client_socket.connect((server_hostname, server_port))


		# Perform SSL/TLS handshake with the target server
		if scheme == "https":
			context = ssl.create_default_context()
			context.check_hostname = False
			context.verify_mode = ssl.CERT_NONE
			client_socket = context.wrap_socket(client_socket, server_side=False, server_hostname=server_hostname)


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

		return TP_HTTP_RESPONSE_PARSER(rawResponse.decode())