import requests
from bs4 import BeautifulSoup


def get_chinese(word):
    str_words_list = ''
    
    try:
        # 利用GET获取输入单词的网页信息
        r = requests.get(url='http://dict.youdao.com/w/%s/#keyfrom=dict2.top' % word)
        # 利用BeautifulSoup将获取到的文本解析成HTML
        soup = BeautifulSoup(r.text, "lxml")
        # 获取字典的标签内容
        s = soup.find(class_='trans-container')('ul')[0]('li')
        # 输出字典的具体内容
        for item in s:
            if item.text:
                str_words_list += word + '\n' + item.text
    
    except Exception:
        print()
        str_words_list += '\n' + "Sorry, there is a error! We can't find the word '{}'".format(
            word) + '\n' + '=' * 40
    return str_words_list


if __name__ == '__main__':
    print(get_chinese('apple'))
