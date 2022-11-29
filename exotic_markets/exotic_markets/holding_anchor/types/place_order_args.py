from __future__ import annotations
from . import (
    order_direction,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class PlaceOrderArgsJSON(typing.TypedDict):
    direction: order_direction.OrderDirectionJSON
    amount: int


@dataclass
class PlaceOrderArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "direction" / order_direction.layout, "amount" / borsh.U64
    )
    direction: order_direction.OrderDirectionKind
    amount: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "PlaceOrderArgs":
        return cls(
            direction=order_direction.from_decoded(obj.direction), amount=obj.amount
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"direction": self.direction.to_encodable(), "amount": self.amount}

    def to_json(self) -> PlaceOrderArgsJSON:
        return {"direction": self.direction.to_json(), "amount": self.amount}

    @classmethod
    def from_json(cls, obj: PlaceOrderArgsJSON) -> "PlaceOrderArgs":
        return cls(
            direction=order_direction.from_json(obj["direction"]), amount=obj["amount"]
        )
