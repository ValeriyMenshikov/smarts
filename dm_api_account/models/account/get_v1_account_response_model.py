from jsonmodels.models import Base
from jsonmodels.fields import StringField, IntField, FloatField, EmbeddedField, ListField, BoolField, DateField


class PagingSettings(Base):
    posts_per_page = IntField(name='postsPerPage')
    comments_per_page = IntField(name='commentsPerPage')
    topics_per_page = IntField(name='topicsPerPage')
    messages_per_page = IntField(name='messagesPerPage')
    entities_per_page = IntField(name='entitiesPerPage')


class UserSettings(Base):
    color_schema = StringField(name='colorSchema')  # asd
    nanny_greetings_message = StringField(name='nannyGreetingsMessage')
    paging = EmbeddedField(PagingSettings)


class InfoDbText(Base):
    value = StringField()
    parse_mode = StringField(name='parseMode')  # asd


class Rating(Base):
    enabled = BoolField()
    quality = IntField()
    quantity = IntField()


class UserDetails(Base):
    login = StringField()
    roles = ListField()
    medium_picture_url = StringField(name='mediumPictureUrl')
    small_picture_url = StringField(name='smallPictureUrl')
    status = StringField()
    rating = EmbeddedField(Rating)
    online = DateField()
    name = StringField()
    location = StringField()
    registration = DateField()
    icq = StringField()
    skype = StringField()
    original_picture_url = StringField(name='originalPictureUrl')
    info = EmbeddedField(InfoDbText)
    settings = EmbeddedField(UserSettings)


class UserDetailsEnvelopeResponseModel(Base):
    resource = EmbeddedField(UserDetails)
    metadata = StringField()
