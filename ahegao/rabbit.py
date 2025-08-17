from faststream.rabbit.fastapi import RabbitRouter

node = RabbitRouter("amqp://guest:guest@localhost:5672/")

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
