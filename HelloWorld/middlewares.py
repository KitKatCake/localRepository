from django.utils.deprecation import MiddlewareMixin


class MD1(MiddlewareMixin):
    def process_request(self, request):
        print("md1  process_request 方法。", id(request))

    def process_response(self, request, response):
        print("md1  process_response 方法！", id(request))
        return response
