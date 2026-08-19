# 프롬프트 관리 프로그램

# 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 기본 프롬프트 데이터 (최소 3개 필수!)
prompts = [
    {
        "title": "블로그 글 작성",
        "content": "당신은 전문 블로거입니다. 주어진 주제로 읽기 쉽고 흥미로운 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "풍경 이미지 생성",
        "content": "아름다운 일몰 풍경, 오렌지빛 하늘, 잔잔한 호수, 사실적인 스타일로 그려주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "친절한 상담사 페르소나",
        "content": "당신은 친절하고 공감 능력이 뛰어난 상담사입니다. 항상 따뜻하게 대화를 이어가주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

# =====================
# 기능 함수들
# =====================

def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    # 제목 입력
    while True:
        title = input("제목을 입력하세요: ").strip()
        if title:
            break
        print("❌ 제목을 입력해주세요!")

    # 내용 입력
    while True:
        content = input("내용을 입력하세요: ").strip()
        if content:
            break
        print("❌ 내용을 입력해주세요!")

    # 카테고리 선택
    print("\n카테고리를 선택하세요:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"  {i}. {cat}")
    print(f"  {len(CATEGORIES)+1}. 직접 입력")

    while True:
        cat_choice = input("번호를 선택하세요: ").strip()
        if cat_choice.isdigit():
            cat_num = int(cat_choice)
            if 1 <= cat_num <= len(CATEGORIES):
                category = CATEGORIES[cat_num - 1]
                break
            elif cat_num == len(CATEGORIES) + 1:
                category = input("카테고리를 직접 입력하세요: ").strip()
                if category:
                    break
                print("❌ 카테고리를 입력해주세요!")
        print("❌ 올바른 번호를 선택하세요!")

    # 프롬프트 저장
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_prompt)
    print(f"\n✅ '{title}' 프롬프트가 추가되었습니다!")


def show_detail(prompt):
    print("\n=== 상세 보기 ===")
    fav = "⭐" if prompt["favorite"] else "없음"
    print(f"제목     : {prompt['title']}")
    print(f"카테고리 : {prompt['category']}")
    print(f"즐겨찾기 : {fav}")
    print(f"내용     :\n{prompt['content']}")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if len(prompts) == 0:
        print("저장된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        fav = "⭐" if p["favorite"] else "  "
        print(f"{i}. {fav} [{p['category']}] {p['title']}")

    # 상세 보기 선택 추가!
    while True:
        choice = input("\n상세 보기할 번호를 선택하세요 (0: 돌아가기): ").strip()
        if choice == "0":
            break
        if choice.isdigit() and 1 <= int(choice) <= len(prompts):
            show_detail(prompts[int(choice) - 1])
            break
        print("❌ 올바른 번호를 선택하세요!")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어를 입력하세요: ").strip()
    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]
    if len(results) == 0:
        print("🔍 검색 결과가 없습니다.")
    else:
        print(f"\n=== 검색 결과 ({len(results)}개) ===")
        for i, p in enumerate(results, 1):
            fav = "⭐" if p["favorite"] else "  "
            print(f"{i}. {fav} [{p['category']}] {p['title']}")


def show_menu():
    print("\n=============================")
    print("    프롬프트 관리 프로그램")
    print("=============================")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록 보기")
    print("3. 프롬프트 검색")
    print("4. 종료")
    print("=============================")


def main():
    print("=== 프롬프트 관리 프로그램 시작 ===")
    while True:
        show_menu()
        choice = input("선택하세요: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            search_prompt()
        elif choice == "4":
            print("프로그램을 종료합니다. 👋")
            break
        else:
            print("❌ 1, 2, 3, 4 중에서 선택하세요!")


if __name__ == "__main__":
    main()