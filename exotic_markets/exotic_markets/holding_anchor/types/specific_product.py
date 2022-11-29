from __future__ import annotations
from . import (
    buy_below_market,
    sell_above_market,
    put_worst_of,
    put_worst_of_knock_in,
    put_selling,
    call_override,
)
import typing
from dataclasses import dataclass
from anchorpy.borsh_extension import EnumForCodegen
import borsh_construct as borsh


class PutWorstOfProductJSONValue(typing.TypedDict):
    put_worst_of: put_worst_of.PutWorstOfJSON


class BuyBelowMarketProductJSONValue(typing.TypedDict):
    buy_below_market: buy_below_market.BuyBelowMarketJSON


class SellAboveMarketProductJSONValue(typing.TypedDict):
    sell_above_market: sell_above_market.SellAboveMarketJSON


class PutWorstOfKnockInProductJSONValue(typing.TypedDict):
    put_worst_of_knock_in: put_worst_of_knock_in.PutWorstOfKnockInJSON


class PutSellingProductJSONValue(typing.TypedDict):
    put_selling: put_selling.PutSellingJSON


class CallOverrideProductJSONValue(typing.TypedDict):
    call_override: call_override.CallOverrideJSON


class PutWorstOfProductValue(typing.TypedDict):
    put_worst_of: put_worst_of.PutWorstOf


class BuyBelowMarketProductValue(typing.TypedDict):
    buy_below_market: buy_below_market.BuyBelowMarket


class SellAboveMarketProductValue(typing.TypedDict):
    sell_above_market: sell_above_market.SellAboveMarket


class PutWorstOfKnockInProductValue(typing.TypedDict):
    put_worst_of_knock_in: put_worst_of_knock_in.PutWorstOfKnockIn


class PutSellingProductValue(typing.TypedDict):
    put_selling: put_selling.PutSelling


class CallOverrideProductValue(typing.TypedDict):
    call_override: call_override.CallOverride


class PutWorstOfProductJSON(typing.TypedDict):
    value: PutWorstOfProductJSONValue
    kind: typing.Literal["PutWorstOfProduct"]


class BuyBelowMarketProductJSON(typing.TypedDict):
    value: BuyBelowMarketProductJSONValue
    kind: typing.Literal["BuyBelowMarketProduct"]


class SellAboveMarketProductJSON(typing.TypedDict):
    value: SellAboveMarketProductJSONValue
    kind: typing.Literal["SellAboveMarketProduct"]


class PutWorstOfKnockInProductJSON(typing.TypedDict):
    value: PutWorstOfKnockInProductJSONValue
    kind: typing.Literal["PutWorstOfKnockInProduct"]


class PutSellingProductJSON(typing.TypedDict):
    value: PutSellingProductJSONValue
    kind: typing.Literal["PutSellingProduct"]


class CallOverrideProductJSON(typing.TypedDict):
    value: CallOverrideProductJSONValue
    kind: typing.Literal["CallOverrideProduct"]


