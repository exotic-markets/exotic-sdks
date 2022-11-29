from __future__ import annotations
import typing
from solana.publickey import PublicKey
from solana.system_program import SYS_PROGRAM_ID
from solana.sysvar import SYSVAR_RENT_PUBKEY
from spl.token.constants import TOKEN_PROGRAM_ID
from solana.transaction import TransactionInstruction, AccountMeta
import borsh_construct as borsh
from ..program_id import PROGRAM_ID


class PlaceBidArgs(typing.TypedDict):
    amount: int


layout = borsh.CStruct("amount" / borsh.U64)


class PlaceBidAccounts(typing.TypedDict):
    user: PublicKey
    admin_data: PublicKey
    holding_data: PublicKey
    bid_data: PublicKey
    bid_token_acc: PublicKey
    management_acc: PublicKey
    source_token_acc: PublicKey
    source_token_mint: PublicKey
    authority_ai: PublicKey


def place_bid(
    args: PlaceBidArgs,
    accounts: PlaceBidAccounts,
    program_id: PublicKey = PROGRAM_ID,
    remaining_accounts: typing.Optional[typing.List[AccountMeta]] = None,
) -> TransactionInstruction:
    keys: list[AccountMeta] = [
        AccountMeta(pubkey=accounts["user"], is_signer=True, is_writable=True),
        AccountMeta(pubkey=accounts["admin_data"], is_signer=False, is_writable=False),
        AccountMeta(pubkey=accounts["holding_data"], is_signer=False, is_writable=True),
        AccountMeta(pubkey=accounts["bid_data"], is_signer=False, is_writable=True),
        AccountMeta(
            pubkey=accounts["bid_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["management_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["source_token_acc"], is_signer=False, is_writable=True
        ),
        AccountMeta(
            pubkey=accounts["source_token_mint"], is_signer=False, is_writable=False
        ),
        AccountMeta(
            pubkey=accounts["authority_ai"], is_signer=False, is_writable=False
        ),
        AccountMeta(pubkey=TOKEN_PROGRAM_ID, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYSVAR_RENT_PUBKEY, is_signer=False, is_writable=False),
        AccountMeta(pubkey=SYS_PROGRAM_ID, is_signer=False, is_writable=False),
    ]
    if remaining_accounts is not None:
        keys += remaining_accounts
    identifier = b"\xeeM\x94[\xc8\x97\\\x92"
    encoded_args = layout.build(
        {
            "amount": args["amount"],
        }
    )
    data = identifier + encoded_args
    return TransactionInstruction(keys, program_id, data)
