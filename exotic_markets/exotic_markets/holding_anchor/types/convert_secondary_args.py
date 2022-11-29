from __future__ import annotations
from . import (
    order_direction,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class ConvertSecondaryArgsJSON(typing.TypedDict):
    direction: order_direction.OrderDirectionJSON


@dataclass
class ConvertSecondaryArgs:
    layout: typing.ClassVar = borsh.CStruct("direction" / order_direction.layout)
    direction: order_direction.OrderDirectionKind

    @classmethod
    def from_decoded(cls, obj: Container) -> "ConvertSecondaryArgs":
        return cls(direction=order_direction.from_decoded(obj.direction))

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"direction": self.direction.to_encodable()}

    def to_json(self) -> ConvertSecondaryArgsJSON:
        return {"direction": self.direction.to_json()}

    @classmethod
    def from_json(cls, obj: ConvertSecondaryArgsJSON) -> "ConvertSecondaryArgs":
        return cls(direction=order_direction.from_json(obj["direction"]))
