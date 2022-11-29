from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class InitHoldingArgs(typing.TypedDict):
    args: types.init_holding_args.InitHoldingArgs


layout = borsh.CStruct("args" / types.init_holding_args.InitHoldingArgs.layout)


class InitHoldingAccounts(typing.TypedDict):
    owner: PublicKey
    admin_data: PublicKey
    holding_data: PublicKey
    product_data: PublicKey
    deposit_buy_mint: PublicKey
    deposit_sell_mint: PublicKey
    deposit_buy_token_acc: PublicKey
    deposit_sell_token_acc: PublicKey
    secondary_buy_mint: PublicKey
    secondary_sell_mint: PublicKey
    authority_ai: PublicKey


def init_holding(
    args: InitHoldingArgs,
    accounts: InitHoldingAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["product_data"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["deposit_buy_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["deposit_sell_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["deposit_buy_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["deposit_sell_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["secondary_buy_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["secondary_sell_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYSVAR_RENT_PUBKEY, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xac\x9dS@\xcb\x8f<O"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
