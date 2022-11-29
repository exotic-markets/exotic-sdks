from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class PutSellingJSON(typing.TypedDict):
    strike: int


@dataclass
class PutSelling:
    layout: typing.ClassVar = borsh.CStruct("strike" / borsh.U64)
    strike: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "PutSelling":
        return cls(strike=obj.strike)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"strike": self.strike}

    def to_json(self) -> PutSellingJSON:
        return {"strike": self.strike}

    @classmethod
    def from_json(cls, obj: PutSellingJSON) -> "PutSelling":
        return cls(strike=obj["strike"])
