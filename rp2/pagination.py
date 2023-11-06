from typing import Any

from django.core.paginator import Paginator

from .settings import (
    DEFAULT_PAGINATION_PAGE,
    DEFAULT_PAGINATION_PAGE_SIZE,
    MAX_PAGE_SIZE,
)


def paginate(
    object_list: Any,
    page: (int | None) = None,
    page_size: (int | None) = None,
) -> Any:

    if page is None:
        page = DEFAULT_PAGINATION_PAGE

    if page_size is None:
        page_size = DEFAULT_PAGINATION_PAGE_SIZE

    if page_size > MAX_PAGE_SIZE:
        page_size = MAX_PAGE_SIZE

    paginator = Paginator(object_list, page_size)
    paginated_query_set = paginator.get_page(page)
    return paginated_query_set
