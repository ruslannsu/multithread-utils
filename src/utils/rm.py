import os
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from utils.base_util import BaseUtil

class RMutil(BaseUtil):
    def __init__(self, path: str) -> None:
        super().__init__(path)
        self._thread_pool = ThreadPoolExecutor(max_workers=700)
        
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
    

    #threading is useless for remove
    def _remove_with_threads(self, path):
        dirs = next(os.walk(path))[1]
        files = next(os.walk(path))[2]

        if len(dirs) == 0:
            for file in files:
                file_path = os.path.join(path, file)
                os.remove(file_path)
            return
        
        futures = []
        for dir in dirs:
            dir_path = os.path.join(path, dir)
            futures.append((self._thread_pool.submit(self._remove_with_threads, dir_path), dir_path))

        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)

        for future in futures:
            res, arg = future
            res.result()
            os.rmdir(arg)

    def _remove_with_multiprocessing(self, path):
        pass
           
        
    def run(self):
        
        
               
        
        
        
