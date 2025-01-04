class BaseError(Exception):
    """汎用エラーの基底クラス"""

    def __init__(self, msg: str, description: str) -> None:
        self.msg = msg
        self.description = description
        super().__init__(msg)


class ValidationError(BaseError):
    """入力検証エラー"""

    def __init__(self, description: str) -> None:
        super().__init__(msg="Validation Error", description=description)


class NotFoundError(BaseError):
    """リソースが見つからないエラー"""

    def __init__(self, description: str) -> None:
        super().__init__(msg="Not Found Error", description=description)


class InternalServerError(BaseError):
    """内部サーバエラー"""

    def __init__(self, description: str) -> None:
        super().__init__(msg="Internal Server Error", description=description)
