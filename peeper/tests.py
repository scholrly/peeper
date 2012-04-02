from nose.tools import eq_
from peeper.find_image_urls import find_image_urls

def test_empty():
  eq_(find_image_urls(html=""), [])

def test_img_without_src():
  eq_(find_image_urls(html='<img title="An owl' \
    ' peering out from a hole in a brick wall.">'), [])

def test_one():
  eq_(find_image_urls(html='<img src="a">'), ['a'])

def test_two_duplicate_removed():
  eq_(find_image_urls(html='<img src="a" title="x"/><img src="a" width=24>'), ['a'])

def test_two_duplicate():
  eq_(find_image_urls(html='<img src="a" title="x"/><img src="a" width=24>',
    duplicate=True), ['a', 'a'])

def test_one_with_url():
  eq_(find_image_urls(url='http://scholr.ly/authors/index.html',
    html='<img src="erdos.jpg">'),
    ['http://scholr.ly/authors/erdos.jpg'])

def test_one_with_base():
  eq_(find_image_urls(
    html='<base href="https://localhost/lolcats/best.html"/>' \
         '<img src="invisible_sandwich.gif">'),
    ['https://localhost/lolcats/invisible_sandwich.gif'])

def test_one_with_base_and_url():
  eq_(find_image_urls(
    url='https://localhost/lolcats/index.html',
    html='<base href="best/index.html"/>' \
         '<img src="im-in-ur-computer-stealing-ur-megahurtz.png">'),
    ['https://localhost/lolcats/best/im-in-ur-computer-stealing-ur-megahurtz.png'])

def test_base_without_href():
  eq_(find_image_urls(html='<base target="_blank"><img src="xyzzy">'), ['xyzzy'])
