from .models import PageVisit
import platform

class PageVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Get the operating system name
        os_name = platform.system()
        # Get the version of the operating system
        os_version = platform.version()
        # Get the machine type (e.g., 'x86_64')
        machine_type = platform.machine()
        # Get the processor type
        processor_type = platform.processor()
        # Get the network hostname
        hostname = platform.node()
        # Get the Python version
        python_version = platform.python_version()
        # Get the architecture (e.g., 32-bit or 64-bit)
        architecture = platform.architecture()
        # Get the libc version (Linux only)
        libc_version = platform.libc_ver()
        # Get the system's release version
        release_version = platform.release()
        System_info = {'Operating System': {os_name}, ' OS Version:':{os_version}, 'Machine Type:': {machine_type}, 'Processor Type': {processor_type}, 'Hostname':{hostname}, 'Python Version':{python_version}, 'Architecture0':{architecture[0]},' Architecture0':{architecture[1]},'Release Version': {release_version}}
        page_visit, created = PageVisit.objects.get_or_create(
                page_url=request.path,
                System_info = System_info,
            )
        # Increment the visit count
        page_visit.visit_count += 1
        page_visit.save()

        return response
