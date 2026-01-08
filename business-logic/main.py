from faststream.rabbit.broker import RabbitBroker
from faststream import FastStream
import logging
import asyncio
import os

rabbit = os.getenv("RABBIT")
log = logging.getLogger()
reception = RabbitBroker(rabbit)
app = FastStream(reception)

@reception.subscriber("cross")
async def load_message(data: str):
    log.warning(f'Получено сообщение {data}')


# if __name__ == "__main__":
