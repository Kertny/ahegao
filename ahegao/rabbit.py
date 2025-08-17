from faststream.rabbit.fastapi import RabbitRouter
from structure import Settings
import os

rabbit = Settings.RABBIT_URL = os.getenv("RABBIT")

node = RabbitRouter(rabbit)

@node.post("/cross")
def make_params(name: str):
    node.broker.publish(
        f'{name}',
        queue="cross",
    )
    return {"data": "ok"}

@node.post("/calibration")
def calibration_maker(name: str):
    node.broker.publish(
        f'{name}',
        queue="cross"
    )
