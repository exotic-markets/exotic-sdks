from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container, Construct
import borsh_construct as borsh


class ExpireProductOverrideArgsJSON(typing.TypedDict):
    spots: list[int]


@dataclass
class ExpireProductOverrideArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "spots" / borsh.Vec(typing.cast(Construct, borsh.U64))
    )
    spots: list[int]

    @classmethod
    def from_decoded(cls, obj: Container) -> "ExpireProductOverrideArgs":
        return cls(spots=obj.spots)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"spots": self.spots}

    def to_json(self) -> ExpireProductOverrideArgsJSON:
        return {"spots": self.spots}

    @classmethod
    def from_json(
        cls, obj: ExpireProductOverrideArgsJSON
    ) -> "ExpireProductOverrideArgs":
        return cls(spots=obj["spots"])
