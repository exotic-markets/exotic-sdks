import typing
from anchorpy.error import ProgramError


class InvalidAmountTransferred(ProgramError):
    def __init__(self) -> None:
        super().__init__(6000, "The transferred amount is invalid")

    code = 6000
    name = "InvalidAmountTransferred"
    msg = "The transferred amount is invalid"


class InvalidAmountMinted(ProgramError):
    def __init__(self) -> None:
        super().__init__(6001, "The minted amount is invalid")

    code = 6001
    name = "InvalidAmountMinted"
    msg = "The minted amount is invalid"


class InvalidAmountBurned(ProgramError):
    def __init__(self) -> None:
        super().__init__(6002, "The burned amount is invalid")

    code = 6002
    name = "InvalidAmountBurned"
    msg = "The burned amount is invalid"


class ImmutableAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6003, "The account is not mutable")

    code = 6003
    name = "ImmutableAccount"
    msg = "The account is not mutable"


class InvalidOrderDirection(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6004, "The order direction does not match the holding order direction"
        )

    code = 6004
    name = "InvalidOrderDirection"
    msg = "The order direction does not match the holding order direction"


class InsufficientAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6005, "The amount on the TokenAccount is insufficient")

    code = 6005
    name = "InsufficientAmount"
    msg = "The amount on the TokenAccount is insufficient"


class InvalidMint(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6006, "The mint of the account does not match with the holding mint"
        )

    code = 6006
    name = "InvalidMint"
    msg = "The mint of the account does not match with the holding mint"


class OutdatedTimestamp(ProgramError):
    def __init__(self) -> None:
        super().__init__(6007, "The timestamp is outdated")

    code = 6007
    name = "OutdatedTimestamp"
    msg = "The timestamp is outdated"


class ForbiddenBid(ProgramError):
    def __init__(self) -> None:
        super().__init__(
            6008,
            "The bid is forbidden because the order possible direction is buy and sell",
        )

    code = 6008
    name = "ForbiddenBid"
    msg = "The bid is forbidden because the order possible direction is buy and sell"


class OperationFailed(ProgramError):
    def __init__(self) -> None:
        super().__init__(6009, "There was an error in the calculation made")

    code = 6009
    name = "OperationFailed"
    msg = "There was an error in the calculation made"


class InvalidCounter(ProgramError):
    def __init__(self) -> None:
        super().__init__(6010, "The number of the counter is invalid")

    code = 6010
    name = "InvalidCounter"
    msg = "The number of the counter is invalid"


class InvalidAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6011, "The account put in the instruction is invalid")

    code = 6011
    name = "InvalidAccount"
    msg = "The account put in the instruction is invalid"


class NonEmptyAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6012, "The account is not empty")

    code = 6012
    name = "NonEmptyAccount"
    msg = "The account is not empty"


class ProductAddressMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6013, "The address of product mismatch")

    code = 6013
    name = "ProductAddressMismatch"
    msg = "The address of product mismatch"


class InvalidProductEconomics(ProgramError):
    def __init__(self) -> None:
        super().__init__(6014, "The product economics is invalid")

    code = 6014
    name = "InvalidProductEconomics"
    msg = "The product economics is invalid"


class IncorrectUnderlyingCount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6015, "The number of underlying is incorrect")

    code = 6015
    name = "IncorrectUnderlyingCount"
    msg = "The number of underlying is incorrect"


class ExpirySpotDoesNotExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6016, "The spot level at product expiry is not set")

    code = 6016
    name = "ExpirySpotDoesNotExist"
    msg = "The spot level at product expiry is not set"


class StrikeDoesNotExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6017, "The strike is not set")

    code = 6017
    name = "StrikeDoesNotExist"
    msg = "The strike is not set"


class BidderDepositAmountDoesNotExist(ProgramError):
    def __init__(self) -> None:
        super().__init__(6018, "The bidder deposit amount is not set")

    code = 6018
    name = "BidderDepositAmountDoesNotExist"
    msg = "The bidder deposit amount is not set"


class DepositBuyMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6019, "The mint of buying deposit mismatch")

    code = 6019
    name = "DepositBuyMintMismatch"
    msg = "The mint of buying deposit mismatch"


class DepositSellMintMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6020, "The mint of selling deposit mismatch")

    code = 6020
    name = "DepositSellMintMismatch"
    msg = "The mint of selling deposit mismatch"


class PlaceOrderPeriodNotEnded(ProgramError):
    def __init__(self) -> None:
        super().__init__(6021, "The place order period is not ended")

    code = 6021
    name = "PlaceOrderPeriodNotEnded"
    msg = "The place order period is not ended"


class OracleAddressMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6022, "The oracle address mismatch")

    code = 6022
    name = "OracleAddressMismatch"
    msg = "The oracle address mismatch"


class InvalidOracle(ProgramError):
    def __init__(self) -> None:
        super().__init__(6023, "The oracle account is invalid")

    code = 6023
    name = "InvalidOracle"
    msg = "The oracle account is invalid"


class UnderlyingAccountCountMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6024, "The length of underlying and oracle accounts mismatch")

    code = 6024
    name = "UnderlyingAccountCountMismatch"
    msg = "The length of underlying and oracle accounts mismatch"


class ProductAlreadyStarted(ProgramError):
    def __init__(self) -> None:
        super().__init__(6025, "The product is already started")

    code = 6025
    name = "ProductAlreadyStarted"
    msg = "The product is already started"


class ProductNotStarted(ProgramError):
    def __init__(self) -> None:
        super().__init__(6026, "The product is not started")

    code = 6026
    name = "ProductNotStarted"
    msg = "The product is not started"


class IncorrectUnderlying(ProgramError):
    def __init__(self) -> None:
        super().__init__(6027, "The underlying address is incorrect")

    code = 6027
    name = "IncorrectUnderlying"
    msg = "The underlying address is incorrect"


class InvalidBidAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6028, "The bidding amount is invalid")

    code = 6028
    name = "InvalidBidAmount"
    msg = "The bidding amount is invalid"


class ProductDurationNotEnded(ProgramError):
    def __init__(self) -> None:
        super().__init__(6029, "The product duration is not ended")

    code = 6029
    name = "ProductDurationNotEnded"
    msg = "The product duration is not ended"


class ProductAlreadyExpired(ProgramError):
    def __init__(self) -> None:
        super().__init__(6030, "The product is already expired")

    code = 6030
    name = "ProductAlreadyExpired"
    msg = "The product is already expired"


class ProductNotExpired(ProgramError):
    def __init__(self) -> None:
        super().__init__(6031, "The product is not expired")

    code = 6031
    name = "ProductNotExpired"
    msg = "The product is not expired"


class PayoffNotSet(ProgramError):
    def __init__(self) -> None:
        super().__init__(6032, "The product payoff is not set")

    code = 6032
    name = "PayoffNotSet"
    msg = "The product payoff is not set"


class BidNotAccepted(ProgramError):
    def __init__(self) -> None:
        super().__init__(6033, "The bid is not accepted yet")

    code = 6033
    name = "BidNotAccepted"
    msg = "The bid is not accepted yet"


class InvalidMathOperation(ProgramError):
    def __init__(self) -> None:
        super().__init__(6034, "The math operation is invalid")

    code = 6034
    name = "InvalidMathOperation"
    msg = "The math operation is invalid"


class NonZeroRemainingAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6035, "The remaining orders amount is not zero")

    code = 6035
    name = "NonZeroRemainingAmount"
    msg = "The remaining orders amount is not zero"


class ZeroRemainingAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6036, "The remaining orders amount is zero")

    code = 6036
    name = "ZeroRemainingAmount"
    msg = "The remaining orders amount is zero"


class FailedGetBump(ProgramError):
    def __init__(self) -> None:
        super().__init__(6037, "The PDA bumps get function failed")

    code = 6037
    name = "FailedGetBump"
    msg = "The PDA bumps get function failed"


class ExceededMaxDepositAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6038, "The maximum deposit amount is exceeded")

    code = 6038
    name = "ExceededMaxDepositAmount"
    msg = "The maximum deposit amount is exceeded"


class InvalidOrderAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6039, "The order amount is invalid")

    code = 6039
    name = "InvalidOrderAmount"
    msg = "The order amount is invalid"


class UnderlyingOwnerMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6040, "The owner of underlying account mismatch")

    code = 6040
    name = "UnderlyingOwnerMismatch"
    msg = "The owner of underlying account mismatch"


class InvalidAdmin(ProgramError):
    def __init__(self) -> None:
        super().__init__(6041, "The admin key is invalid")

    code = 6041
    name = "InvalidAdmin"
    msg = "The admin key is invalid"


class InvalidManagementAcc(ProgramError):
    def __init__(self) -> None:
        super().__init__(6042, "The managemnet account key is invalid")

    code = 6042
    name = "InvalidManagementAcc"
    msg = "The managemnet account key is invalid"


class ExceededConfidenceInterval(ProgramError):
    def __init__(self) -> None:
        super().__init__(6043, "The oracle confidence interval is exceeded")

    code = 6043
    name = "ExceededConfidenceInterval"
    msg = "The oracle confidence interval is exceeded"


class HoldingOwnerMismatch(ProgramError):
    def __init__(self) -> None:
        super().__init__(6044, "The owner of the holding account is invalid")

    code = 6044
    name = "HoldingOwnerMismatch"
    msg = "The owner of the holding account is invalid"


class InvalidOwner(ProgramError):
    def __init__(self) -> None:
        super().__init__(6045, "The account owner is invalid")

    code = 6045
    name = "InvalidOwner"
    msg = "The account owner is invalid"


class InsufficientSolMainAccount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6046, "Insufficient SOL in main account")

    code = 6046
    name = "InsufficientSolMainAccount"
    msg = "Insufficient SOL in main account"


class InvalidConvertAmount(ProgramError):
    def __init__(self) -> None:
        super().__init__(6047, "The convert amount is invalid")

    code = 6047
    name = "InvalidConvertAmount"
    msg = "The convert amount is invalid"


