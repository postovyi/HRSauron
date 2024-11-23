import asyncio

import aiohttp
import base64
from typing import Any
from app.config import settings


class GitHubService:
    def __init__(self):
        self.base_url = settings.gh.GITHUB_API_URL
        self.headers = {}
        if settings.gh.GITHUB_API_KEY:
            self.headers['Authorization'] = f'token {settings.gh.GITHUB_API_KEY}'

    async def get_default_branch(self, session: aiohttp.ClientSession, repo_full_name: str) -> str:
        repo_url = f'{self.base_url}/repos/{repo_full_name}'
        async with session.get(repo_url) as response:
            response.raise_for_status()
            data = await response.json()
            return data.get('default_branch', 'master')

    async def get_repo_tree(self, session: aiohttp.ClientSession, repo_full_name: str, branch: str) -> list[dict[str, Any]]:
        tree_url = f'{self.base_url}/repos/{repo_full_name}/git/trees/{branch}?recursive=1'
        async with session.get(tree_url) as response:
            response.raise_for_status()
            data = await response.json()
            return data.get('tree', [])

    async def get_file_content(self, session: aiohttp.ClientSession, repo_full_name: str, path: str) -> str | None:
        content_url = f'{self.base_url}/repos/{repo_full_name}/contents/{path}'
        async with session.get(content_url) as response:
            response.raise_for_status()
            data = await response.json()
            if data.get('encoding') == 'base64':
                content = base64.b64decode(data['content']).decode('utf-8', errors='ignore')
                return content
            return None

    async def get_repo_files(self, repo_full_name: str) -> dict[str, str]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            default_branch = await self.get_default_branch(session, repo_full_name)

            tree = await self.get_repo_tree(session, repo_full_name, default_branch)

            file_paths = [item['path'] for item in tree if item['type'] == 'blob']

            tasks = [self.get_file_content(session, repo_full_name, path) for path in file_paths]
            contents = await asyncio.gather(*tasks, return_exceptions=True)

            files = {}
            for path, content in zip(file_paths, contents):
                if isinstance(content, Exception):
                    files[path] = None
                else:
                    files[path] = content

            return files


gh_service = GitHubService()
