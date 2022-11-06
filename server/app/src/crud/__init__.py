from .crud_item import item
from .crud_user import user
from .crud_inventor import inventor
from .crud_expert import expert
from .crud_innovation_support import innovation_support
from .crud_foundation_admin import foundation_admin
from .crud_project import project
from .crud_field import field
from .crud_expert_field import expert_field
from .crud_project_field import project_field
from .crud_feedback import feedback
from .crud_expert_project import expert_project
from .crud_evaluation import evaluation
# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate

# item = CRUDBase[Item, ItemCreate, ItemUpdate](Item)