import os
from utils.base_util import BaseUtil

class RMutil(BaseUtil):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        
    def _remove_default(self, path):
        
        dirs = next(os.walk(path))[1]
        files = next(os.walk(path))[2]

        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)

        if len(dirs) == 0:
            return

        for dir in dirs:
            dir_path = os.path.join(path, dir)
            self._remove_default(dir_path)
            os.rmdir(dir_path)
    
    def run(self):
        self._remove_default(self._path)
            

        
