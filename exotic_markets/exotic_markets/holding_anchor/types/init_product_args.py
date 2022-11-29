from __future__ import annotations
from . import (
    specific_product,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class InitProductArgsJSON(typing.TypedDict):
    maturity: int
    underlying_count: int
    specific_data: specific_product.SpecificProductJSON


@dataclass
class InitProductArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "maturity" / borsh.U32,
        "underlying_count" / borsh.U8,
        "specific_data" / specific_product.layout,
    )
    maturity: int
    underlying_count: int
    specific_data: specific_product.SpecificProductKind

    @classmethod
    def from_decoded(cls, obj: Container) -> "InitProductArgs":
        return cls(
            maturity=obj.maturity,
            underlying_count=obj.underlying_count,
            specific_data=specific_product.from_decoded(obj.specific_data),
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "maturity": self.maturity,
            "underlying_count": self.underlying_count,
            "specific_data": self.specific_data.to_encodable(),
        }

    def to_json(self) -> InitProductArgsJSON:
        return {
            "maturity": self.maturity,
            "underlying_count": self.underlying_count,
            "specific_data": self.specific_data.to_json(),
        }

    @classmethod
    def from_json(cls, obj: InitProductArgsJSON) -> "InitProductArgs":
        return cls(
            maturity=obj["maturity"],
            underlying_count=obj["underlying_count"],
            specific_data=specific_product.from_json(obj["specific_data"]),
        )
