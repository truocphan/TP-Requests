import setuptools
import datetime

setuptools.setup(
	name="TP_Requests",
	version=datetime.datetime.now().strftime("%Y.%m.%d"),
	author="Truoc Phan",
	license="MIT",
	author_email="truocphan112017@gmail.com",
	description="Send HTTP Request",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=open("requirements.txt").read().split(),
	url="https://github.com/truocphan/TP-Requests",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["TP_Requests", "TP_HTTP_REQUEST", "TP_MQTT_REQUEST", "TP_WEBSOCKET_REQUEST"],
	packages=["TP_Requests"],
)