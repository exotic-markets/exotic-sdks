from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class SellAboveMarketJSON(typing.TypedDict):
    strike: int
    knock_out: int


@dataclass
class SellAboveMarket:
    layout: typing.ClassVar = borsh.CStruct(
        "strike" / borsh.U64, "knock_out" / borsh.U64
    )
    strike: int
    knock_out: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "SellAboveMarket":
        return cls(strike=obj.strike, knock_out=obj.knock_out)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"strike": self.strike, "knock_out": self.knock_out}

    def to_json(self) -> SellAboveMarketJSON:
        return {"strike": self.strike, "knock_out": self.knock_out}

    @classmethod
    def from_json(cls, obj: SellAboveMarketJSON) -> "SellAboveMarket":
        return cls(strike=obj["strike"], knock_out=obj["knock_out"])
