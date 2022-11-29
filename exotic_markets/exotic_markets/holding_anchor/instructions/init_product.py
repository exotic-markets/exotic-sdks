from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class InitProductArgs(typing.TypedDict):
    args: types.init_product_args.InitProductArgs


layout = borsh.CStruct("args" / types.init_product_args.InitProductArgs.layout)


class InitProductAccounts(typing.TypedDict):
    owner: PublicKey
    admin_data: PublicKey
    product: PublicKey
    deposit_buy_mint: PublicKey
    deposit_sell_mint: PublicKey


def init_product(
    args: InitProductArgs,
    accounts: InitProductAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["product"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["deposit_buy_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["deposit_sell_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xaa\xed\\\xe8\xf0VY\xde"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
