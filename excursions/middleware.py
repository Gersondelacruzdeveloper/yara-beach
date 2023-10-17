from .models import PageVisit

import logging

logger = logging.getLogger(__name__)

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        page_url = request.path
        try:
            page_visit, created = PageVisit.objects.get_or_create(page_url=page_url)
            page_visit.visit_count += 1
            page_visit.save()
        except Exception as e:
            logger.error(f"PageVisitMiddleware error: {e}")
        return response

