import json
import xml.etree.ElementTree as ET


def get_top_words(text, min_len=6, words_qty=10):
    words = set(text.split())
    result = [x for x in words if len(x) > min_len]
    result.sort(key=lambda x: len(x))
    return result[:-(words_qty + 1):-1]


def parse_json(filename, min_len=6, words_qty=10):
    with open(filename, encoding='utf-8') as file:
        file = json.load(file)
        items = file['rss']['channel']['items']
        text = ''
        for item in items:
            text += item['description']
    return get_top_words(text, min_len, words_qty)


def parse_xml(filename, min_len=6, words_qty=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(filename, parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    text = ''
    for item in items:
        text += item.find('description').text
    return get_top_words(text, min_len, words_qty)


print('Вывод длинных слов из "newsafr.json":')
print(*parse_json('newsafr.json'), sep='\n')
print('\nВывод длинных слов из "newsafr.xml":')
print(*parse_xml('newsafr.xml'), sep='\n')
