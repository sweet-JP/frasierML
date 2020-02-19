source = open('src/UrlList.html', 'r')
text = source.readlines()
source.close()

lines = []
for i in text:
	if "Season" in i and "Episode" in i:
		lines.append(i)

urls = []
for i in lines:
	temp = i
	start = i.find('kacl780')
	end = i.find('title=')
	temp = i[start-11:end-2]
	print(temp)
	urls.append(temp + "\n")

output = open('out/UrlList', 'w')
output.truncate(0)
output.writelines(urls)
output.close()