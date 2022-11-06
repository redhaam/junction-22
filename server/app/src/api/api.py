from src.api.endpoints import login, users, items, inventors, experts, innovation_supports, foundation_admins, projects, fields, expert_field, project_field, feedbacks, expert_project, evaluations
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.core.config import settings

api_router = FastAPI()



@api_router.get("/")
def read_root():
    return {"message": "Welcome !"}







# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    api_router.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(inventors.router, prefix="/inventors", tags=["inventors"])
api_router.include_router(experts.router, prefix="/experts", tags=["experts"])
api_router.include_router(innovation_supports.router, prefix="/innovation_supports", tags=["innovation_supports"])
api_router.include_router(foundation_admins.router, prefix="/foundation_admins", tags=["foundation_admins"])
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(fields.router, prefix="/fields", tags=["fields"])
api_router.include_router(expert_field.router, prefix="/expert_field", tags=["expert_field"])
api_router.include_router(project_field.router, prefix="/project_field", tags=["project_field"])
api_router.include_router(feedbacks.router, prefix="/feedbacks", tags=["feedbacks"])
api_router.include_router(expert_project.router, prefix="/expert_project", tags=["expert_project"])
api_router.include_router(evaluations.router, prefix="/evaluations", tags=["evaluations"])