from rest_framework.pagination import LimitOffsetPagination


class PlaceSetPagination(LimitOffsetPagination):
    default_limit = 6
    max_limit = 10
