from __future__ import annotations
import typing
from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from .. import types
from ..program_id import PROGRAM_ID


class WithdrawSingleDirectionArgs(typing.TypedDict):
    direction: types.order_direction.OrderDirectionKind


layout = borsh.CStruct("direction" / types.order_direction.layout)


class WithdrawSingleDirectionAccounts(typing.TypedDict):
    user: PublicKey
    admin: PublicKey
    admin_data: PublicKey
    holding_data: PublicKey
    position_data: PublicKey
    product_data: PublicKey
    deposit_token_acc: PublicKey
    user_token_acc: PublicKey
    authority_ai: PublicKey


def withdraw_single_direction(
    args: WithdrawSingleDirectionArgs,
    accounts: WithdrawSingleDirectionAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin"], is_signer=True, is_writable=False),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
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
    identifier = b"'e\xa2l\xe9\xcc\xa1b"
    encoded_args = layout.build(
        {
            "direction": args["direction"].to_encodable(),
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
