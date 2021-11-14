#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
