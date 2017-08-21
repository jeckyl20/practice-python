# vim: set fileencoding=utf_8 :
'''
Decode A Web Page Two    
Exercise 19 (and Solution)

Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.
'''
import requests
import bs4

import re
import urlparse

def print_article(site):
## Lets get the heading first:
    print site.h1.string
## Now print the text of the page:
    for i in site.find_all('p'):
        print i.text
#        p1 += i.text
    print "\n" + "="*40 + "\n"

def give_me_soup(url):
    homepage = requests.get(url)
    homepage_html = homepage.text
    soup = bs4.BeautifulSoup(homepage_html, "html.parser")
    return soup


if __name__ == "__main__":
#    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    url = 'http://www.tldp.org/LDP/nag2/x-087-2-intro.history.html'
#    homepage = requests.get(url)
#    homepage_html = homepage.text
#    soup = bs4.BeautifulSoup(homepage_html, "html.parser")

### look for p (paragraph) tag and inside that data-reactid="<number" tag. 233 through 316
#    for h in soup.find_all('p'):
#        print h.find('data-reactid')

#    for h in soup.find_all('p'):
#        print h

#    print soup.p ## returns <p data-reactid="225">‘How does it feel to be America’s premier blow-job queen?”</p>
#    print soup.p['data-reactid'] ## returns 225
#    print soup.p.get_text() ## returns ‘How does it feel to be America’s premier blow-job queen?”

### get count of p tags, the second line will print that number tag
#    print len(soup.find_all('p'))
#    print soup.find_all('p')[2].text

##### Worked to print all the paragraph tags on the Monica Lewinsky article, but there were not multiple pages
#    for i in soup.find_all('p'):
#        print i.text

##### Try another site to get text from
#    p1, p2 = "", ""
#    print type(p1)
#    print type(p2)

    soup = give_me_soup(url)
    print_article(soup)

#    next_url = soup.find('link', rel='NEXT').get('href')
    next_url = urlparse.urljoin(url, soup.find('link', rel='NEXT').get('href'))
#    print next_url
    soup2 = give_me_soup(next_url)

    print_article(soup2)
    
    ## Now lets go to the next page:
'''    
#    next_url = soup.div['class']#="NAVFOOTER"]
#    print next_url
    #print next_url.text
    next_url = soup.find('link', rel='NEXT')
#    print next_url.get('href')
    next_url_text = next_url.get('href')
    print next_url_text
#    test = urlparse.urljoin(url, next_url.get('href')
    #print test
    test2 = urlparse.urlsplit(url)
    print test2
    test = urlparse.urljoin(url, next_url_text)
    print test
'''
    
