import requests
import json


class DataDumper(object):
    """ Dump data from dump1090 rest api """
    @staticmethod
    def execute(host="127.0.0.1:8080"):
        url = "http://{host}/data.json".format(host=host)
        data = requests.get(url).content
        data = json.loads(data.decode("utf8"))
        print(data)


def main():
    DataDumper().execute()


if __name__ == "__main__":
    main()
