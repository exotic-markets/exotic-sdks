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


class PositionJSON(typing.TypedDict):
    user: str
    holding: str
    buy_amount: int
    sell_amount: int
    bump: int


@dataclass
class Position:
    discriminator: typing.ClassVar = b"\xaa\xbc\x8f\xe4z@\xf7\xd0"
    layout: typing.ClassVar = borsh.CStruct(
        "user" / BorshPubkey,
        "holding" / BorshPubkey,
        "buy_amount" / borsh.U64,
        "sell_amount" / borsh.U64,
        "bump" / borsh.U8,
    )
    user: PublicKey
    holding: PublicKey
    buy_amount: int
    sell_amount: int
    bump: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.Optional["Position"]:
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
    ) -> typing.List[typing.Optional["Position"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Position"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Position":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Position.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            user=dec.user,
            holding=dec.holding,
            buy_amount=dec.buy_amount,
            sell_amount=dec.sell_amount,
            bump=dec.bump,
        )

    def to_json(self) -> PositionJSON:
        return {
            "user": str(self.user),
            "holding": str(self.holding),
            "buy_amount": self.buy_amount,
            "sell_amount": self.sell_amount,
            "bump": self.bump,
        }

    @classmethod
    def from_json(cls, obj: PositionJSON) -> "Position":
        return cls(
            user=PublicKey(obj["user"]),
            holding=PublicKey(obj["holding"]),
            buy_amount=obj["buy_amount"],
            sell_amount=obj["sell_amount"],
            bump=obj["bump"],
        )
