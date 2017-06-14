from pyramid.view import view_config


def scrape(term): # Pulls the data from wikipedia and returns the data
    from bs4 import BeautifulSoup
    import urllib2

    # NoneType term processing
    if not term:
        return ["",""]

    page = "https://en.wikipedia.org/wiki/" + '_'.join(term.split(' '))

    try:
        target = urllib2.urlopen(page).read()
    except:    # Handles exception when ivalid term is entered in the search bar
        return [term,"Invalid Search Term"]

    soup = BeautifulSoup(target, 'lxml') # Scrap data out xml

    no_toc = [term,"Requested search term has no table of contents"]

    try:
        payload = soup.find("div", {"class": "toc"})
        if not payload:
            return no_toc
    except:
        return no_toc

    term = term.upper()
    return [term, payload]

	
@view_config(route_name='home', renderer='templates/wikiapp.jinja2')
def main_view(request):

    result = scrape(request.GET.get('query'))

    return {'query':result[0],'result':result[1]}
