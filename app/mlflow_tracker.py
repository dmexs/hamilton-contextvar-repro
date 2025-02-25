from hamilton.lifecycle import base
from hamilton import node, graph
import logging
from typing import Type, Any, Optional, Dict, List
import contextvars
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

node_context = contextvars.ContextVar('node_context', default='ORIGINAL')

class MLFlowTrackerAsync(
    base.BasePreNodeExecuteAsync,
    base.BasePostNodeExecuteAsync,
    # base.BasePreGraphExecuteAsync,
    # base.BasePostGraphExecuteAsync,
):
    def __init__(self, *args, **kwargs):
        pass

    async def pre_node_execute(
        self,
        run_id: str,
        node_: node.Node,
        kwargs: Dict[str, Any],
        task_id: Optional[str] = None
    ) -> None:
        init_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f'init_time is {init_time}')
        node_context.set(init_time)

        node_context.set(init_time)
        print(f'pre node_context is {node_context.get()}\n\n')

    async def post_node_execute(
        self,
        run_id: str,
        node_: node.Node,
        success: bool,
        error: Optional[Exception],
        result: Any,
        task_id: Optional[str] = None,
        **future_kwargs: dict,
    ) -> None:

        print(f'post node_context is {node_context.get()}\n\n')
        node_context.set(None)
