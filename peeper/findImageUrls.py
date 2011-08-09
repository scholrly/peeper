import argparse, mechanize
from lxml import etree
from urlparse import urljoin

def findImageUrls(url=None, html=None, duplicate=False, alphabetical=False):
  assert url is not None or html is not None
  if html == "": return []
  urls = __findImageUrls(url, html)
  if not duplicate: urls = uniquify(urls)
  if alphabetical: urls.sort()
  return urls

def uniquify(seq):
  seen = set()
  return [x for x in seq if x not in seen and not seen.add(x)]

def __findImageUrls(url, html):
  tree = __tree(url, html)
  base = __base(tree, url)
  return [
    urljoin(base, x.attrib['src'])
    for x in tree.xpath('//img')
    if 'src' in x.attrib ]

def __tree(url, html):
  parser = etree.HTMLParser()
  if html is None:
    response = mechanize.Browser().open(url)
    return etree.parse(source=response, parser=parser, base_url=url)
  else:
    return etree.fromstring(text=html, parser=parser, base_url=url)

def __base(tree, url):
  for base in tree.xpath('//base'):
    if 'href' in base.attrib:
      return __urljoin(base.attrib['href'], url)
  return url

def __urljoin(href, url=None):
  if url is None: return href
  else: return urljoin(url, href)

def __findImageUrlsArgParser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-u', '--url', type=str)
  parser.add_argument('-d', '--duplicate', action='store_true')
  parser.add_argument('-a', '--alphabetical', action='store_true')
  parser.add_argument('-x', '--html')
  return parser

if __name__ == '__main__':
  args = __findImageUrlsArgParser().parse_args()
  print '\n'.join(findImageUrls(**vars(args)))
