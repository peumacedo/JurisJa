from pathlib import Path
from bs4 import BeautifulSoup
import pytest

@pytest.fixture(scope="module")
def soup():
    html_path = Path(__file__).resolve().parents[1] / "index.html"
    html = html_path.read_text(encoding="utf-8")
    return BeautifulSoup(html, "html.parser")

def test_title_presence(soup):
    assert soup.title is not None and soup.title.get_text(strip=True), "index.html deve conter uma tag <title>"


def test_no_button_inside_anchor(soup):
    for anchor in soup.find_all("a"):
        assert not anchor.find("button"), "<button> não deve estar dentro de <a>"
