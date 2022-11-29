from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class ChangeBidArgs(typing.TypedDict):
    args: types.change_bid_args.ChangeBidArgs


layout = borsh.CStruct("args" / types.change_bid_args.ChangeBidArgs.layout)


class ChangeBidAccounts(typing.TypedDict):
    user: PublicKey
    holding_data: PublicKey
    bid_data: PublicKey
    bid_token_acc: PublicKey
    source_token_acc: PublicKey


def change_bid(
    args: ChangeBidArgs,
    accounts: ChangeBidAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bid_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["bid_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["source_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"N\xef;\x1fU\xd5\xf7\x91"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
