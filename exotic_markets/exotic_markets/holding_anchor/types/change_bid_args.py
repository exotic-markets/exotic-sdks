from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class ChangeBidArgsJSON(typing.TypedDict):
    amount: int


@dataclass
class ChangeBidArgs:
    layout: typing.ClassVar = borsh.CStruct("amount" / borsh.U64)
    amount: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "ChangeBidArgs":
        return cls(amount=obj.amount)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"amount": self.amount}

    def to_json(self) -> ChangeBidArgsJSON:
        return {"amount": self.amount}

    @classmethod
    def from_json(cls, obj: ChangeBidArgsJSON) -> "ChangeBidArgs":
        return cls(amount=obj["amount"])
