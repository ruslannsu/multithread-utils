import os
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor
from utils.base_util import BaseUtil

class RMutil(BaseUtil):
    def __init__(self, path: str, proc_count=4) -> None:
        super().__init__(path)
        self._processes = proc_count
    
    def _remove_wrapper(self, path: str) -> None:
        self._remove_rec(path)
        os.rmdir(path)

    def _remove_rec(self, path: str) -> None:  
        _root, dirs, files = next(os.walk(path))

        for file in files:
            file_path = os.path.join(path, file)
            os.remove(file_path)

        if len(dirs) == 0:
            return

        for dir in dirs:
            dir_path = os.path.join(path, dir)
            self._remove_rec(dir_path)
            os.rmdir(dir_path)
        
        
    def _remove_batch(self, paths: list) -> None:
        for path in  paths:
            self._remove_wrapper(path=path)

    def _remove(self):
        dirs = next(os.walk(self._path))[1]
        
        task_args = []
        step = len(dirs) // self._processes
        for i in range(self._processes):
            left = i * step
            right = (i + 1) * step

            if right >= len(dirs):
                right = len(dirs)
                
            task_paths = dirs[left:right]
            task_paths = [os.path.join(self._path, task_path) for task_path in task_paths]
            task_args.append(task_paths)

        with mp.Pool(processes=self._processes) as process_pool:
            process_pool.map(self._remove_batch, task_args)
        
    def run(self):
        self._remove()