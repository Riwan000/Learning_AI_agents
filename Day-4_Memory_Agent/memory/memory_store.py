import json 
import os 
 
class MemoryStore:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def get_memory(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def add_exchange(self, role, content):
        memory = self.get_memory()
        memory.append({'role':role, 'content':content})
        with open(self.file_path, 'w') as f:
            json.dump(memory[-10:], f)
            