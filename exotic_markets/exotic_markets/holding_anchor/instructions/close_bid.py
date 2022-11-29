from __future__ import annotations
import typing
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class CloseBidAccounts(typing.TypedDict):
    management_acc: PublicKey
    holding_data: PublicKey
    bid_data: PublicKey
    bid_token_acc: PublicKey
    source_token_acc: PublicKey
    authority_ai: PublicKey
    user: PublicKey


def close_bid(
    accounts: CloseBidAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(
            pubkey=accounts["management_acc"], is_signer=True, is_writable=False
        ),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bid_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["bid_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["source_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xa9\xabBs\xdc\xa8\xe7\x15"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
