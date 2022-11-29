import typing
from dataclasses import dataclass
from construct import Construct
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID
from .. import types


class HoldingJSON(typing.TypedDict):
    owner: str
    end_collection: int
    start_auction: int
    end_auction: int
    deposit_buy_mint: str
    deposit_sell_mint: str
    authority_bump: int
    deposit_buy_bump: int
    deposit_sell_bump: int
    secondary_buy_mint_bump: int
    secondary_sell_mint_bump: int
    possible_order_direction: types.order_possible_direction.OrderPossibleDirectionJSON
    highest_bid_pubkey: str
    highest_bid_amount: int
    total_buy_amount: int
    total_sell_amount: int
    remaining_orders_amount: int
    remaining_bid_count: int
    product: str
    product_expiry: int
    initial_spot_level: typing.Optional[list[int]]
    expiry_spot_level: typing.Optional[list[int]]
    strike: typing.Optional[list[int]]
    bidder_deposit_amount: typing.Optional[int]
    deposit_buy_payoff: typing.Optional[int]
    deposit_sell_payoff: typing.Optional[int]
    max_total_deposit: typing.Optional[int]
    max_deposit_per_user: typing.Optional[int]
    min_deposit_per_user: int
    est_yield: int
    min_yield: int
    min_bid_increment: int
    init_day: int
    bump: int
    risk_level: int


