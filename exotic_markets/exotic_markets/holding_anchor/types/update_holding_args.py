from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class UpdateHoldingArgsJSON(typing.TypedDict):
    new_est_yield: int
    new_min_yield: int


@dataclass
class UpdateHoldingArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "new_est_yield" / borsh.U64, "new_min_yield" / borsh.U64
    )
    new_est_yield: int
    new_min_yield: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdateHoldingArgs":
        return cls(new_est_yield=obj.new_est_yield, new_min_yield=obj.new_min_yield)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "new_est_yield": self.new_est_yield,
            "new_min_yield": self.new_min_yield,
        }

    def to_json(self) -> UpdateHoldingArgsJSON:
        return {
            "new_est_yield": self.new_est_yield,
            "new_min_yield": self.new_min_yield,
        }

    @classmethod
    def from_json(cls, obj: UpdateHoldingArgsJSON) -> "UpdateHoldingArgs":
        return cls(
            new_est_yield=obj["new_est_yield"], new_min_yield=obj["new_min_yield"]
        )
