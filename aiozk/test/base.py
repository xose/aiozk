from aiozk import ZKClient
from .aio_test import AIOTestCase


class ZKBase(AIOTestCase):

    async def client(self):
        c = ZKClient('localhost', chroot='/test_aiozk')
        await c.start()
        self.clients.append(c)
        return c

    async def setUp(self):
        self.clients = []
        self.c = ZKClient('localhost', chroot='/test_aiozk')
        await self.c.start()

    async def tearDown(self):
        for c in self.clients:
            await c.close()
        await self.c.delete('/')
        await self.c.close()