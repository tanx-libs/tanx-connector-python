import requests
from typing import Callable


class Session(requests.Session):
    def __init__(self, retry_login: Callable[[], dict or None], url_base=None, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.url_base = url_base
        self.retry_login = retry_login

    def request(self, method, url, **kwargs):
        modified_url = self.url_base + url
        response = super(Session, self).request(method, modified_url, **kwargs)

        if response.status_code == 401 and self.headers.get('Authorization'):
            del self.headers['Authorization']
            login = self.retry_login()
            self.headers.update(
                {'Authorization': f"JWT {login['token']['access']}"})
            response.request.headers.update(
                {'Authorization': f"JWT {login['token']['access']}"})
            return self.send(response.request, verify=False)

        response.raise_for_status()
        return response
