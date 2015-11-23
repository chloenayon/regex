import urllib2, google, bs4, re, math

def parse_names_who(text):
    list_of_names = re.findall('[A-Z][a-z]+ [A-Z][a-z]+', text)
    print list_of_names
    print #"x^x"
    return list_of_names

def top_names_who(who_query):
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
                soup = bs4.BeautifulSoup(page,"html.parser")
                raw = soup.get_text()
                print "2"
                possibles = parse_names_who(raw)
                print "2"
                power = int(math.log(pages, 2))-int(math.log(counter+1, 2))+1
                for name in possibles:
                    if name not in names:
                        names[name] = power
                    else:
                        names[name]+=power
            except:
                print "error loading page"
            print counter
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
        print most_mentioned
        return most_mentioned
    #print top
    return top

##top_names("who is Champ?")

def top_answers(q):
    if re.search("When|when", q):
        return top_dates_when(q)
    return top_names_who(q)

def parse_names_when(text):
    list_of_names = re.findall(' [1-9]{4} ', text)
    print list_of_names
    print #"x^x"
    return list_of_names

def top_dates_when(who_query):
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
                soup = bs4.BeautifulSoup(page,"html.parser")
                raw = soup.get_text()
                print "2"
                possibles = parse_names_when(raw)
                print "2"
                power = int(math.log(pages, 2))-int(math.log(counter+1, 2))+1
                for name in possibles:
                    if name not in names:
                        names[name] = power
                    else:
                        names[name]+=power
            except:
                print "error loading page"
            print counter
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
        print most_mentioned
        return most_mentioned
    print top
