from faststream.rabbit.broker import RabbitBroker
from faststream import FastStream
import logging
import asyncio

log = logging.getLogger()
reception = RabbitBroker()
app = FastStream(reception)

@reception.subscriber("cross")
async def load_message(data: str):
    log.warning(f'Получено сообщение {data}')


# if __name__ == "__main__":
