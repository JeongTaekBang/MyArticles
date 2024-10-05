import re
import requests
from requests.auth import HTTPBasicAuth
import os

# WordPress 인증 정보
USERNAME = "matrix0709"
APPLICATION_PASSWORD = "fRl9 jlm6 s448 WWKo bxh8 W3E0"

# WordPress API 엔드포인트
MEDIA_URL = "https://www.boundlessjourneyofthought.com/wp-json/wp/v2/media"
POST_URL = "https://www.boundlessjourneyofthought.com/wp-json/wp/v2/posts"

# Markdown 파일 경로
MARKDOWN_PATH = "/Users/jeongtaekbang/PycharmProjects/Articles/JN_20241004.md"

# 이미지 파일 경로를 추출하는 정규 표현식
IMAGE_PATTERN = r'!\[.*?\]\((.*?)\)'

def read_markdown_file(filepath):
    """Markdown 파일을 읽어서 내용을 반환"""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def find_image_paths(markdown_content):
    """Markdown 내용에서 모든 이미지 경로를 추출"""
    return re.findall(IMAGE_PATTERN, markdown_content)

def upload_image_to_wordpress(image_path):
    """로컬 이미지를 WordPress에 업로드하고, 성공 시 이미지 ID와 URL을 반환"""
    try:
        with open(image_path, 'rb') as img:
            media_headers = {
                "Content-Disposition": f"attachment; filename={image_path.split('/')[-1]}",
                "Content-Type": "image/png"  # 이미지 형식에 맞게 설정 (image/png 등)
            }
            response = requests.post(MEDIA_URL, headers=media_headers, data=img,
                                     auth=HTTPBasicAuth(USERNAME, APPLICATION_PASSWORD))

            if response.status_code == 201:
                image_id = response.json()["id"]
                image_url = response.json()["source_url"]
                print(f"Image uploaded successfully! ID: {image_id}, URL: {image_url}")
                return image_id, image_url
            else:
                print(f"Failed to upload image: {response.status_code}, {response.text}")
                return None, None
    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return None, None

def remove_first_image_from_markdown(content, image_path):
    """Markdown 내용에서 첫 번째 이미지를 제거"""
    return re.sub(r'!\[.*?\]\(' + re.escape(image_path) + r'\)', '', content, count=1)

def replace_image_in_markdown(content, local_image, image_url):
    """Markdown 파일 내의 로컬 이미지 경로를 업로드된 URL로 대체"""
    return content.replace(local_image, image_url)

def create_post_data(title, content, categories, tags, featured_media_id=None):
    """WordPress에 포스트를 업로드할 데이터 구성"""
    post_data = {
        "title": title,
        "content": content,
        "status": "publish",  # 바로 게시하려면 "publish", 초안으로 저장하려면 "draft"
        "categories": categories,
        "tags": tags
    }
    if featured_media_id:
        post_data["featured_media"] = featured_media_id
    return post_data

def upload_post_to_wordpress(post_data):
    """WordPress에 포스트 업로드"""
    headers = {"Content-Type": "application/json"}
    response = requests.post(POST_URL, json=post_data, auth=HTTPBasicAuth(USERNAME, APPLICATION_PASSWORD),
                             headers=headers)

    if response.status_code == 201:
        print("Post published successfully!")
    else:
        print(f"Failed to publish post: {response.status_code}, {response.text}")

def extract_title_from_filename(filepath):
    """파일 경로에서 파일명을 추출하고 확장자를 제외한 부분을 제목으로 반환"""
    return os.path.splitext(os.path.basename(filepath))[0]

def main():
    # 1. Markdown 파일 읽기
    markdown_content = read_markdown_file(MARKDOWN_PATH)

    # 2. 파일명에서 제목 추출
    title = extract_title_from_filename(MARKDOWN_PATH)

    # 3. 이미지 경로 찾기
    image_paths = find_image_paths(markdown_content)

    # 4. 첫 번째 이미지를 WordPress에 업로드하여 Featured Image로 설정
    featured_image_id = None
    if image_paths:
        first_image = image_paths[0]
        featured_image_id, _ = upload_image_to_wordpress(first_image)

        if featured_image_id:
            # Markdown에서 첫 번째 이미지를 제거
            markdown_content = remove_first_image_from_markdown(markdown_content, first_image)

    # 5. 나머지 이미지 업로드 및 경로 변경
    for local_image in image_paths[1:]:
        _, image_url = upload_image_to_wordpress(local_image)
        if image_url:
            markdown_content = replace_image_in_markdown(markdown_content, local_image, image_url)

    # 6. 포스트 데이터 생성
    category_ids = [25]  # 원하는 카테고리 ID 설정
    tags = [26]  # 원하는 태그 ID 설정
    post_data = create_post_data(title, markdown_content, category_ids, tags, featured_image_id)

    # 7. WordPress에 포스트 업로드
    upload_post_to_wordpress(post_data)

if __name__ == "__main__":
    main()
