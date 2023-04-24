from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):
        return Response(data)
