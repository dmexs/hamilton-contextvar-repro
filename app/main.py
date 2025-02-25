from hamilton import async_driver, base, registry
import asyncio

import dag
from mlflow_tracker import MLFlowTrackerAsync

registry.disable_autoload()

async def main():
    dr = async_driver.AsyncDriver(
        {},
        dag,
        result_builder=base.DictResult(),
        adapters=[MLFlowTrackerAsync()],
    )

    await dr.execute(
        [
            'step_one',
            'step_two',
        ],
        inputs={
            'input': 'HELLO',
        }
    )

if __name__ == "__main__":
    asyncio.run(main())