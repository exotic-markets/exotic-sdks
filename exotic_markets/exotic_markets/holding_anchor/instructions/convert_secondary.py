from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class ConvertSecondaryArgs(typing.TypedDict):
    args: types.convert_secondary_args.ConvertSecondaryArgs


layout = borsh.CStruct(
    "args" / types.convert_secondary_args.ConvertSecondaryArgs.layout
)


class ConvertSecondaryAccounts(typing.TypedDict):
    user: PublicKey
    holding_data: PublicKey
    position_data: PublicKey
    user_secondary_token_acc: PublicKey
    secondary_mint: PublicKey
    exotic_stake_pool: PublicKey
    authority_ai: PublicKey


def convert_secondary(
    args: ConvertSecondaryArgs,
    accounts: ConvertSecondaryAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=True),
        AccountMeta(
            pubkey=accounts["holding_data"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["position_data"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["user_secondary_token_acc"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["secondary_mint"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["exotic_stake_pool"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x03\xcex\xe7\xed\x86\xb4G"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
