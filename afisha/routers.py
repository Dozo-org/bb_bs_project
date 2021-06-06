from rest_framework.routers import Route, DefaultRouter


class CustomRouter(DefaultRouter):
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create',
                'delete': 'destroy',
                'put': 'update',
                'patch': 'partial_update'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
    ]
