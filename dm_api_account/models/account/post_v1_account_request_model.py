import dataclasses
import json
from jsonmodels.models import Base
from jsonmodels.fields import StringField


class RegistrationRequestModel(Base):
    login = StringField()
    email = StringField()
    password = StringField()


@dataclasses.dataclass
class RegistrationRequestModel1:
    login: str
    email: str
    password: str = None


print(json.dumps(dataclasses.asdict(RegistrationRequestModel1(login='1', email='2'))))
