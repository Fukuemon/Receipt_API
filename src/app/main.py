from config.config import Settings
from mangum import Mangum
from server.api import APIApplication

settings = Settings()

app = APIApplication(settings).get_app()

handler = Mangum(app)
