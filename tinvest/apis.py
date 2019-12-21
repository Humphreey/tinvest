from typing import Optional

from .shemas import (
    SandboxSetCurrencyBalanceRequest,
    SandboxSetPositionBalanceRequest,
    LimitOrderRequest,
    Empty,
    CandleResolution,
    PortfolioResponse,
    OrdersResponse,
    OperationsResponse,
    LimitOrderResponse,
    PortfolioCurrenciesResponse,
    MarketInstrumentListResponse,
    OrderbookResponse,
    CandlesResponse,
    MarketInstrumentResponse,
)


class SandboxApi:
    """Операция в sandbox"""

    def __init__(self, client):
        self._client = client

    def sandbox_register_post(self, **kwargs):
        """POST /sandbox/register Регистрация клиента в sandbox"""
        return self._client.request(
            "POST", "/sandbox/register", response_model=Empty, **kwargs
        )

    def sandbox_currencies_balance_post(
        self, body: SandboxSetCurrencyBalanceRequest, **kwargs
    ):
        """POST /sandbox/currencies/balance Выставление баланса по валютным позициям"""
        kwargs.setdefault("data", body.json(by_alias=True))
        return self._client.request(
            "POST", "/sandbox/currencies/balance", response_model=Empty, **kwargs
        )

    def sandbox_positions_balance_post(
        self, body: SandboxSetPositionBalanceRequest, **kwargs
    ):
        """POST /sandbox/positions/balance Выставление баланса по инструментным позициям"""
        kwargs.setdefault("data", body.json(by_alias=True))
        return self._client.request(
            "POST", "/sandbox/positions/balance", response_model=Empty, **kwargs
        )

    def sandbox_clear_post(self, **kwargs):
        """POST /sandbox/clear Удаление всех позиций"""
        return self._client.request(
            "POST", "/sandbox/clear", response_model=Empty, **kwargs
        )


class OrdersApi:
    """Операции заявок"""

    def __init__(self, client):
        self._client = client

    def orders_get(self, **kwargs):
        """GET /orders Получение списка активных заявок"""
        return self._client.request(
            "GET", "/orders", response_model=OrdersResponse, **kwargs
        )

    def orders_limit_order_post(self, figi: str, body: LimitOrderRequest, **kwargs):
        """POST /orders/limit-order Создание лимитной заявки"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("figi", figi)
        kwargs.setdefault("data", body.json(by_alias=True))
        return self._client.request(
            "POST", "/orders/limit-order", response_model=LimitOrderResponse, **kwargs
        )

    def orders_cancel_post(self, order_id: str, body: Optional[Empty] = None, **kwargs):
        """POST /orders/cancel Отмена заявки"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("orderId", order_id)
        if body:
            kwargs.setdefault("data", body.json(by_alias=True))
        return self._client.request(
            "POST", "/orders/cancel", response_model=Empty, **kwargs
        )


class PortfolioApi:
    """Операции с портфелем пользователя"""

    def __init__(self, client):
        self._client = client

    def portfolio_get(self, **kwargs):
        """GET /portfolio Получение портфеля клиента"""
        return self._client.request(
            "GET", "/portfolio", response_model=PortfolioResponse, **kwargs
        )

    def portfolio_currencies_get(self, **kwargs):
        """GET /portfolio/currencies Получение валютных активов клиента"""
        return self._client.request(
            "GET",
            "/portfolio/currencies",
            response_model=PortfolioCurrenciesResponse,
            **kwargs
        )


class MarketApi:
    """Получении информации по бумагам"""

    def __init__(self, client):
        self._client = client

    def market_stocks_get(self, **kwargs):
        """GET /market/stocks Получение списка акций"""
        return self._client.request(
            "GET",
            "/market/stocks",
            response_model=MarketInstrumentListResponse,
            **kwargs
        )

    def market_bonds_get(self, **kwargs):
        """GET /market/bonds Получение списка облигаций"""
        return self._client.request(
            "GET",
            "/market/bonds",
            response_model=MarketInstrumentListResponse,
            **kwargs
        )

    def market_etfs_get(self, **kwargs):
        """GET /market/etfs Получение списка ETF"""
        return self._client.request(
            "GET", "/market/etfs", response_model=MarketInstrumentListResponse, **kwargs
        )

    def market_currencies_get(self, **kwargs):
        """GET /market/currencies Получение списка валютных пар"""
        return self._client.request(
            "GET",
            "/market/currencies",
            response_model=MarketInstrumentListResponse,
            **kwargs
        )

    def market_orderbook_get(self, figi: str, depth: int, **kwargs):
        """GET /market/orderbook Получение стакана"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("figi", figi)
        params.setdefault("depth", depth)
        return self._client.request(
            "GET", "/market/orderbook", response_model=OrderbookResponse, **kwargs
        )

    def market_candles_get(
        self, figi: str, from_: str, to: str, interval: CandleResolution, **kwargs
    ):
        """GET /market/candles Получение исторических свечей по FIGI"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("figi", figi)
        params.setdefault("from", from_)
        params.setdefault("to", to)
        return self._client.request(
            "GET", "/market/candles", response_model=CandlesResponse, **kwargs
        )

    def market_search_by_figi_get(self, figi: str, **kwargs):
        """GET /market/search/by-figi Получение инструмента по FIGI"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("figi", figi)
        return self._client.request(
            "GET", "/market/search/by-figi", response_model=MarketInstrumentResponse, **kwargs
        )

    def market_search_by_ticker_get(self, ticker: str, **kwargs):
        """GET /market/search/by-ticker Получение инструмента по тикеру"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("ticker", ticker)
        return self._client.request(
            "GET", "/market/search/by-ticker", response_model=MarketInstrumentListResponse, **kwargs
        )


class OperationsApi:
    """Получении информации по операциям"""

    def __init__(self, client):
        self._client = client

    def operations_get(self, from_: str, to: str, figi: Optional[str] = None, **kwargs):
        """GET /operations Получение списка операций"""
        kwargs.setdefault("params", {})
        params = kwargs["params"]
        params.setdefault("from", from_)
        params.setdefault("to", to)
        if figi:
            params.setdefault("figi", figi)
        return self._client.request(
            "GET", "/operations", response_model=OperationsResponse, **kwargs
        )
