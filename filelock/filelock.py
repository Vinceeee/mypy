import asyncio
import sys
from typing import AsyncContextManager, Optional

from loguru import logger

class FileLock(AsyncContextManager):
    """Support different platform filelock
    """

    POLLING = 0.1
    DEFAULT_TIMEOUT = 3600

    def __init__(self, lock_fn: str, timeout: Optional[int] = None):
        self.lock_fn = lock_fn
        self.timouet = timeout if timeout else self.DEFAULT_TIMEOUT

    def _aquire(self) -> bool:
        if sys.platform == "win32":
            return self._aquire_win()
        return self._aquire_posix()

    def _aquire_win(self) -> bool:
        raise NotImplementedError

     def _aquire_posix(self) -> bool:
        raise NotImplementedError   

    def _release(self):
        with open(self.lock_fn, "w") as f:
            try:
                #.LOCK_EX   strange results for reading.
                import fcntl, os
                if f.writable(): 
                    fcntl.lockf(f, fcntl.LOCK_UN)
                    return True

            except ModuleNotFoundError:
                # Windows file locking
                import msvcrt, os
                def file_size(f):
                    return os.path.getsize( os.path.realpath(f.name) )
                def lock_file(f):
                    msvcrt.locking(f.fileno(), msvcrt.LK_RLCK, file_size(f))

    async def __aenter__(self):
        timeout = self.timouet
        logger.debug(f"locking file: {self.lock_fn}")
        while timeout > 0:
            await asyncio.sleep(self.POLLING)
            if self._aquire():
                break
            timeout -= self.POLLING

        if timeout <= 0:
            raise asyncio.TimeoutError("Failed to require lock")

        logger.debug(f"locked file: {self.lock_fn}")

    async def __aexit__(self, exc_type, exc_value, traceback):
        self._release()
        logger.debug(f"unlock file: {self.lock_fn}")

