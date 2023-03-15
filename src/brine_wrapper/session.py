import requests


class Session(requests.Session):
    def __init__(self, url_base=None, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.url_base = url_base

    def request(self, method, url, **kwargs):
        modified_url = self.url_base + url
        response = super(Session, self).request(method, modified_url, **kwargs)
        response.raise_for_status()
        return response
    
