import httpx

from app.exceptions import SearchEngineError, SearchEngineUnavailableError


class SearchClient:
    """Talks to the Search Engine service over HTTP."""

    def __init__(self, base_url: str, api_key: str, timeout: float = 30) -> None:
        headers = {"X-API-Key": api_key} if api_key else {}
        self._client = httpx.Client(
            base_url=base_url,
            headers=headers,
            timeout=timeout,
        )

    def _request(self, method: str, path: str, **kwargs) -> dict:
        """One place for sending requests and turning failures into our own errors."""
        try:
            response = self._client.request(method, path, **kwargs)
        except (httpx.ConnectError, httpx.TimeoutException) as exc:
            raise SearchEngineUnavailableError(...) from exc

        if response.status_code >= 400:
            # FastAPI puts the reason in {"detail": ...}; it can be a string OR a list

            try :
                detail = response.json().get("detail",response.text)

            except ValueError:
                detail = response.text   
            raise SearchEngineError(f"Search Engine returned {response.status_code}: {detail}")

        return response.json()

    def health(self) -> bool:
        
        try:

            self._request("GET","/health")

            return True

        except (SearchEngineError, SearchEngineUnavailableError):
            return False

    def index_document(self, document_id: str, file_name: str, text: str) -> dict:
        
        payload = {"document_id":document_id,"file_name":file_name,"text":text}

        return self._request("POST","/documents",json=payload,timeout=120)

    def search(self, query: str, top_k: int = 3, document_ids: list[str] | None = None) -> list[dict]:
        # POST /search; return only the "results" list
        payload = {"query":query,"top_k":top_k}

        if document_ids is not None:
            payload["document_ids"] = document_ids
        
        response = self._request("POST","/search",json=payload)

        return response.get("results", [])

    def close(self) -> None:
        self._client.close()