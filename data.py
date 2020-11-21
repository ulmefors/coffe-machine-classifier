import os
import requests
from typing import Sequence

from path import Path
import fastai.vision.all as V
from fastai.vision.all import L

# Bing configuration
AZURE_SEARCH_KEY = os.environ['AZURE_SEARCH_KEY']
BING_API_ENDPOINT = 'https://api.bing.microsoft.com/v7.0/images/search'


def search_images_bing(key: str, term: str) -> L:
    headers = {'Ocp-Apim-Subscription-Key': key}
    params = {'q': term, 'textDecorations': True, 'textFormat': 'HTML'}
    response = requests.get(BING_API_ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    search_results = L(response.json()['value'])
    return search_results


def create_dataset(path: Path, categories: Sequence[str]) -> None:
    if not path.exists():
        for category in categories:
            dest = (path/category)
            os.makedirs(dest, exist_ok=True)
            results = search_images_bing(AZURE_SEARCH_KEY, f'{category}'.replace('-', ' '))
            V.download_images(dest, urls=results.attrgot('contentUrl'))


def remove_failed_images(path: Path) -> L:
    image_paths = V.get_image_files(path)
    failed_images = V.verify_images(image_paths)
    return failed_images.map(Path.unlink)
