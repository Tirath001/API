from rest_framework.pagination import PageNumberPagination

class JobListPagination(PageNumberPagination):
    page_size = 3 
    page_size_query_param = 3
    max_page_size = 100