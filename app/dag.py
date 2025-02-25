from typing import Any

from mlflow_tracker import node_context

async def step_one(input: str) -> str:
    updated = f"step_one: {input}"
    print(updated)
    print(f'step_one node_context is {node_context.get()}\n\n')
    return updated

async def step_two(step_one: str) -> str:
    updated = f"step_two: {step_one}"
    print(updated)
    print(f'step_two node_context is {node_context.get()}\n\n')
    return updated