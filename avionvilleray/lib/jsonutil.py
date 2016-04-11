import json

from collections import OrderedDict


def encode(content):
    return json.dumps(content, sort_keys=True)


def decode(content):
    return json.loads(content.decode("utf8"), object_pairs_hook=OrderedDict)
