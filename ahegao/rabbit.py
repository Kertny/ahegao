from faststream.rabbit.fastapi import RabbitRouter
from structure import Settings
import os

rabbit = "amqp://guest:guest@172.20.10.5:5672/"

node = RabbitRouter(rabbit)

@node.post("/cross")
async def make_params(name: str):
    await node.broker.publish(
        f'{name}',
        queue="cross",
    )
    return {"data": "ok"}

@node.post("/calibration")
async def calibration_maker(name: str):
    await node.broker.publish(
        f'{name}',
        queue="cross"
    )
