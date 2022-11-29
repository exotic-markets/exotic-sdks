from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
from solana.publickey import PublicKey
from anchorpy.borsh_extension import BorshPubkey
import borsh_construct as borsh


class UpdateStateArgsJSON(typing.TypedDict):
    new_admin: str


@dataclass
class UpdateStateArgs:
    layout: typing.ClassVar = borsh.CStruct("new_admin" / BorshPubkey)
    new_admin: PublicKey

    @classmethod
    def from_decoded(cls, obj: Container) -> "UpdateStateArgs":
        return cls(new_admin=obj.new_admin)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"new_admin": self.new_admin}

    def to_json(self) -> UpdateStateArgsJSON:
        return {"new_admin": str(self.new_admin)}

    @classmethod
    def from_json(cls, obj: UpdateStateArgsJSON) -> "UpdateStateArgs":
        return cls(new_admin=PublicKey(obj["new_admin"]))
