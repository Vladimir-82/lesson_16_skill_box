from html.parser import HTMLParser
import requests

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'Encounted a start tag: <{tag}>')

    def handle_endtag(self, tag):
        print(f'Encounted a end tag: <{tag}>')

    def handle_data(self, data) -> None:
        print(f'Encounted a end tag: <{data}>')


response = requests.get('http://bern.by').text
parser = MyHTMLParser()
parser.feed(response)


