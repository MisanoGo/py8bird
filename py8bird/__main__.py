import asyncio
import threading

from aiobot import main as am
from twee import main as tm

aml = lambda : asyncio.run(am())
tml = lambda : asyncio.run(tm())

if __name__=="__main__":
    threading.Thread(target=aml).start()
    threading.Thread(target=tml).start()
    
