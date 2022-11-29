import typing
from dataclasses import dataclass
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID


class UnderlyingJSON(typing.TypedDict):
    base_mint: str
    quote_mint: str
    base_oracle: str
    quote_oracle: str
    owner: str
    bump: int


@dataclass
class Underlying:
    discriminator: typing.ClassVar = b"\xce\x80\x98Mp\xa4\r\x02"
    layout: typing.ClassVar = borsh.CStruct(
        "base_mint" / BorshPubkey,
        "quote_mint" / BorshPubkey,
        "base_oracle" / BorshPubkey,
        "quote_oracle" / BorshPubkey,
        "owner" / BorshPubkey,
        "bump" / borsh.U8,
    )
    base_mint: PublicKey
    quote_mint: PublicKey
    base_oracle: PublicKey
    quote_oracle: PublicKey
    owner: PublicKey
    bump: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.Optional["Underlying"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id.to_solders():
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[PublicKey],
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["Underlying"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Underlying"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Underlying":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Underlying.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            base_mint=dec.base_mint,
            quote_mint=dec.quote_mint,
            base_oracle=dec.base_oracle,
            quote_oracle=dec.quote_oracle,
            owner=dec.owner,
            bump=dec.bump,
        )

    def to_json(self) -> UnderlyingJSON:
        return {
            "base_mint": str(self.base_mint),
            "quote_mint": str(self.quote_mint),
            "base_oracle": str(self.base_oracle),
            "quote_oracle": str(self.quote_oracle),
            "owner": str(self.owner),
            "bump": self.bump,
        }

    @classmethod
    def from_json(cls, obj: UnderlyingJSON) -> "Underlying":
        return cls(
            base_mint=PublicKey(obj["base_mint"]),
            quote_mint=PublicKey(obj["quote_mint"]),
            base_oracle=PublicKey(obj["base_oracle"]),
            quote_oracle=PublicKey(obj["quote_oracle"]),
            owner=PublicKey(obj["owner"]),
            bump=obj["bump"],
        )
