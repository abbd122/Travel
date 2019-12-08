import json


def handle_json(path):
  with open(path, 'r', encoding='utf-8') as f:
    ret = json.load(f)
  return ret


if __name__ == '__main__':
  handle_json('/home/wangzheng/project/Travel/static/mode/index.json')
