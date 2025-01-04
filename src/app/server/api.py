from config.config import Settings
from domain.errors.errors import (
    BaseError,
)
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from server.error import (  # エラーラッパーと処理をインポート
    HTTPErrorWrapper,
    handle_error,
)
from server.route.health_route import router as health_router
from server.route.v1.route import router as v1_router


class APIApplication:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.app = FastAPI(
            title=self.settings.app.title, version=self.settings.app.version
        )
        self._add_routes()
        self._add_exception_handlers()

    # ルーティングの登録
    def _add_routes(self) -> None:
        self.app.include_router(health_router)
        self.app.include_router(v1_router)

    # エラーハンドラの登録
    def _add_exception_handlers(self) -> None:
        @self.app.exception_handler(BaseError)
        async def base_error_handler(request: Request, exc: BaseError):  # noqa: ANN202, ARG001
            try:
                handle_error(exc)
            except HTTPErrorWrapper as wrapped_exc:
                return JSONResponse(
                    status_code=wrapped_exc.status_code,
                    content=wrapped_exc.detail,
                )

    def get_app(self) -> FastAPI:
        return self.app
