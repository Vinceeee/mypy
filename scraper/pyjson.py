import json,os

def main():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path)

    with open("{0}/samples/kugoo_song_sample.json".format(dir_path),mode='rb') as f:
        result = f.read()
        # print(result.decode('utf-8'))

    model = json.loads(result)['data']

    for each in model['lists']:
        print(each['SongName'])


if __name__ == '__main__':
    main()