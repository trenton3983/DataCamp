import json


def get_api_key(api_name):
    """

    :param api_name:
    :return:
    """
    # Load JSON: json_data
    with open("api_keys.json") as json_file:
        json_data = json.load(json_file)

    api_key = json_data[api_name]['key']
    example = json_data[api_name]['example']

    return api_key, example


if __name__ == '__main__':

    api_key, example, = get_api_key('omdb')
    print('API Key: ', api_key)
    print('Example: ', example)
