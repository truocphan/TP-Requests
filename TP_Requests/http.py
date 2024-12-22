import json_duplicate_keys as jdks, socket, ssl, copy, time
from TP_HTTP_Request_Response_Parser import TP_HTTP_REQUEST_PARSER

class TP_HTTP_REQUEST:
	def __init__(self, rawRequest:str, separator:str="||", parse_index:str="$", dupSign_start:str="{{{", dupSign_end:str="}}}", ordered_dict:bool=False) -> None:
		self.__version = "2025.1.1"

		self.RequestParser = TP_HTTP_REQUEST_PARSER(rawRequest, separator=separator, parse_index=parse_index, dupSign_start=dupSign_start, dupSign_end=dupSign_end, ordered_dict=ordered_dict)

		if self.RequestParser.request_headers.get("User-Agent", case_insensitive=True)["value"] == "JSON_DUPLICATE_KEYS_ERROR":
			self.RequestParser.request_headers.set("User-Agent", "TP-Requests (http/TP_HTTP_REQUEST "+self.__version+")")
		if self.RequestParser.request_headers.get("Connection", case_insensitive=True)["value"] == "JSON_DUPLICATE_KEYS_ERROR":
			self.RequestParser.request_headers.set("Connection", "close")



	def sendRequest(self, Host:str, Port:int, Scheme:str, timeout:int=30, update_content_length:bool=True, proxy_server:dict=None) -> dict:
		rawRequest = self.RequestParser.unparse(update_content_length=update_content_length)
		rawResponse = None
		request_timestamp = response_timestamp = 0

		try:
			# Create a socket connection
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client_socket.settimeout(timeout)

			# Connect to the proxy/ server
			if type(proxy_server) == dict:
				try:
					client_socket.connect((proxy_server["host"], proxy_server["port"]))
				except Exception as e:
					client_socket.connect((Host, Port))
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
			rawResponse = rawResponse.decode()
		except Exception as e:
			pass

		return jdks.JSON_DUPLICATE_KEYS({
			"Host": Host,
			"Port": Port,
			"Scheme": Scheme,
			"rawRequest": rawRequest,
			"rawResponse": rawResponse,
			"request_timestamp": request_timestamp,
			"response_timestamp": response_timestamp
		})