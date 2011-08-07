import argparse, mechanize
from lxml import etree
from twisted.python.util import uniquify

def findImageUrls(url, duplicate=False, alphabetical=False):
  browser = mechanize.Browser()
  response = browser.open(url)
  parser = etree.HTMLParser()
  tree = etree.parse(response, parser)
  images = tree.xpath('//img')
  imagePaths = map(lambda x: x.attrib['src'], images)
  if not duplicate: imagePaths = uniquify(imagePaths)
  if alphabetical: imagePaths.sort()
  return imagePaths

def findImageUrlsArgParser():
  parser = argparse.ArgumentParser()
  parser.add_argument('url', type=str)
  parser.add_argument('-d', '--duplicate', action='store_true')
  parser.add_argument('-a', '--alphabetical', action='store_true')
  return parser

if __name__ == '__main__':
  args = findImageUrlsArgParser().parse_args()
  print '\n'.join(findImageUrls(**vars(args)))
