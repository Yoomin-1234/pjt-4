import requests
import json
import os

from openai import OpenAI


# 한국어 위키피디아 API 주소
WIKIPEDIA_API_URL = "https://ko.wikipedia.org/w/api.php"

# Wikimedia API 요청 시 클라이언트 식별 정보 전달
HEADERS = {
    "User-Agent": "MyDjangoProject/1.0 (student project)"
}


def search_author_from_wikipedia(author_name):
    # 1. 위키피디아에서 작가 이름 검색
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": author_name,
        "format": "json",
        "utf8": 1,
    }

    search_response = requests.get(
        WIKIPEDIA_API_URL,
        params=search_params,
        headers=HEADERS,
        timeout=10,
    )
    search_response.raise_for_status()

    search_results = (
        search_response.json()
        .get("query", {})
        .get("search", [])
    )

    # 검색 결과가 없는 경우
    if not search_results:
        return {
            "title": author_name,
            "extract": "",
            "image_url": "",
        }

    # 첫 번째 검색 결과의 문서 제목 사용
    page_title = search_results[0]["title"]

    # 2. 문서의 설명과 이미지 조회
    detail_params = {
        "action": "query",
        "prop": "extracts|pageimages",
        "titles": page_title,
        "exintro": 1,
        "explaintext": 1,
        "piprop": "original",
        "format": "json",
        "redirects": 1,
    }

    detail_response = requests.get(
        WIKIPEDIA_API_URL,
        params=detail_params,
        headers=HEADERS,
        timeout=10,
    )
    detail_response.raise_for_status()

    pages = (
        detail_response.json()
        .get("query", {})
        .get("pages", {})
    )

    if not pages:
        return {
            "title": page_title,
            "extract": "",
            "image_url": "",
        }

    page = next(iter(pages.values()))

    # 3. 필요한 정보만 반환
    return {
        "title": page.get("title", page_title),
        "extract": page.get("extract", ""),
        "image_url": (
            page.get("original", {}).get("source", "")
        ),
    }




def generate_author_information(author_name, wikipedia_data):
    """
    작가 이름과 위키백과 정보를 바탕으로
    작가 소개 및 대표 작품을 생성한다.
    """

    # 1. API 키 가져오기
    api_key = os.environ.get("GMS_API_KEY")

    if not api_key:
        raise ValueError(
            "GMS_API_KEY가 설정되지 않았습니다."
        )

    # 2. OpenAI 클라이언트 생성
    # base_url을 지정하지 않으면 OpenAI 기본 API 주소를 사용한다.
    client = client = OpenAI(
        api_key=api_key,
        base_url="https://gms.ssafy.io/gmsapi/api.openai.com/v1",
)
    # 3. AI에게 전달할 프롬프트 작성
    prompt = f"""
다음 작가에 대한 정보를 작성해 주세요.

작가 이름:
{author_name}

Wikipedia 검색 정보:
{wikipedia_data.get("extract", "")}

반드시 아래 JSON 형식으로만 응답하세요.

{{
    "author_info": "작가에 대한 객관적인 설명",
    "author_works": [
        "대표 작품 1",
        "대표 작품 2",
        "대표 작품 3"
    ]
}}

주의사항:
- 확인되지 않은 내용을 사실처럼 단정하지 마세요.
- 작가 소개는 한국어로 작성하세요.
- 대표 작품은 문자열 배열로 반환하세요.
- JSON 이외의 설명이나 Markdown은 출력하지 마세요.
"""

    # 4. AI API 호출
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {
                "role": "system",
                "content": (
                    "당신은 도서 및 작가 정보를 정리하는 도우미입니다."
                ),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )

    # 5. AI 응답 가져오기
    message = response.choices[0].message.content

    if not message:
        raise ValueError("AI가 빈 응답을 반환했습니다.")

    content = message.strip()

    # 6. Markdown 코드 블록 제거
    if content.startswith("```json"):
        content = content.removeprefix("```json")
    elif content.startswith("```"):
        content = content.removeprefix("```")

    content = content.removesuffix("```").strip()

    # 7. JSON 문자열을 Python 딕셔너리로 변환
    result = json.loads(content)

    author_info = result.get("author_info", "")
    author_works = result.get("author_works", [])

    # 8. 반환 데이터 형식 확인
    if not isinstance(author_info, str):
        author_info = str(author_info)

    if not isinstance(author_works, list):
        author_works = []

    author_works = [
        str(work).strip()
        for work in author_works
        if str(work).strip()
    ]

    # 9. 결과 반환
    return {
        "author_info": author_info,
        "author_works": author_works,
    }

def create_author_metadata(author_name):
    wikipedia_data = search_author_from_wikipedia(author_name)

    ai_data = generate_author_information(
        author_name=author_name,
        wikipedia_data=wikipedia_data,
    )

    return {
        "author_info": ai_data.get("author_info", ""),
        "author_works": ai_data.get("author_works", []),
        "author_image_url": wikipedia_data.get("image_url", ""),
    }