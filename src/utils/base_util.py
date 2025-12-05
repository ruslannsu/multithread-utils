from concurrent.futures import ThreadPoolExecutor

class BaseUtil:
    def __init__(self, path: str) -> None:
        self._thread_pool = ThreadPoolExecutor(max_workers=10)
        self._path = path
    
    

