from fastapi import FastAPI, Request
from app.core.config import APP_TITLE, APP_VERSION, APP_DESCRIPTION, ROUTER_PREFIX, APP_DEBUG

# Set docs URL conditionally
swagger_url = f"/{ROUTER_PREFIX}/docs" if APP_DEBUG else "/docs"

# Initialize FastAPI app
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    description=APP_DESCRIPTION,
    docs_url=swagger_url,  # Set custom docs URL or disable
    redoc_url=None,        # (optional) disable ReDoc if you want
    openapi_url=f"/{ROUTER_PREFIX}/openapi.json" if APP_DEBUG else None  # OpenAPI path if debug
)

@app.get('/', tags=["Default"])
async def read_root(request: Request):
    return {
        "status_code": 200,
        "message": f"Welcome to {APP_TITLE}! Go to docs at {request.base_url}{ROUTER_PREFIX}/docs",
        "result": None
    }
