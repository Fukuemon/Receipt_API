import logging

from domain.errors.errors import (
    BaseError,
    InternalServerError,
    NotFoundError,
    ValidationError,
)
from fastapi import HTTPException

logger = logging.getLogger(__name__)


class HTTPErrorWrapper(HTTPException):
    """FastAPI依存のエラーラッパー"""

    def __init__(self, base_error: BaseError, status_code: int) -> None:
        super().__init__(
            status_code=status_code,
            detail={
                "msg": base_error.msg,
                "description": base_error.description,
            },
        )


def handle_error(e: BaseError) -> None:
    error_mapping: dict[type[BaseError], int] = {
        ValidationError: 400,
        NotFoundError: 404,
        InternalServerError: 500,
    }

    status_code = error_mapping.get(type(e), 500)

    # 500エラーの場合はログ出力
    if status_code == error_mapping[InternalServerError]:
        logger.error("%s: %s", e.msg, e.description)

    raise HTTPErrorWrapper(e, status_code)
