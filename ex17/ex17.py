# vim: set fileencoding=utf_8 :
'''
Decode A Web Page    
This is the first 4-chili exercise of this blog! We’ll see what people think, and decide whether or not to continue with 4-chili exercises in the future.

Exercise 17 (and Solution)

Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

### some sites I used to reference:
http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/


'''
import requests
import bs4

if __name__ == "__main__":
    url = 'http://nytimes.com'
    homepage = requests.get(url)
    homepage_html = homepage.text
    soup = bs4.BeautifulSoup(homepage_html, "html.parser")

### Get this error
## AttributeError: 'NoneType' object has no attribute 'text'

    articles1 = []
    for h in soup.find_all(class_="story-heading"):
        try:
            a = h.find('a').text.lstrip()
            print a
            articles1.append(a)
        except AttributeError:
            pass
    print len(articles1)

#    print "---------------------- Break this apart -----------------------"
#    print "----------------------  -----------------------"

## Was getting some None types in here
#    articles = []
#    for h in soup.find_all(class_="story-heading"):
#            a = h.find('a')
#            print a
#            articles.append(a)
#    print len(articles)
