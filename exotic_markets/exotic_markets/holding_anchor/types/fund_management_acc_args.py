from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class FundManagementAccArgsJSON(typing.TypedDict):
    management_acc_bump: int


@dataclass
class FundManagementAccArgs:
    layout: typing.ClassVar = borsh.CStruct("management_acc_bump" / borsh.U8)
    management_acc_bump: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "FundManagementAccArgs":
        return cls(management_acc_bump=obj.management_acc_bump)

    def to_encodable(self) -> dict[str, typing.Any]:
        return {"management_acc_bump": self.management_acc_bump}

    def to_json(self) -> FundManagementAccArgsJSON:
        return {"management_acc_bump": self.management_acc_bump}

    @classmethod
    def from_json(cls, obj: FundManagementAccArgsJSON) -> "FundManagementAccArgs":
        return cls(management_acc_bump=obj["management_acc_bump"])
