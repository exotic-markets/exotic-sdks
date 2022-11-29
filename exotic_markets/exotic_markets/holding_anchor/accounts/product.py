import typing
from dataclasses import dataclass
from solana.publickey import PublicKey
from solana.rpc.async_api import AsyncClient
from solana.rpc.commitment import Commitment
import borsh_construct as borsh
from anchorpy.coder.accounts import ACCOUNT_DISCRIMINATOR_SIZE
from anchorpy.error import AccountInvalidDiscriminator
from anchorpy.utils.rpc import get_multiple_accounts
from anchorpy.borsh_extension import BorshPubkey
from ..program_id import PROGRAM_ID
from .. import types


class ProductJSON(typing.TypedDict):
    owner: str
    common_data: types.product_common.ProductCommonJSON
    specific_data: types.specific_product.SpecificProductJSON


@dataclass
class Product:
    discriminator: typing.ClassVar = b"fL7\xfb&I\xe0\xe5"
    layout: typing.ClassVar = borsh.CStruct(
        "owner" / BorshPubkey,
        "common_data" / types.product_common.ProductCommon.layout,
        "specific_data" / types.specific_product.layout,
    )
    owner: PublicKey
    common_data: types.product_common.ProductCommon
    specific_data: types.specific_product.SpecificProductKind

    @classmethod
    async def fetch(
        cls,
        conn: AsyncClient,
        address: PublicKey,
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.Optional["Product"]:
        resp = await conn.get_account_info(address, commitment=commitment)
        info = resp.value
        if info is None:
            return None
        if info.owner != program_id.to_solders():
            raise ValueError("Account does not belong to this program")
        bytes_data = info.data
        return cls.decode(bytes_data)

    @classmethod
    async def fetch_multiple(
        cls,
        conn: AsyncClient,
        addresses: list[PublicKey],
        commitment: typing.Optional[Commitment] = None,
        program_id: PublicKey = PROGRAM_ID,
    ) -> typing.List[typing.Optional["Product"]]:
        infos = await get_multiple_accounts(conn, addresses, commitment=commitment)
        res: typing.List[typing.Optional["Product"]] = []
        for info in infos:
            if info is None:
                res.append(None)
                continue
            if info.account.owner != program_id:
                raise ValueError("Account does not belong to this program")
            res.append(cls.decode(info.account.data))
        return res

    @classmethod
    def decode(cls, data: bytes) -> "Product":
        if data[:ACCOUNT_DISCRIMINATOR_SIZE] != cls.discriminator:
            raise AccountInvalidDiscriminator(
                "The discriminator for this account is invalid"
            )
        dec = Product.layout.parse(data[ACCOUNT_DISCRIMINATOR_SIZE:])
        return cls(
            owner=dec.owner,
            common_data=types.product_common.ProductCommon.from_decoded(
                dec.common_data
            ),
            specific_data=types.specific_product.from_decoded(dec.specific_data),
        )

    def to_json(self) -> ProductJSON:
        return {
            "owner": str(self.owner),
            "common_data": self.common_data.to_json(),
            "specific_data": self.specific_data.to_json(),
        }

    @classmethod
    def from_json(cls, obj: ProductJSON) -> "Product":
        return cls(
            owner=PublicKey(obj["owner"]),
            common_data=types.product_common.ProductCommon.from_json(
                obj["common_data"]
            ),
            specific_data=types.specific_product.from_json(obj["specific_data"]),
        )
