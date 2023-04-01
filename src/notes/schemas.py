from ninja import ModelSchema, Schema
from datetime import date
from .models import Note


__all__ = (
    'CategoryIn',
    'CategoryOut',
    'NoteIn',
    'NoteUpd',
    'NoteOut'
)


class CategoryIn(Schema):
    title: str
    description: str


class CategoryOut(Schema):
    id: int
    title: str
    description: str
    created: date
    updated: date


class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title',  'category']


class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'completed']


class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'category', 'created',
                        'updated', 'completed']