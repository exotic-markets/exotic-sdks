from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY
from spl.token.constants import TOKEN_PROGRAM_ID, ASSOCIATED_TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class ConvertPositionArgs(typing.TypedDict):
    args: types.convert_position_args.ConvertPositionArgs


layout = borsh.CStruct("args" / types.convert_position_args.ConvertPositionArgs.layout)


class ConvertPositionAccounts(typing.TypedDict):
    user: PublicKey
    holding_data: PublicKey
    position_data: PublicKey
    user_secondary_token_acc: PublicKey
    secondary_mint: PublicKey
    authority_ai: PublicKey


def convert_position(
    args: ConvertPositionArgs,
    accounts: ConvertPositionAccounts,
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
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=ASSOCIATED_TOKEN_PROGRAM_ID, is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=SYSVAR_RENT_PUBKEY, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\x8f\xfbW\xb4\x85pQ\x80"
    encoded_args = layout.build(
        {
            "args": args["args"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
