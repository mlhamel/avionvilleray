import requests


class Dump1090Client:
    def __init__(self, host):
        self.host = host

    def get_url(self):
        return "http://{host}/data.json".format(host=self.host)

    def receive(self)
        content = requests.get(self.get_url()).content
        return jsonutil.decode(content)
