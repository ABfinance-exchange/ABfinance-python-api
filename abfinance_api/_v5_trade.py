from ._http_manager import _V5HTTPManager
from .trade import Trade


class TradeHTTP(_V5HTTPManager):
    def place_order(self, **kwargs):
        """Create an order for spot trading.

        Required args:
            category (string): Product type: spot
            symbol (string): Symbol name
            side (string): Buy, Sell
            orderType (string): Market, Limit
            qty (string): Order quantity

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.PLACE_ORDER}",
            query=kwargs,
            auth=True,
        )

    def amend_order(self, **kwargs):
        """Amend an unfilled or partially filled order.

        Required args:
            category (string): Product type: spot
            symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.AMEND_ORDER}",
            query=kwargs,
            auth=True,
        )

    def cancel_order(self, **kwargs):
        """Cancel an unfilled or partially filled order.

        Required args:
            category (string): Product type: spot
            symbol (string): Symbol name
            orderId (string): Order ID. Either orderId or orderLinkId is required
            orderLinkId (string): User customised order ID. Either orderId or orderLinkId is required

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.CANCEL_ORDER}",
            query=kwargs,
            auth=True,
        )

    def get_open_orders(self, **kwargs):
        """Query unfilled or partially filled orders in real-time.

        Required args:
            category (string): Product type: spot

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Trade.GET_OPEN_ORDERS}",
            query=kwargs,
            auth=True,
        )

    def cancel_all_orders(self, **kwargs):
        """Cancel all open orders.

        Required args:
            category (string): Product type: spot

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.CANCEL_ALL_ORDERS}",
            query=kwargs,
            auth=True,
        )

    def get_order_history(self, **kwargs):
        """Query order history.

        Required args:
            category (string): Product type: spot

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Trade.GET_ORDER_HISTORY}",
            query=kwargs,
            auth=True,
        )

    def place_batch_order(self, **kwargs):
        """Place multiple orders in a single request.

        Required args:
            category (string): Product type: spot
            request (array): Object
            > symbol (string): Symbol name
            > side (string): Buy, Sell
            > orderType (string): Market, Limit
            > qty (string): Order quantity

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.BATCH_PLACE_ORDER}",
            query=kwargs,
            auth=True,
        )

    def amend_batch_order(self, **kwargs):
        """Amend multiple orders in a single request.

        Required args:
            category (string): Product type: spot
            request (array): Object
            > symbol (string): Symbol name
            > orderId (string): Order ID. Either orderId or orderLinkId is required
            > orderLinkId (string): User customised order ID. Either orderId or orderLinkId is required

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.BATCH_AMEND_ORDER}",
            query=kwargs,
            auth=True,
        )

    def cancel_batch_order(self, **kwargs):
        """Cancel multiple orders in a single request.

        Required args:
            category (string): Product type: spot
            request (array): Object
            > symbol (string): Symbol name

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.BATCH_CANCEL_ORDER}",
            query=kwargs,
            auth=True,
        )

    def get_borrow_quota(self, **kwargs):
        """Query the qty and amount of borrowable coins in spot account.

        Required args:
            category (string): Product type: spot
            symbol (string): Symbol name
            side (string): Transaction side. Buy, Sell

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Trade.GET_BORROW_QUOTA}",
            query=kwargs,
            auth=True,
        )

    def set_dcp(self, **kwargs):
        """Set the disconnected cancel all configuration.

        Required args:
            timeWindow (integer): Disconnection timing window time. [10, 300], unit: second

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.SET_DCP}",
            query=kwargs,
            auth=True,
        )

    def get_executions(self, **kwargs):
        """Query users' execution records, sorted by execTime in descending order.

        Required args:
            category (string): Product type: spot

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Trade.GET_EXECUTIONS}",
            query=kwargs,
            auth=True,
        )
