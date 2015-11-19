import urllib2, google, bs4, re, math

def parse_names(text):
    more = True
    list_of_names = []
    while(more):
        name = re.match('[A-Z][a-z]+ [A-Z][a-z]+', text)
        re.sub('[A-Z][a-z]{1,15} [A-Z][a-z]{1,15} ','name',text)
        if(name == None):
            more = False
        else:
            list_of_names.append(name)
            print list_of_names[0]
    return list_of_names

def top_names(who_query):
    pages = 10
    urls = google.search(who_query,num=pages,start=0,stop=pages)
    result=[]
    for thing in urls:
        result.append(thing)
    print result
    names={}
    print result
    counter = 0
    for thing in result:
        print counter
        u = urllib2.urlopen(thing)
        page = u.read()
        soup = bs4.BeautifulSoup(page,'html')
        raw = soup.get_text()
        possibles = parse_names(raw)
        power = math.log(pages, 2)-math.log(counter+1, 2)
        counter+=1
        for name in possibles:
            if name not in names:
                names[name] = power
            else:
                names[name]+=power
    print names

top_names("who is president")
