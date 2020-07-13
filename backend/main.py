from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware

from app.api import router as api_router, audit_handler


app = FastAPI()
app.add_middleware(GZipMiddleware)
app.include_router(api_router, dependencies=[Depends(audit_handler)])

