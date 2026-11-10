from fastapi import FastAPI

app = FastAPI(title="LikeLion Backend Study")


@app.get("/", tags=["root"])
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    return {"status": "ok", "project_name": "2026 Fall Backend"}


@app.patch("/health", tags=["health"])
async def health_patch() -> dict[str, str]:
    return {"http_method": "patch method", "status": "ok"}