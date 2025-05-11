import re
import os
from typing import Literal
from typing_extensions import override


from wxabc.logger import logger
import requests


class ContentFetcher:
    timeout = (3, 10)

    def __init__(self) -> None:
        self._session = requests.Session()

    def _fetch_content(self, url: str, method: Literal["GET", "POST", "HEAD"], **kwargs) -> dict:
        resp = self._session.request(method, url, **kwargs)
        logger.debug(f"{method} {url} response: {resp}")
        resp.raise_for_status()
        return resp.json()

    def fetch_content(self, url: str):
        resp = self._fetch_content(url, "GET")
        logger.info(resp)


class GithubContentFetcher(ContentFetcher):
    """
    支持目录或文件
    - get a tree: https://docs.github.com/en/rest/git/trees?apiVersion=2022-11-28#get-a-tree
    - get content: https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28
    """

    url_pattern: re.Pattern = re.compile(r"github\.com\/([^\/]+)\/([^\/]+)\/(blob|tree)\/([^\/]+)\/(.*)")

    def __init__(self) -> None:
        super().__init__()
        self._api_key = os.getenv("GITHUB_API_KEY", "")
        if not self._api_key:
            logger.warning("GITHUB_API_KEY is not set, some of the github api might not be accessed.")

    @override
    def fetch_content(self, url: str):
        match = re.search(self.url_pattern, url)
        if not match:
            raise Exception(f"url({url}) pattern not matched")
        user = match.group(1)
        repo = match.group(2)
        is_tree = match.group(3) == "tree"
        branch = match.group(4)
        file_path = match.group(5)
        kwargs = {"headers": {"Accept": "application/vnd.github.object+json"}}
        if is_tree:
            # 如果超过比较大的数量,还需通过git_tree的方式获取,但是有个缺陷是不能提前通过tree_sha去定位
            # api_url = f"https://api.github.com/repos/{user}/{repo}/git/trees/{branch}"
            # kwargs["params"] = {"recursive": 1}
            api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{file_path}"
            kwargs["params"] = {"ref": branch}
        else:
            api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{file_path}"
            kwargs["params"] = {"ref": branch}
        if self._api_key:
            kwargs["headers"]["Authorization"] = f"token {self._api_key}"
        result = self._fetch_content(api_url, "GET", **kwargs)
        logger.info(result)
        if is_tree:
            api_url = result["git_url"]
            tree_objs = self._fetch_content(api_url, "GET")
            logger.info(tree_objs)
        else:
            logger.info(result)


logger.info("test info")
logger.error("test error")
