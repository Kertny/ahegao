from faststream.rabbit.fastapi import RabbitRouter

node = RabbitRouter()

@node.post("/order")
async def make_params(name: str):
    await node.broker.publish(
        f'push: {name}',
        queue=name
    )
    return {"data": "ok"}