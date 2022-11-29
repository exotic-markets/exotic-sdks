from __future__ import annotations
import typing
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class CloseHoldingAccounts(typing.TypedDict):
    owner: PublicKey
    holding_data: PublicKey
    deposit_buy_token_acc: PublicKey
    deposit_sell_token_acc: PublicKey
    remaining_buy_token_acc: PublicKey
    remaining_sell_token_acc: PublicKey
    authority_ai: PublicKey


def close_holding(
    accounts: CloseHoldingAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["owner"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["deposit_buy_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["deposit_sell_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["remaining_buy_token_acc"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["remaining_sell_token_acc"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xd7<\x01n\x04Y\xd4\x8d"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