@dataclass
class Holding:
    discriminator: typing.ClassVar = b"\x17`@\xfa\xeb\xbf\x00\x90"
    layout: typing.ClassVar = borsh.CStruct(
        "owner" / BorshPubkey,
        "end_collection" / borsh.U64,
        "start_auction" / borsh.U64,
        "end_auction" / borsh.U64,
        "deposit_buy_mint" / BorshPubkey,
        "deposit_sell_mint" / BorshPubkey,
        "authority_bump" / borsh.U8,
        "deposit_buy_bump" / borsh.U8,
        "deposit_sell_bump" / borsh.U8,
        "secondary_buy_mint_bump" / borsh.U8,
        "secondary_sell_mint_bump" / borsh.U8,
        "possible_order_direction" / types.order_possible_direction.layout,
        "highest_bid_pubkey" / BorshPubkey,
        "highest_bid_amount" / borsh.U64,
        "total_buy_amount" / borsh.U64,
        "total_sell_amount" / borsh.U64,
        "remaining_orders_amount" / borsh.U64,
        "remaining_bid_count" / borsh.U64,
        "product" / BorshPubkey,
        "product_expiry" / borsh.U64,
        "initial_spot_level"
        / borsh.Option(borsh.Vec(typing.cast(Construct, borsh.U64))),
        "expiry_spot_level"
        / borsh.Option(borsh.Vec(typing.cast(Construct, borsh.U64))),
        "strike" / borsh.Option(borsh.Vec(typing.cast(Construct, borsh.U64))),
        "bidder_deposit_amount" / borsh.Option(borsh.U64),
        "deposit_buy_payoff" / borsh.Option(borsh.U64),
        "deposit_sell_payoff" / borsh.Option(borsh.U64),
        "max_total_deposit" / borsh.Option(borsh.U64),
        "max_deposit_per_user" / borsh.Option(borsh.U64),
        "min_deposit_per_user" / borsh.U64,
        "est_yield" / borsh.U64,
        "min_yield" / borsh.U64,
        "min_bid_increment" / borsh.U64,
        "init_day" / borsh.U64,
        "bump" / borsh.U8,
        "risk_level" / borsh.U8,
    )
    owner: PublicKey
    end_collection: int
    start_auction: int
    end_auction: int
    deposit_buy_mint: PublicKey
    deposit_sell_mint: PublicKey
    authority_bump: int
    deposit_buy_bump: int
    deposit_sell_bump: int
    secondary_buy_mint_bump: int
    secondary_sell_mint_bump: int
    possible_order_direction: types.order_possible_direction.OrderPossibleDirectionKind
    highest_bid_pubkey: PublicKey
    highest_bid_amount: int
    total_buy_amount: int
    total_sell_amount: int
    remaining_orders_amount: int
    remaining_bid_count: int
    product: PublicKey
    product_expiry: int
    initial_spot_level: typing.Optional[list[int]]
    expiry_spot_level: typing.Optional[list[int]]
    strike: typing.Optional[list[int]]
    bidder_deposit_amount: typing.Optional[int]
    deposit_buy_payoff: typing.Optional[int]
    deposit_sell_payoff: typing.Optional[int]
    max_total_deposit: typing.Optional[int]
    max_deposit_per_user: typing.Optional[int]
    min_deposit_per_user: int
    est_yield: int
    min_yield: int
    min_bid_increment: int
    init_day: int
    bump: int
    risk_level: int

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.Optional["Holding"]:
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
    ) -> typing.List[typing.Optional["Holding"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Holding"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Holding":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Holding.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            owner=dec.owner,
            end_collection=dec.end_collection,
            start_auction=dec.start_auction,
            end_auction=dec.end_auction,
            deposit_buy_mint=dec.deposit_buy_mint,
            deposit_sell_mint=dec.deposit_sell_mint,
            authority_bump=dec.authority_bump,
            deposit_buy_bump=dec.deposit_buy_bump,
            deposit_sell_bump=dec.deposit_sell_bump,
            secondary_buy_mint_bump=dec.secondary_buy_mint_bump,
            secondary_sell_mint_bump=dec.secondary_sell_mint_bump,
            possible_order_direction=types.order_possible_direction.from_decoded(
                dec.possible_order_direction
            ),
            highest_bid_pubkey=dec.highest_bid_pubkey,
            highest_bid_amount=dec.highest_bid_amount,
            total_buy_amount=dec.total_buy_amount,
            total_sell_amount=dec.total_sell_amount,
            remaining_orders_amount=dec.remaining_orders_amount,
            remaining_bid_count=dec.remaining_bid_count,
            product=dec.product,
            product_expiry=dec.product_expiry,
            initial_spot_level=dec.initial_spot_level,
            expiry_spot_level=dec.expiry_spot_level,
            strike=dec.strike,
            bidder_deposit_amount=dec.bidder_deposit_amount,
            deposit_buy_payoff=dec.deposit_buy_payoff,
            deposit_sell_payoff=dec.deposit_sell_payoff,
            max_total_deposit=dec.max_total_deposit,
            max_deposit_per_user=dec.max_deposit_per_user,
            min_deposit_per_user=dec.min_deposit_per_user,
            est_yield=dec.est_yield,
            min_yield=dec.min_yield,
            min_bid_increment=dec.min_bid_increment,
            init_day=dec.init_day,
            bump=dec.bump,
            risk_level=dec.risk_level,
        )

    def to_json(self) -> HoldingJSON:
        return {
            "owner": str(self.owner),
            "end_collection": self.end_collection,
            "start_auction": self.start_auction,
            "end_auction": self.end_auction,
            "deposit_buy_mint": str(self.deposit_buy_mint),
            "deposit_sell_mint": str(self.deposit_sell_mint),
            "authority_bump": self.authority_bump,
            "deposit_buy_bump": self.deposit_buy_bump,
            "deposit_sell_bump": self.deposit_sell_bump,
            "secondary_buy_mint_bump": self.secondary_buy_mint_bump,
            "secondary_sell_mint_bump": self.secondary_sell_mint_bump,
            "possible_order_direction": self.possible_order_direction.to_json(),
            "highest_bid_pubkey": str(self.highest_bid_pubkey),
            "highest_bid_amount": self.highest_bid_amount,
            "total_buy_amount": self.total_buy_amount,
            "total_sell_amount": self.total_sell_amount,
            "remaining_orders_amount": self.remaining_orders_amount,
            "remaining_bid_count": self.remaining_bid_count,
            "product": str(self.product),
            "product_expiry": self.product_expiry,
            "initial_spot_level": self.initial_spot_level,
            "expiry_spot_level": self.expiry_spot_level,
            "strike": self.strike,
            "bidder_deposit_amount": self.bidder_deposit_amount,
            "deposit_buy_payoff": self.deposit_buy_payoff,
            "deposit_sell_payoff": self.deposit_sell_payoff,
            "max_total_deposit": self.max_total_deposit,
            "max_deposit_per_user": self.max_deposit_per_user,
            "min_deposit_per_user": self.min_deposit_per_user,
            "est_yield": self.est_yield,
            "min_yield": self.min_yield,
            "min_bid_increment": self.min_bid_increment,
            "init_day": self.init_day,
            "bump": self.bump,
            "risk_level": self.risk_level,
        }

    @classmethod
    def from_json(cls, obj: HoldingJSON) -> "Holding":
        return cls(
            owner=PublicKey(obj["owner"]),
            end_collection=obj["end_collection"],
            start_auction=obj["start_auction"],
            end_auction=obj["end_auction"],
            deposit_buy_mint=PublicKey(obj["deposit_buy_mint"]),
            deposit_sell_mint=PublicKey(obj["deposit_sell_mint"]),
            authority_bump=obj["authority_bump"],
            deposit_buy_bump=obj["deposit_buy_bump"],
            deposit_sell_bump=obj["deposit_sell_bump"],
            secondary_buy_mint_bump=obj["secondary_buy_mint_bump"],
            secondary_sell_mint_bump=obj["secondary_sell_mint_bump"],
            possible_order_direction=types.order_possible_direction.from_json(
                obj["possible_order_direction"]
            ),
            highest_bid_pubkey=PublicKey(obj["highest_bid_pubkey"]),
            highest_bid_amount=obj["highest_bid_amount"],
            total_buy_amount=obj["total_buy_amount"],
            total_sell_amount=obj["total_sell_amount"],
            remaining_orders_amount=obj["remaining_orders_amount"],
            remaining_bid_count=obj["remaining_bid_count"],
            product=PublicKey(obj["product"]),
            product_expiry=obj["product_expiry"],
            initial_spot_level=obj["initial_spot_level"],
            expiry_spot_level=obj["expiry_spot_level"],
            strike=obj["strike"],
            bidder_deposit_amount=obj["bidder_deposit_amount"],
            deposit_buy_payoff=obj["deposit_buy_payoff"],
            deposit_sell_payoff=obj["deposit_sell_payoff"],
            max_total_deposit=obj["max_total_deposit"],
            max_deposit_per_user=obj["max_deposit_per_user"],
            min_deposit_per_user=obj["min_deposit_per_user"],
            est_yield=obj["est_yield"],
            min_yield=obj["min_yield"],
            min_bid_increment=obj["min_bid_increment"],
            init_day=obj["init_day"],
            bump=obj["bump"],
            risk_level=obj["risk_level"],
        )
