# notes_manager.py

import json
from datetime import datetime
from note import Note

class NotesManager:
    def __init__(self):
        self.notes = []