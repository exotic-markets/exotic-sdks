from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class AcceptBidAccounts(typing.TypedDict):
    signer: PublicKey
    user: PublicKey
    holding_data: PublicKey
    bid_data: PublicKey
    bid_token_acc: PublicKey
    deposit_token_acc: PublicKey
    position_data: PublicKey
    authority_ai: PublicKey


def accept_bid(
    accounts: AcceptBidAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["signer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["user"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bid_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["bid_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["deposit_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["position_data"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xc4\xbf\x01\xe5\x90\xacz\xe3"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
