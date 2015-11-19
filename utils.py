import urllib2, google, bs4, re, math

def parse_names(text):
    list_of_names = re.findall('[A-Z][a-z]+ [A-Z][a-z]+', text)
    return list_of_names

def top_names(who_query):
    pages = 16
    print who_query
    urls = google.search(who_query,num=pages,start=0,stop=pages)
    result=[]
    for thing in urls:
        result.append(thing)
    names={}
    counter = 0
    for thing in result:
        if counter < pages:
            try:
                u = urllib2.urlopen(thing)
                page = u.read()
                soup = bs4.BeautifulSoup(page,'html')
                raw = soup.get_text()
                possibles = parse_names(raw)
                power = int(math.log(pages, 2))-int(math.log(counter+1, 2))+1
                for name in possibles:
                    if name not in names:
                        names[name] = power
                    else:
                        names[name]+=power
            except:
                pass
            counter+=1
    i = 0
    top={}
    while i < 1:
        most_mentioned=None
        mentions = 0
        for name in names:
            if names[name] > mentions:
                most_mentioned = name
                mentions = names[name]
        names[most_mentioned]=0
        top[most_mentioned]=mentions
        i+=1
    print top

top_names("who is Champ?")
