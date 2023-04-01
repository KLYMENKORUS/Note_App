from typing import List
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import Note, Category
from .schemas import *


api = NinjaAPI()


@api.post('/notes', tags=['Notes'])
def create_note(request, payload: NoteIn):
    data = payload.dict()
    category = Category.objects.get(id=data.get('category'))
    del data['category']
    note = Note.objects.create(category=category, **data)
    return {'id': note.id}


@api.post('/category', tags=['Categories'])
def create_category(request, payload: CategoryIn):
    category = Category.objects.create(**payload.dict())
    return {'id': category.id}


@api.get('/notes/{int:note_id}', response=NoteOut, tags=['Notes'])
def get_note(request, note_id: int):
    note = get_object_or_404(Note, id=note_id)
    return note


@api.get('/category/{int:category_id}', response=CategoryOut, tags=['Categories'])
def get_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    return category


@api.get('/category', response=List[CategoryOut], tags=['Categories'])
def list_categories(request):
    categories = Category.objects.all()
    return categories


@api.get('/notes', response=List[NoteOut], tags=['Notes'])
def list_notes(request):
    notes = Note.objects.all()
    return notes


@api.patch('/notes/{int:notes_id}', tags=['Notes'])
def update_note(request, notes_id: int, payload: NoteUpd):
    note = get_object_or_404(Note, id=notes_id)
    for attr, value in payload.dict().items():
        setattr(note, attr, value)
    note.save()
    return {'success': True}


@api.put('/category/{int:category_id}', tags=['Categories'])
def update_category(request, category_id: int, payload: CategoryIn):
    category = get_object_or_404(Category, id=category_id)
    for attr, value in payload.dict().items():
        setattr(category, attr, value)
    category.save()
    return {'success': True}


@api.api_operation(['DELETE'], '/notes/{int:notes_id}', tags=['Notes'])
def delete_note(request, notes_id: int):
    note = get_object_or_404(Note, id=notes_id)
    note.delete()
    return {'success': True}


@api.delete('/category/{int:category_id}', tags=['Categories'])
def delete_category(request, category_id: int):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return {'success': True}



