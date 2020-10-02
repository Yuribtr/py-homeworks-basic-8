import json
import xml.etree.ElementTree as ET
# from time import perf_counter
#
# start_time = perf_counter()


def get_top_words(words, words_qty=10):
    """
    This function returns most used words in list
    """
    result = {}
    # join all words in dict, where word is a key, and count is a value
    for word in words:
        result[word] = result.setdefault(word, 0) + 1
    # making two-dimensional array from dict
    result = [[x, y] for x, y in result.items()]
    # sorting in reverse order by second element (prev value) and cut first 10 elements
    result = sorted(result, key=lambda x: x[1], reverse=True)[:(words_qty + 1)]
    # comment out foll line if you want to see word's frequency of use in numbers
    result = [x[0] for x in result]
    return result


def get_longest_words(words, min_len=6, words_qty=10):
    """
    This function returns most longest words in list
    """
    result = [x for x in words if len(x) > min_len]
    result.sort(key=lambda x: len(x))
    return result[:-(words_qty + 1):-1]


def parse_json(filename, min_len=6, words_qty=10):
    with open(filename, encoding='utf-8') as file:
        file = json.load(file)
        items = file['rss']['channel']['items']
        text = []
        for item in items:
            text += [x for x in item['description'].split() if len(x) > min_len]
    return get_top_words(text, words_qty)


def parse_xml(filename, min_len=6, words_qty=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(filename, parser)
    root = tree.getroot()
    items = root.findall('channel/item')
    text = []
    for item in items:
        text += [x for x in item.find('description').text.split() if len(x) > min_len]
    return get_top_words(text, words_qty)


print('Вывод наиболее часто встречающихся слов из "newsafr.json":')
print(*parse_json('newsafr.json'), sep='\n')
print('\nВывод наиболее часто встречающихся слов из "newsafr.xml":')
print(*parse_xml('newsafr.xml'), sep='\n')

# end_time = perf_counter()
# print(f"Time taken: {(end_time - start_time) * 1000000} mkS")
