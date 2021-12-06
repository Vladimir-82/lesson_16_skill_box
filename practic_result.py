# -*- coding: utf-8 -*-

import cv2
import bs4
import peewee
import requests

# Шаг 1 - выкачиваем картинки с 'http://bern.by/about/leadership/'

html = requests.get('http://bern.by/about/leadership/').text
# print(html)

soup = bs4.BeautifulSoup(html, 'html.parser')
all_images = soup.find_all('img')
# print(all_images)
# print('\n'.join(str(t) for t in all_images if 'title' in str(t)))

downloaded_files = []

for tag in all_images:
    if 'title' in str(tag):
        url = tag.get('src')
        # print(url)
        filename = str(url).split('/')[-1]
        filename_full = f'photos/{filename}'
        downloaded_files.append(str(filename))
        with open(filename_full, 'wb') as f:
            f.write(requests.get('http://www.bern.by' + url).content)

def draw_horns(image, x, y, w, h):

    # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), thickness=3)
    cv2.line(image, (x + w // 2 - w // 5, y), (x + w // 2 - w // 5, y - h // 4), (0, 0, 255), 8)
    cv2.line(image, (x + w // 2 + w // 5, y), (x + w // 2 + w // 5, y - h // 4), (0, 0, 255), 8)
    cv2.imshow('res', image)
    cv2.waitKey(500)


database = peewee.SqliteDatabase("Horns.db")


class Horns(peewee.Model):
    name = peewee.CharField()

    class Meta:
        database = database


Horns.create_table()

# Шаг 2 - распознаем лица

for image_path in downloaded_files:

    img = cv2.imread('photos/' + image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('videos/faces.xml')
    result = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Шаг 3 - рисовка рогов

    for (x, y, w, h) in result:
        draw_horns(img, x, y, w, h)


# Шаг 4 - пишем в файл и базу

    horns_image_path = image_path.replace('photos', 'photos_results')
    cv2.imwrite(horns_image_path, img)
    Horns.create(name=horns_image_path)

print(list(Horns.select()))

