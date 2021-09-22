import argparse
import json


def main(f):
    # with open('2fa-basic.json', 'r') as f:
    data = json.loads(f.read())
    for ins in data:
        if ins['type'] == 'output':
            print(ins['value'])
        else:
            input(ins["value"])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replays logs as if they happened')
    parser.add_argument('file', help="file with replay data")
    args = parser.parse_args()
    f = open(args.file, 'r')
    main(f)
    f.close()
