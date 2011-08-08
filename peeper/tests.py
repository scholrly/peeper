from nose.tools import eq_
from peeper.findImageUrls import findImageUrls

def test_empty():
  eq_(findImageUrls(html=""), [])

def test_img_without_src():
  eq_(findImageUrls(html='<img title="An owl' \
    ' peering out from a hole in a brick wall.">'), [])

def test_one():
  eq_(findImageUrls(html='<img src="a">'), ['a'])

def test_one_with_url():
  eq_(findImageUrls(url='http://scholr.ly/authors/index.html',
    html='<img src="erdos.jpg">'),
    ['http://scholr.ly/authors/erdos.jpg'])

def test_one_with_base():
  eq_(findImageUrls(
    html='<base href="https://localhost/lolcats/best.html"/>' \
         '<img src="invisible_sandwich.gif">'),
    ['https://localhost/lolcats/invisible_sandwich.gif'])
