import os
from utils.base_util import BaseUtil

class RMutil(BaseUtil):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        
    def run(self):
        
        for dirpath, dirnames, filenames in os.walk(self._path):
            for fname in filenames:
                os.remove(fname)
            
            

        
