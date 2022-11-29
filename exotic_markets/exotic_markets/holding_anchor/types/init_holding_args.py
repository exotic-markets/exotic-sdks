from __future__ import annotations
from . import (
    order_possible_direction,
)
import typing
from dataclasses import dataclass
from construct import Container
import borsh_construct as borsh


class InitHoldingArgsJSON(typing.TypedDict):
    end_collection: int
    start_auction: int
    end_auction: int
    authority_ai_bump: int
    possible_order_direction: order_possible_direction.OrderPossibleDirectionJSON
    max_total_deposit: typing.Optional[int]
    max_deposit_per_user: typing.Optional[int]
    min_deposit_per_user: int
    est_yield: int
    min_yield: int
    min_bid_increment: int
    risk_level: int


@dataclass
class InitHoldingArgs:
    layout: typing.ClassVar = borsh.CStruct(
        "end_collection" / borsh.U64,
        "start_auction" / borsh.U64,
        "end_auction" / borsh.U64,
        "authority_ai_bump" / borsh.U8,
        "possible_order_direction" / order_possible_direction.layout,
        "max_total_deposit" / borsh.Option(borsh.U64),
        "max_deposit_per_user" / borsh.Option(borsh.U64),
        "min_deposit_per_user" / borsh.U64,
        "est_yield" / borsh.U64,
        "min_yield" / borsh.U64,
        "min_bid_increment" / borsh.U64,
        "risk_level" / borsh.U8,
    )
    end_collection: int
    start_auction: int
    end_auction: int
    authority_ai_bump: int
    possible_order_direction: order_possible_direction.OrderPossibleDirectionKind
    max_total_deposit: typing.Optional[int]
    max_deposit_per_user: typing.Optional[int]
    min_deposit_per_user: int
    est_yield: int
    min_yield: int
    min_bid_increment: int
    risk_level: int

    @classmethod
    def from_decoded(cls, obj: Container) -> "InitHoldingArgs":
        return cls(
            end_collection=obj.end_collection,
            start_auction=obj.start_auction,
            end_auction=obj.end_auction,
            authority_ai_bump=obj.authority_ai_bump,
            possible_order_direction=order_possible_direction.from_decoded(
                obj.possible_order_direction
            ),
            max_total_deposit=obj.max_total_deposit,
            max_deposit_per_user=obj.max_deposit_per_user,
            min_deposit_per_user=obj.min_deposit_per_user,
            est_yield=obj.est_yield,
            min_yield=obj.min_yield,
            min_bid_increment=obj.min_bid_increment,
            risk_level=obj.risk_level,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "end_collection": self.end_collection,
            "start_auction": self.start_auction,
            "end_auction": self.end_auction,
            "authority_ai_bump": self.authority_ai_bump,
            "possible_order_direction": self.possible_order_direction.to_encodable(),
            "max_total_deposit": self.max_total_deposit,
            "max_deposit_per_user": self.max_deposit_per_user,
            "min_deposit_per_user": self.min_deposit_per_user,
            "est_yield": self.est_yield,
            "min_yield": self.min_yield,
            "min_bid_increment": self.min_bid_increment,
            "risk_level": self.risk_level,
        }

    def to_json(self) -> InitHoldingArgsJSON:
        return {
            "end_collection": self.end_collection,
            "start_auction": self.start_auction,
            "end_auction": self.end_auction,
            "authority_ai_bump": self.authority_ai_bump,
            "possible_order_direction": self.possible_order_direction.to_json(),
            "max_total_deposit": self.max_total_deposit,
            "max_deposit_per_user": self.max_deposit_per_user,
            "min_deposit_per_user": self.min_deposit_per_user,
            "est_yield": self.est_yield,
            "min_yield": self.min_yield,
            "min_bid_increment": self.min_bid_increment,
            "risk_level": self.risk_level,
        }

    @classmethod
    def from_json(cls, obj: InitHoldingArgsJSON) -> "InitHoldingArgs":
        return cls(
            end_collection=obj["end_collection"],
            start_auction=obj["start_auction"],
            end_auction=obj["end_auction"],
            authority_ai_bump=obj["authority_ai_bump"],
            possible_order_direction=order_possible_direction.from_json(
                obj["possible_order_direction"]
            ),
            max_total_deposit=obj["max_total_deposit"],
            max_deposit_per_user=obj["max_deposit_per_user"],
            min_deposit_per_user=obj["min_deposit_per_user"],
            est_yield=obj["est_yield"],
            min_yield=obj["min_yield"],
            min_bid_increment=obj["min_bid_increment"],
            risk_level=obj["risk_level"],
        )
