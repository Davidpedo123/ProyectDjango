class SubDomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2:
            request.subdomain = '.'.join(host_parts[:-2])
        else:
            request.subdomain = None
        response = self.get_response(request)
        return response