@dataclass
class PutWorstOfProduct:
    discriminator: typing.ClassVar = 0
    kind: typing.ClassVar = "PutWorstOfProduct"
    value: PutWorstOfProductValue

    def to_json(self) -> PutWorstOfProductJSON:
        return PutWorstOfProductJSON(
            kind="PutWorstOfProduct",
            value={
                "put_worst_of": self.value["put_worst_of"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "PutWorstOfProduct": {
                "put_worst_of": self.value["put_worst_of"].to_encodable(),
            },
        }


@dataclass
class BuyBelowMarketProduct:
    discriminator: typing.ClassVar = 1
    kind: typing.ClassVar = "BuyBelowMarketProduct"
    value: BuyBelowMarketProductValue

    def to_json(self) -> BuyBelowMarketProductJSON:
        return BuyBelowMarketProductJSON(
            kind="BuyBelowMarketProduct",
            value={
                "buy_below_market": self.value["buy_below_market"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "BuyBelowMarketProduct": {
                "buy_below_market": self.value["buy_below_market"].to_encodable(),
            },
        }


@dataclass
class SellAboveMarketProduct:
    discriminator: typing.ClassVar = 2
    kind: typing.ClassVar = "SellAboveMarketProduct"
    value: SellAboveMarketProductValue

    def to_json(self) -> SellAboveMarketProductJSON:
        return SellAboveMarketProductJSON(
            kind="SellAboveMarketProduct",
            value={
                "sell_above_market": self.value["sell_above_market"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "SellAboveMarketProduct": {
                "sell_above_market": self.value["sell_above_market"].to_encodable(),
            },
        }


@dataclass
class PutWorstOfKnockInProduct:
    discriminator: typing.ClassVar = 3
    kind: typing.ClassVar = "PutWorstOfKnockInProduct"
    value: PutWorstOfKnockInProductValue

    def to_json(self) -> PutWorstOfKnockInProductJSON:
        return PutWorstOfKnockInProductJSON(
            kind="PutWorstOfKnockInProduct",
            value={
                "put_worst_of_knock_in": self.value["put_worst_of_knock_in"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "PutWorstOfKnockInProduct": {
                "put_worst_of_knock_in": self.value[
                    "put_worst_of_knock_in"
                ].to_encodable(),
            },
        }


@dataclass
class PutSellingProduct:
    discriminator: typing.ClassVar = 4
    kind: typing.ClassVar = "PutSellingProduct"
    value: PutSellingProductValue

    def to_json(self) -> PutSellingProductJSON:
        return PutSellingProductJSON(
            kind="PutSellingProduct",
            value={
                "put_selling": self.value["put_selling"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "PutSellingProduct": {
                "put_selling": self.value["put_selling"].to_encodable(),
            },
        }


@dataclass
class CallOverrideProduct:
    discriminator: typing.ClassVar = 5
    kind: typing.ClassVar = "CallOverrideProduct"
    value: CallOverrideProductValue

    def to_json(self) -> CallOverrideProductJSON:
        return CallOverrideProductJSON(
            kind="CallOverrideProduct",
            value={
                "call_override": self.value["call_override"].to_json(),
            },
        )

    def to_encodable(self) -> dict:
        return {
            "CallOverrideProduct": {
                "call_override": self.value["call_override"].to_encodable(),
            },
        }


SpecificProductKind = typing.Union[
    PutWorstOfProduct,
    BuyBelowMarketProduct,
    SellAboveMarketProduct,
    PutWorstOfKnockInProduct,
    PutSellingProduct,
    CallOverrideProduct,
]
SpecificProductJSON = typing.Union[
    PutWorstOfProductJSON,
    BuyBelowMarketProductJSON,
    SellAboveMarketProductJSON,
    PutWorstOfKnockInProductJSON,
    PutSellingProductJSON,
    CallOverrideProductJSON,
]


def from_decoded(obj: dict) -> SpecificProductKind:
    if not isinstance(obj, dict):
        raise ValueError("Invalid enum object")
    if "PutWorstOfProduct" in obj:
        val = obj["PutWorstOfProduct"]
        return PutWorstOfProduct(
            PutWorstOfProductValue(
                put_worst_of=put_worst_of.PutWorstOf.from_decoded(val["put_worst_of"]),
            )
        )
    if "BuyBelowMarketProduct" in obj:
        val = obj["BuyBelowMarketProduct"]
        return BuyBelowMarketProduct(
            BuyBelowMarketProductValue(
                buy_below_market=buy_below_market.BuyBelowMarket.from_decoded(
                    val["buy_below_market"]
                ),
            )
        )
    if "SellAboveMarketProduct" in obj:
        val = obj["SellAboveMarketProduct"]
        return SellAboveMarketProduct(
            SellAboveMarketProductValue(
                sell_above_market=sell_above_market.SellAboveMarket.from_decoded(
                    val["sell_above_market"]
                ),
            )
        )
    if "PutWorstOfKnockInProduct" in obj:
        val = obj["PutWorstOfKnockInProduct"]
        return PutWorstOfKnockInProduct(
            PutWorstOfKnockInProductValue(
                put_worst_of_knock_in=put_worst_of_knock_in.PutWorstOfKnockIn.from_decoded(
                    val["put_worst_of_knock_in"]
                ),
            )
        )
    if "PutSellingProduct" in obj:
        val = obj["PutSellingProduct"]
        return PutSellingProduct(
            PutSellingProductValue(
                put_selling=put_selling.PutSelling.from_decoded(val["put_selling"]),
            )
        )
    if "CallOverrideProduct" in obj:
        val = obj["CallOverrideProduct"]
        return CallOverrideProduct(
            CallOverrideProductValue(
                call_override=call_override.CallOverride.from_decoded(
                    val["call_override"]
                ),
            )
        )
    raise ValueError("Invalid enum object")


def from_json(obj: SpecificProductJSON) -> SpecificProductKind:
    if obj["kind"] == "PutWorstOfProduct":
        put_worst_of_product_json_value = typing.cast(
            PutWorstOfProductJSONValue, obj["value"]
        )
        return PutWorstOfProduct(
            PutWorstOfProductValue(
                put_worst_of=put_worst_of.PutWorstOf.from_json(
                    put_worst_of_product_json_value["put_worst_of"]
                ),
            )
        )
    if obj["kind"] == "BuyBelowMarketProduct":
        buy_below_market_product_json_value = typing.cast(
            BuyBelowMarketProductJSONValue, obj["value"]
        )
        return BuyBelowMarketProduct(
            BuyBelowMarketProductValue(
                buy_below_market=buy_below_market.BuyBelowMarket.from_json(
                    buy_below_market_product_json_value["buy_below_market"]
                ),
            )
        )
    if obj["kind"] == "SellAboveMarketProduct":
        sell_above_market_product_json_value = typing.cast(
            SellAboveMarketProductJSONValue, obj["value"]
        )
        return SellAboveMarketProduct(
            SellAboveMarketProductValue(
                sell_above_market=sell_above_market.SellAboveMarket.from_json(
                    sell_above_market_product_json_value["sell_above_market"]
                ),
            )
        )
    if obj["kind"] == "PutWorstOfKnockInProduct":
        put_worst_of_knock_in_product_json_value = typing.cast(
            PutWorstOfKnockInProductJSONValue, obj["value"]
        )
        return PutWorstOfKnockInProduct(
            PutWorstOfKnockInProductValue(
                put_worst_of_knock_in=put_worst_of_knock_in.PutWorstOfKnockIn.from_json(
                    put_worst_of_knock_in_product_json_value["put_worst_of_knock_in"]
                ),
            )
        )
    if obj["kind"] == "PutSellingProduct":
        put_selling_product_json_value = typing.cast(
            PutSellingProductJSONValue, obj["value"]
        )
        return PutSellingProduct(
            PutSellingProductValue(
                put_selling=put_selling.PutSelling.from_json(
                    put_selling_product_json_value["put_selling"]
                ),
            )
        )
    if obj["kind"] == "CallOverrideProduct":
        call_override_product_json_value = typing.cast(
            CallOverrideProductJSONValue, obj["value"]
        )
        return CallOverrideProduct(
            CallOverrideProductValue(
                call_override=call_override.CallOverride.from_json(
                    call_override_product_json_value["call_override"]
                ),
            )
        )
    kind = obj["kind"]
    raise ValueError(f"Unrecognized enum kind: {kind}")


layout = EnumForCodegen(
    "PutWorstOfProduct"
    / borsh.CStruct("put_worst_of" / put_worst_of.PutWorstOf.layout),
    "BuyBelowMarketProduct"
    / borsh.CStruct("buy_below_market" / buy_below_market.BuyBelowMarket.layout),
    "SellAboveMarketProduct"
    / borsh.CStruct("sell_above_market" / sell_above_market.SellAboveMarket.layout),
    "PutWorstOfKnockInProduct"
    / borsh.CStruct(
        "put_worst_of_knock_in" / put_worst_of_knock_in.PutWorstOfKnockIn.layout
    ),
    "PutSellingProduct" / borsh.CStruct("put_selling" / put_selling.PutSelling.layout),
    "CallOverrideProduct"
    / borsh.CStruct("call_override" / call_override.CallOverride.layout),
)
