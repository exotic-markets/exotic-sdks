from __future__ import annotations
import typing
from dataclasses import dataclass
from construct import Container, Construct
from solana.publickey import PublicKey
from anchorpy.borsh_extension import BorshPubkey
import borsh_construct as borsh


class ProductCommonJSON(typing.TypedDict):
    underlying: list[str]
    maturity: int
    deposit_buy_mint: str
    deposit_sell_mint: str
    quote_underlying: str


@dataclass
class ProductCommon:
    layout: typing.ClassVar = borsh.CStruct(
        "underlying" / borsh.Vec(typing.cast(Construct, BorshPubkey)),
        "maturity" / borsh.U32,
        "deposit_buy_mint" / BorshPubkey,
        "deposit_sell_mint" / BorshPubkey,
        "quote_underlying" / BorshPubkey,
    )
    underlying: list[PublicKey]
    maturity: int
    deposit_buy_mint: PublicKey
    deposit_sell_mint: PublicKey
    quote_underlying: PublicKey

    @classmethod
    def from_decoded(cls, obj: Container) -> "ProductCommon":
        return cls(
            underlying=obj.underlying,
            maturity=obj.maturity,
            deposit_buy_mint=obj.deposit_buy_mint,
            deposit_sell_mint=obj.deposit_sell_mint,
            quote_underlying=obj.quote_underlying,
        )

    def to_encodable(self) -> dict[str, typing.Any]:
        return {
            "underlying": self.underlying,
            "maturity": self.maturity,
            "deposit_buy_mint": self.deposit_buy_mint,
            "deposit_sell_mint": self.deposit_sell_mint,
            "quote_underlying": self.quote_underlying,
        }

    def to_json(self) -> ProductCommonJSON:
        return {
            "underlying": list(map(lambda item: str(item), self.underlying)),
            "maturity": self.maturity,
            "deposit_buy_mint": str(self.deposit_buy_mint),
            "deposit_sell_mint": str(self.deposit_sell_mint),
            "quote_underlying": str(self.quote_underlying),
        }

    @classmethod
    def from_json(cls, obj: ProductCommonJSON) -> "ProductCommon":
        return cls(
            underlying=list(map(lambda item: PublicKey(item), obj["underlying"])),
            maturity=obj["maturity"],
            deposit_buy_mint=PublicKey(obj["deposit_buy_mint"]),
            deposit_sell_mint=PublicKey(obj["deposit_sell_mint"]),
            quote_underlying=PublicKey(obj["quote_underlying"]),
        )
