from faststream.rabbit.fastapi import RabbitRouter

node = RabbitRouter()

@node.post("/cross")
async def make_params(name: str):
    await node.broker.publish(
        f'{name}',
        queue="cross",
    )
    return {"data": "ok"}