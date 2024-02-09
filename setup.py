import setuptools

setuptools.setup(
	name="TP_Requests",
	version="2024.2.9",
	author="TP Cyber Security",
	license="MIT",
	author_email="tpcybersec2023@gmail.com",
	description="Send the HTTP/ MQTT/ WEBSOCKET Request",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=open("requirements.txt").read().split(),
	url="https://github.com/truocphan/TP-Requests",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: Implementation :: Jython"
	],
	keywords=["TPCyberSec", "TP_Requests", "TP_HTTP_REQUEST", "TP_MQTT_REQUEST", "TP_WEBSOCKET_REQUEST"],
	packages=["TP_Requests"],
)