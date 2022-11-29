from __future__ import annotations
import typing
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class WithdrawUnstartProductAccounts(typing.TypedDict):
    user: PublicKey
    holding_data: PublicKey
    position_data: PublicKey
    product_data: PublicKey
    deposit_token_acc: PublicKey
    user_token_acc: PublicKey
    authority_ai: PublicKey


def withdraw_unstart_product(
    accounts: WithdrawUnstartProductAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["position_data"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["product_data"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["deposit_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["user_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b'?/\x1a\xdb;W"\xea'
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
