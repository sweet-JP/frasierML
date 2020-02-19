import re
import requests
import sys
import time
import HTMLParser

class Episode:
	def __init__(self):
		self.title = ''
		self.raw = ''
		self.script = []
		self.line = 0
	def feed(self, data, line):
		self.line = line
		self.parseScript(data)
	def parseScript(self, data):
		parser = HTMLParser.HTMLParser()
		self.raw = cleanhtml(parser.unescape(data))
		start = sys.maxint
		end = sys.maxint
		split = self.raw.splitlines()

		count = 0
		for i in split:
			if 'Transcript {' in i or 'Quotes & Scene Summary {' in i:
				start = min(start, count + 1)
				print("start @ ", start)
			if 'Legal Stuff' in i or 'Guest Appearances' in i:
				end = min(end, count - 1)
				print("end @ ", end)
			if 'Production Code:' in i:
				self.title = i.replace('Production Code: ', '').replace('.', ',')
			count += 1

		if start == sys.maxint or end == 0 or self.title == '':
			print("ERROR AT ", self.line, ": \n START: ", start, "\n END: ", end, "\n TITLE: ", self.title)
			sys.exit()

		split = split[start:end]
		for i in split:
			self.script.append(i.encode('ascii', 'ignore') + '\n')
			print(i)
	def getTitle(self):
		return self.title
	def getScript(self):
		return self.script

##CREDIT: https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

startline = 0
if (len(sys.argv) > 1):
	startline = max(startline, int(sys.argv[1]))

urllist = open('out/UrlList', 'r')
#urllist = open('out/TestUrlList', 'r')
urls = urllist.readlines()
urllist.close()

count = 0
for i in urls:
	print(count, startline)
	if (count >= startline):
		url = requests.get(i)
		text = url.text
		#time.sleep(0.5)
		ep = Episode()
		ep.feed(text, count)
		outstring = 'out/eps/' + ep.getTitle()
		out = open(outstring, 'w')
		out.truncate(0)
		out.writelines(str(line) for line in ep.getScript())
		out.close()
		del ep
	count += 1
