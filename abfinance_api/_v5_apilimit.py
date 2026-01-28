from ._http_manager import _V5HTTPManager
from .apilimit import ApiLimit


class ApiLimitHTTP(_V5HTTPManager):
    def query(self, **kwargs):
        """Query the API limit information.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{ApiLimit.QUERY}",
            query=kwargs,
            auth=True,
        )

    def query_all(self, **kwargs):
        """Query all API limit information.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{ApiLimit.QUERY_ALL}",
            query=kwargs,
            auth=True,
        )

    def query_cap(self, **kwargs):
        """Query the API limit cap.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{ApiLimit.QUERY_CAP}",
            query=kwargs,
            auth=True,
        )

    def set(self, **kwargs):
        """Set the API limit.

        Returns:
            Request results as dictionary.

        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{ApiLimit.SET}",
            query=kwargs,
            auth=True,
        )
