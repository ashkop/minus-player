import urllib2, urllib
import json


class ErrorHandler(urllib2.HTTPDefaultErrorHandler):

    def http_error_default(self, request, fp, code, msg, headers):
        body =  fp.read()
        if body:
            try:
                response = json.loads(body)
                error_desc = response['error_description']
            except ValueError:
                pass
            except KeyError:
                pass
            else:
                raise Exception(error_desc)
        super(ErrorHandler, self).http_error_default(request, fp, code, msg, headers)


    
class RestTransport(object):

    api_domain = ''

    def __init__(self):
        opener = urllib2.build_opener(ErrorHandler())
        urllib2.install_opener(opener)

    def generate_request(self, method, url, params):

        if method not in ['GET', 'POST']:
            raise Exception('Unknown request method')
        if hasattr(self, 'auth') and self.auth:
            params['bearer_token'] = self.auth.access_token
        url_params = urllib.urlencode(params)
        if method == 'GET':
            if url_params:
                request = urllib2.Request(self.api_domain + url + '?' +url_params)
            else:
                request = urllib2.Request(self.api_domain + url)
        else:
            request = urllib2.Request(self.api_domain + url, url_params)





        return request

    def get(self, url, params):
        request = self.generate_request('GET', url, params)
        response = urllib2.urlopen(request)
        return json.loads(response.read())

    def post(self, url, params):
        request = self.generate_request('POST', url, params)
        response = urllib2.urlopen(request)
        return json.loads(response.read())


MinusTransport = RestTransport()
MinusTransport.api_domain = 'https://minus.com/'
