from config.config import Settings
from fastapi import FastAPI
from server.route.health_route import router as health_router
from server.route.v1.route import router as v1_router


class APIApplication:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.app = FastAPI(
            title=self.settings.app.title, version=self.settings.app.version
        )
        self._add_routes()

    def _add_routes(self) -> None:
        self.app.include_router(health_router)
        self.app.include_router(v1_router)

    def get_app(self) -> FastAPI:
        return self.app
