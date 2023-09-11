from .models import PageVisit

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        page_visit, created = PageVisit.objects.get_or_create(
                page_url=request.path
            )
        
        # Increment the visit count
        page_visit.visit_count += 1
        page_visit.save()

        return response
