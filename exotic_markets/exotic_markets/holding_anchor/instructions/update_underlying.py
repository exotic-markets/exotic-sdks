from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class UpdateUnderlyingAccounts(typing.TypedDict):
    owner: PublicKey
    underlying: PublicKey
    base_mint: PublicKey
    quote_mint: PublicKey
    new_base_oracle: PublicKey
    new_quote_oracle: PublicKey


def update_underlying(
    accounts: UpdateUnderlyingAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["underlying"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["base_mint"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["quote_mint"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["new_base_oracle"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["new_quote_oracle"], is_signer=False, is_writable=False
        ),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xd1\x00M\xa1j \x9d\xe0"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
