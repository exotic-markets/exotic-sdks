from __future__ import annotations
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class BuyJSON(typing.TypedDict):
    kind: typing.Literal["Buy"]


class SellJSON(typing.TypedDict):
    kind: typing.Literal["Sell"]


class BuyAndSellJSON(typing.TypedDict):
    kind: typing.Literal["BuyAndSell"]


@dataclass
class Buy:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "Buy"

    @classmethod
    def to_json(cls) -> BuyJSON:
        return BuyJSON(
            kind="Buy",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Buy": {},
        }


@dataclass
class Sell:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "Sell"

    @classmethod
    def to_json(cls) -> SellJSON:
        return SellJSON(
            kind="Sell",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "Sell": {},
        }


@dataclass
class BuyAndSell:
    discriminator: typing.ClassVar = 2
    kind: typing.ClassVar = "BuyAndSell"

    @classmethod
    def to_json(cls) -> BuyAndSellJSON:
        return BuyAndSellJSON(
            kind="BuyAndSell",
        )

    @classmethod
    def to_encodable(cls) -> dict:
        return {
            "BuyAndSell": {},
        }


OrderPossibleDirectionKind = typing.Union[Buy, Sell, BuyAndSell]
OrderPossibleDirectionJSON = typing.Union[BuyJSON, SellJSON, BuyAndSellJSON]


def from_decoded(obj: dict) -> OrderPossibleDirectionKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "Buy" in obj:
        return Buy()
    if "Sell" in obj:
        return Sell()
    if "BuyAndSell" in obj:
        return BuyAndSell()
    raise ValueError("Invalid enum object")


def from_json(obj: OrderPossibleDirectionJSON) -> OrderPossibleDirectionKind:
    if obj["kind"] == "Buy":
        return Buy()
    if obj["kind"] == "Sell":
        return Sell()
    if obj["kind"] == "BuyAndSell":
        return BuyAndSell()
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
    "Buy" / borsh.CStruct(), "Sell" / borsh.CStruct(), "BuyAndSell" / borsh.CStruct()
)
