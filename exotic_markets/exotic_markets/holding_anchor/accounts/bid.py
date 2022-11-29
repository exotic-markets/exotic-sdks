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


class BidJSON(typing.TypedDict):
    bidder: str
    holding: str
    user_token_acc_pubkey: str
    bid_acc_bump: int
    bid_token_acc_bump: int
    bid_amount: int


@dataclass
class Bid:
    discriminator: typing.ClassVar = b"\x8f\xf60\xf5*\x91\xb4X"
    layout: typing.ClassVar = borsh.CStruct(
        "bidder" / BorshPubkey,
        "holding" / BorshPubkey,
        "user_token_acc_pubkey" / BorshPubkey,
        "bid_acc_bump" / borsh.U8,
        "bid_token_acc_bump" / borsh.U8,
        "bid_amount" / borsh.U64,
    )
    bidder: PublicKey
    holding: PublicKey
    user_token_acc_pubkey: PublicKey
    bid_acc_bump: int
    bid_token_acc_bump: int
    bid_amount: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.Optional["Bid"]:
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
    ) -> typing.List[typing.Optional["Bid"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Bid"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Bid":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Bid.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            bidder=dec.bidder,
            holding=dec.holding,
            user_token_acc_pubkey=dec.user_token_acc_pubkey,
            bid_acc_bump=dec.bid_acc_bump,
            bid_token_acc_bump=dec.bid_token_acc_bump,
            bid_amount=dec.bid_amount,
        )

    def to_json(self) -> BidJSON:
        return {
            "bidder": str(self.bidder),
            "holding": str(self.holding),
            "user_token_acc_pubkey": str(self.user_token_acc_pubkey),
            "bid_acc_bump": self.bid_acc_bump,
            "bid_token_acc_bump": self.bid_token_acc_bump,
            "bid_amount": self.bid_amount,
        }

    @classmethod
    def from_json(cls, obj: BidJSON) -> "Bid":
        return cls(
            bidder=PublicKey(obj["bidder"]),
            holding=PublicKey(obj["holding"]),
            user_token_acc_pubkey=PublicKey(obj["user_token_acc_pubkey"]),
            bid_acc_bump=obj["bid_acc_bump"],
            bid_token_acc_bump=obj["bid_token_acc_bump"],
            bid_amount=obj["bid_amount"],
        )