class InvalidConvertPositionArgs(ProgramError):
    def __init__(self) -> None:
        super().__init__(6048, "The convert position args is invalid")

    code = 6048
    name = "InvalidConvertPositionArgs"
    msg = "The convert position args is invalid"


class InvalidConvertSecondaryDirection(ProgramError):
    def __init__(self) -> None:
        super().__init__(6049, "The convert secondary direction is invalid")

    code = 6049
    name = "InvalidConvertSecondaryDirection"
    msg = "The convert secondary direction is invalid"


class StrikeZero(ProgramError):
    def __init__(self) -> None:
        super().__init__(6050, "Strike is Zero")

    code = 6050
    name = "StrikeZero"
    msg = "Strike is Zero"


CustomError = typing.Union[
    InvalidAmountTransferred,
    InvalidAmountMinted,
    InvalidAmountBurned,
    ImmutableAccount,
    InvalidOrderDirection,
    InsufficientAmount,
    InvalidMint,
    OutdatedTimestamp,
    ForbiddenBid,
    OperationFailed,
    InvalidCounter,
    InvalidAccount,
    NonEmptyAccount,
    ProductAddressMismatch,
    InvalidProductEconomics,
    IncorrectUnderlyingCount,
    ExpirySpotDoesNotExist,
    StrikeDoesNotExist,
    BidderDepositAmountDoesNotExist,
    DepositBuyMintMismatch,
    DepositSellMintMismatch,
    PlaceOrderPeriodNotEnded,
    OracleAddressMismatch,
    InvalidOracle,
    UnderlyingAccountCountMismatch,
    ProductAlreadyStarted,
    ProductNotStarted,
    IncorrectUnderlying,
    InvalidBidAmount,
    ProductDurationNotEnded,
    ProductAlreadyExpired,
    ProductNotExpired,
    PayoffNotSet,
    BidNotAccepted,
    InvalidMathOperation,
    NonZeroRemainingAmount,
    ZeroRemainingAmount,
    FailedGetBump,
    ExceededMaxDepositAmount,
    InvalidOrderAmount,
    UnderlyingOwnerMismatch,
    InvalidAdmin,
    InvalidManagementAcc,
    ExceededConfidenceInterval,
    HoldingOwnerMismatch,
    InvalidOwner,
    InsufficientSolMainAccount,
    InvalidConvertAmount,
    InvalidConvertPositionArgs,
    InvalidConvertSecondaryDirection,
    StrikeZero,
]
CUSTOM_ERROR_MAP: dict[int, CustomError] = {
    6000: InvalidAmountTransferred(),
    6001: InvalidAmountMinted(),
    6002: InvalidAmountBurned(),
    6003: ImmutableAccount(),
    6004: InvalidOrderDirection(),
    6005: InsufficientAmount(),
    6006: InvalidMint(),
    6007: OutdatedTimestamp(),
    6008: ForbiddenBid(),
    6009: OperationFailed(),
    6010: InvalidCounter(),
    6011: InvalidAccount(),
    6012: NonEmptyAccount(),
    6013: ProductAddressMismatch(),
    6014: InvalidProductEconomics(),
    6015: IncorrectUnderlyingCount(),
    6016: ExpirySpotDoesNotExist(),
    6017: StrikeDoesNotExist(),
    6018: BidderDepositAmountDoesNotExist(),
    6019: DepositBuyMintMismatch(),
    6020: DepositSellMintMismatch(),
    6021: PlaceOrderPeriodNotEnded(),
    6022: OracleAddressMismatch(),
    6023: InvalidOracle(),
    6024: UnderlyingAccountCountMismatch(),
    6025: ProductAlreadyStarted(),
    6026: ProductNotStarted(),
    6027: IncorrectUnderlying(),
    6028: InvalidBidAmount(),
    6029: ProductDurationNotEnded(),
    6030: ProductAlreadyExpired(),
    6031: ProductNotExpired(),
    6032: PayoffNotSet(),
    6033: BidNotAccepted(),
    6034: InvalidMathOperation(),
    6035: NonZeroRemainingAmount(),
    6036: ZeroRemainingAmount(),
    6037: FailedGetBump(),
    6038: ExceededMaxDepositAmount(),
    6039: InvalidOrderAmount(),
    6040: UnderlyingOwnerMismatch(),
    6041: InvalidAdmin(),
    6042: InvalidManagementAcc(),
    6043: ExceededConfidenceInterval(),
    6044: HoldingOwnerMismatch(),
    6045: InvalidOwner(),
    6046: InsufficientSolMainAccount(),
    6047: InvalidConvertAmount(),
    6048: InvalidConvertPositionArgs(),
    6049: InvalidConvertSecondaryDirection(),
    6050: StrikeZero(),
}


def from_code(code: int) -> typing.Optional[CustomError]:
    maybe_err = CUSTOM_ERROR_MAP.get(code)
    if maybe_err is None:
        return None
    return maybe_err
