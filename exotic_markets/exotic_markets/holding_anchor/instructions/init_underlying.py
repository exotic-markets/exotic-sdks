from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class InitUnderlyingAccounts(typing.TypedDict):
    owner: PublicKey
    admin_data: PublicKey
    underlying: PublicKey
    base_mint: PublicKey
    quote_mint: PublicKey
    base_oracle: PublicKey
    quote_oracle: PublicKey


def init_underlying(
    accounts: InitUnderlyingAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["underlying"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["base_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["quote_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["base_oracle"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["quote_oracle"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xf6\xf9M\x007\x99P\xe0"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
