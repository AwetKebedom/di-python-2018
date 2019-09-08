class WebView:
    def __init__(self, name, content):
        self.name    = name
        self.content = content


class Website:  # the sites that we are creating
    def __init__(self, name, url):
        self.name    = name
        self.url     = url
        self.routes  = {}

    def add_page(self, page_obj, uri):
        self.routes[uri] = page_obj

    def request(self, uri):
        if uri not in self.routes:
            return False
        return self.routes[uri]


class SearchEngine:
    def __init__(self):
        self.sites = {}
        self.sites_name = {}



    def get

