from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
from ..program_id import PROGRAM_ID


class FundManagementAccAccounts(typing.TypedDict):
    payer: PublicKey
    admin_data: PublicKey
    management_acc: PublicKey


def fund_management_acc(
    accounts: FundManagementAccAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["payer"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(
            pubkey=accounts["management_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xef\x10{_\x9f\xff\x19\x15"
    encoded_args = b""
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
