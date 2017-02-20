# -*- coding:utf-8 -*-
import codecs
import csv
import re

import jieba.analyse
import matplotlib.pyplot as plt
import requests
from scipy.misc import imread
from wordcloud import WordCloud

__author__ = 'liuzhijun'

cookies = {
    "ALF": "1489741225",
    "SCF": "AlE23pvO55c-tjcvq_9U-BwEK7OzuLdN6XnI-Bg1vQPlNcm7Atblq34rFR1PIei5Sp-jX1oikqxt7eLYtw_ZJ4c.",
    "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9W5eUgwfgjhvYJraoCA.ZDn.5JpX5KMhUgL.Foe71K2NeozpSh-2dJLoIEBLxKBLBonL1h5LxKqL1-BL1h5LxKML1K.LB.-LxK.L1hML12et",
    "SUB": "_2A251rjzFDeRxGeVO4lMW8izNzzmIHXVXUUSNrDV6PUNbktBeLRnMkW1ZGDRFqMInP5uvmMQRhehPb0ySLA..",
    "SUHB": "0BLYeDP6-UgtFq",
    "_T_WM": "954dbf366abd053f9c7793df6c4fba79",
    "SSOLoginState": "1487555733",
}


def fetch_weibo():
    api = "http://m.weibo.cn/index/my?format=cards&page=%s"
    for i in range(1, 102):
        response = requests.get(url=api % i, cookies=cookies)
        data = response.json()[0]
        groups = data.get("card_group") or []
        for group in groups:
            text = group.get("mblog").get("text")
            text = text.encode("utf-8")

            def cleanring(content):
                """
                去掉无用字符
                """
                pattern = "<a .*?/a>|<i .*?/i>|转发微博|//:|Repost|，|？|。|、|分享图片"
                content = re.sub(pattern, "", content)
                return content

            text = cleanring(text).strip()
            if text:
                yield text


def write_csv(texts):
    with codecs.open('./weibo.csv', 'w') as f:
        writer = csv.DictWriter(f, fieldnames=["text"])
        writer.writeheader()
        for text in texts:
            writer.writerow({"text": text})


def read_csv():
    with codecs.open('./weibo.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row['text']


def word_segment(texts):
    jieba.analyse.set_stop_words("./stopwords.txt")
    for text in texts:
        tags = jieba.analyse.extract_tags(text, topK=20)
        yield " ".join(tags)


def generate_img(texts):
    data = " ".join(text for text in texts)

    mask_img = imread('./heart-mask.jpg', flatten=True)
    wordcloud = WordCloud(
        font_path='msyh.ttc',
        background_color='white',
        mask=mask_img
    ).generate(data)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.savefig('./heart.jpg', dpi=600)


if __name__ == '__main__':
    texts = fetch_weibo()
    write_csv(texts)
    generate_img(word_segment(read_csv()))
