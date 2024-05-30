from time import sleep
import asyncio

class SyncSpongeBob():
    def cook_bread(self):
        sleep(3)

    def cook_hamburger(self):
        sleep(10)
    
    def mount_sandwich(self):
        sleep(3)

    def make_milkshake(self):
        sleep(5)

    def cook(self):
        self.cook_bread()
        self.cook_hamburger()
        self.mount_sandwich()
        self.make_milkshake()

class AsyncSpongeBob():
    async def cook_bread(self):
        await asyncio.sleep(3)

    async def cook_hamburger(self):
        await asyncio.sleep(10)
    
    async def mount_sandwich(self):
        await asyncio.sleep(3)

    async def make_milkshake(self):
        await asyncio.sleep(5)

    async def make_sandwich(self):
        await asyncio.gather(
            self.cook_bread(),
            self.cook_hamburger()
        )
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.mount_sandwich())

    async def cook(self):
        await asyncio.gather(
            self.make_sandwich(),
            self.make_milkshake()
        )        


# sync_spngebob = SyncSpongeBob()
# sync_spngebob.cook()
async_spngebob = AsyncSpongeBob()
asyncio.run(async_spngebob.cook())

