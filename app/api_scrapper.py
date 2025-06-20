import asyncio
import sys
from logging import Logger
from typing import Any

import httpx
from httpx import AsyncHTTPTransport, AsyncClient, Timeout

BASE_URL = "https://catfact.ninja"


def configure_logger() -> Logger:
    try:
        from loguru import logger as loguru_logger

        loguru_logger.remove()
        loguru_logger.add(
            sink=sys.stdout,
            colorize=True,
            level='DEBUG',
            format='<cyan>{time:DD.MM.YYYY HH:mm:ss}</cyan> | <level>{level}</level> | <magenta>{message}</magenta>',
        )
        return loguru_logger  # type: ignore
    except ImportError:
        import logging

        logging_logger = logging.getLogger('main_logger')
        formatter = logging.Formatter(
            datefmt='%Y.%m.%d %H:%M:%S',
            fmt='%(asctime)s | %(levelname)s | func name: %(funcName)s | message: %(message)s',
        )
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(formatter)
        logging_logger.setLevel(logging.INFO)
        logging_logger.addHandler(handler)
        return logging_logger


logger = configure_logger()

class AsyncNetScrapper:

    async def get_cats_facts(self) -> list[dict[str, Any]]:
        transport = AsyncHTTPTransport(retries=1)
        timeout = Timeout(timeout=2)



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
            for facts in all_cats_facts:
                cat_facts.extend(facts["data"])
            return cat_facts

    def run(self):
        return asyncio.run(self.get_cats_facts())

    async def _async_request(self, client: AsyncClient, url: str) -> dict[str, Any] | None:
        response = await client.get(url)
        status = response.status_code
        if status == httpx.codes.OK:
            return response.json()
        else:
            logger.info(f'got response status: {status} for uri: {url}')
            return None


def main() -> None:
    async_net_scrapper = AsyncNetScrapper()
    facts = async_net_scrapper.run()
    print(facts)


main()