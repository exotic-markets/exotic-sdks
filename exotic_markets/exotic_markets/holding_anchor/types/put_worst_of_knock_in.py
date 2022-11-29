from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class PutWorstOfKnockInJSON(typing.TypedDict):
    strike: int
    knock_in: int


@dataclass
class PutWorstOfKnockIn:
    layout: typing.ClassVar = borsh.CStruct(
        "strike" / borsh.U64, "knock_in" / borsh.U64
    )
    strike: int
    knock_in: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "PutWorstOfKnockIn":
        return cls(strike=obj.strike, knock_in=obj.knock_in)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"strike": self.strike, "knock_in": self.knock_in}

    def to_json(self) -> PutWorstOfKnockInJSON:
        return {"strike": self.strike, "knock_in": self.knock_in}

    @classmethod
    def from_json(cls, obj: PutWorstOfKnockInJSON) -> "PutWorstOfKnockIn":
        return cls(strike=obj["strike"], knock_in=obj["knock_in"])
