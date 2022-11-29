from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class ExpireProductOverrideArgs(typing.TypedDict):
    args: types.expire_product_override_args.ExpireProductOverrideArgs


layout = borsh.CStruct(
    "args" / types.expire_product_override_args.ExpireProductOverrideArgs.layout
)


class ExpireProductOverrideAccounts(typing.TypedDict):
    owner: PublicKey
    admin_data: PublicKey
    holding_data: PublicKey
    product_data: PublicKey


def expire_product_override(
    args: ExpireProductOverrideArgs,
    accounts: ExpireProductOverrideAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["product_data"], is_signer=False, is_writable=False
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"w4Hb\xcb\x8a\xb3l"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
