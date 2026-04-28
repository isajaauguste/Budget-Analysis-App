from typing import Annotated, Literal, Optional

from fastapi import Query

from schemas import ListParams


def get_list_params(
    sort_by: Annotated[
        Optional[Literal["date", "amount"]],
        Query(),
    ] = None,
    sort_order: Annotated[Literal["asc", "desc"], Query()] = "asc",
    limit: Annotated[int, Query(gt=0, le=100)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> ListParams:
    return ListParams(
        sort_by=sort_by,
        sort_order=sort_order,
        limit=limit,
        offset=offset,
    )