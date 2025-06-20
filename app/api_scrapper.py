import asyncio
from dataclasses import dataclass
from typing import Any

import httpx
from httpx import AsyncHTTPTransport, AsyncClient, Timeout

from app.constants import BASE_URL
from app.dto import CatDataDTO
from app.logger import logger





@dataclass
class AsyncNetScrapper:

    async def get_cats_facts(self) -> list[dict[str, Any]]:
        transport = AsyncHTTPTransport(retries=1)
        timeout = Timeout(timeout=2)
        try:
            async with AsyncClient(transport=transport, timeout=timeout) as client:
                response = await self._async_request(client=client, url=f"{BASE_URL}/facts")

                if not response:
                    return []

                last_page = response["last_page"]

                coros = []
                for page in range(1, last_page + 1):
                    coros.append(self._async_request(client=client, url=f"{BASE_URL}/facts?page={page}"))

                all_cats_facts = await asyncio.gather(*coros)
                cat_facts = []
                for facts_page in all_cats_facts:
                    for fact in facts_page["data"]:
                        cat_facts.append(CatDataDTO(fact=fact["fact"], length=fact["length"]))
                return cat_facts
        except httpx.TimeoutException as error:
            logger.error("time out to web resourse", error=error)
            return []


    def get_data(self):
        return asyncio.run(self.get_cats_facts())

    async def _async_request(self, client: AsyncClient, url: str) -> dict[str, Any] | None:
        response = await client.get(url)
        status = response.status_code
        if status == httpx.codes.OK:
            return response.json()
        else:
            logger.info(f'got response status: {status} for uri: {url}')
            return None
