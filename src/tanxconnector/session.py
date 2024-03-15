import requests
from typing import Callable, Union, Optional
from .typings import LoginResponse


class Session(requests.Session):
    def __init__(self, refresh_tokens: Callable, url_base=None, *args, **kwargs):
        super(Session, self).__init__(*args, **kwargs)
        self.url_base = url_base
        self.refresh_tokens = refresh_tokens

    def request(self, method, url, **kwargs):
        modified_url = self.url_base + url
        response = super(Session, self).request(method, modified_url, **kwargs)

        if response.status_code == 401 and self.headers.get('Authorization') and response.json().get('payload').get('token_type') == 'access':
            del self.headers['Authorization']
            res = self.refresh_tokens()

            if res:
                self.headers.update(
                    {'Authorization': f"JWT {res['payload']['access']}"})
                response.headers.update(
                    {'Authorization': f"JWT {res['payload']['access']}"})

            return super(Session, self).request(method, modified_url, **kwargs)

        response.raise_for_status()
        return response
