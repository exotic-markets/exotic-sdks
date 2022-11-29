from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class UpdateHoldingArgs(typing.TypedDict):
    args: types.update_holding_args.UpdateHoldingArgs


layout = borsh.CStruct("args" / types.update_holding_args.UpdateHoldingArgs.layout)


class UpdateHoldingAccounts(typing.TypedDict):
    admin: PublicKey
    admin_data: PublicKey
    holding_data: PublicKey


def update_holding(
    args: UpdateHoldingArgs,
    accounts: UpdateHoldingAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xd7\xf6\x91L\x08[\xc6\x8e"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
