from typing import TYPE_CHECKING
from typing import Any
from typing import Dict
from typing import Type
from typing import TypeVar

from pydantic import BaseModel

if TYPE_CHECKING:
    from websockets.legacy.client import WebSocketClientProtocol

T = TypeVar("T", bound=BaseModel)


class MessageModel(BaseModel):
    @property
    def type(self: "MessageModel") -> str:
        return self.__class__.__name__

    def dict(self: "MessageModel", *args: Any, **kwargs: Any) -> Dict[str, Any]:
        base_dict = super().dict(*args, **kwargs)
        return {**base_dict, "type": self.type}


class StartExecutionRequest(MessageModel):
    code: str


class ExecutionStartedResponse(MessageModel):
    stages: int


class StageStartedNotification(MessageModel):
    stage: str


class StageFinishedNotification(MessageModel):
    stage: str
    succeeded: bool
    exit_code: str


class ExecutionFinishedNotification(MessageModel):
    succeeded: bool
    exit_code: int


class ExecutionOutputNotification(MessageModel):
    stage: str
    output: str


class ExecutionFailedResponse(MessageModel):
    detail: str
    traceback: str


async def recv_as(ws: "WebSocketClientProtocol", model: Type[T]) -> T:
    return model.parse_raw(await ws.recv())


async def send(ws: "WebSocketClientProtocol", message: BaseModel) -> None:
    await ws.send(message.json(by_alias=True))
