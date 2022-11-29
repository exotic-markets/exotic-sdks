from __future__ import annotations
import typing
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class WithdrawAccounts(typing.TypedDict):
    user: PublicKey
    holding_data: PublicKey
    position_data: PublicKey
    product_data: PublicKey
    deposit_buy_token_acc: PublicKey
    deposit_sell_token_acc: PublicKey
    user_buy_token_acc: PublicKey
    user_sell_token_acc: PublicKey
    authority_ai: PublicKey
    exotic_stake_pool: PublicKey
    exotic_stake_fee_state: PublicKey
    member_data: PublicKey
    performance_fee_recipient_buy_token_acc: PublicKey
    performance_fee_recipient_sell_token_acc: PublicKey


def withdraw(
    accounts: WithdrawAccounts,
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
            pubkey=accounts["deposit_buy_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["deposit_sell_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["user_buy_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["user_sell_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["exotic_stake_pool"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["exotic_stake_fee_state"],
            is_signer=False,
            is_writable=False,
        ),
        AccountMeta(pubkey=accounts["member_data"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["performance_fee_recipient_buy_token_acc"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(
            pubkey=accounts["performance_fee_recipient_sell_token_acc"],
            is_signer=False,
            is_writable=True,
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b'\xb7\x12F\x9c\x94m\xa1"'
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
