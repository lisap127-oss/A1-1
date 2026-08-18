# 프롬프트 관리 프로그램

prompts = []  # 프롬프트를 저장할 리스트

def search_prompt():
    keyword = input("검색어를 입력하세요: ")
    results = [p for p in prompts if keyword in p]
    if len(results) == 0:
        print("🔍 검색 결과가 없습니다.")
    else:
        print(f"\n=== 검색 결과 ({len(results)}개) ===")
        for i, prompt in enumerate(results, 1):
            print(f"{i}. {prompt}")

def main():
    print("=== 프롬프트 관리 프로그램 ===")

    while True:
        print("\n1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 프롬프트 검색")
        print("4. 종료")

        choice = input("\n선택하세요: ")

        if choice == "1":
            prompt = input("프롬프트를 입력하세요: ")
            prompts.append(prompt)
            print("✅ 추가되었습니다!")

        elif choice == "2":
            if len(prompts) == 0:
                print("저장된 프롬프트가 없습니다.")
            else:
                print("\n=== 저장된 프롬프트 ===")
                for i, prompt in enumerate(prompts, 1):
                    print(f"{i}. {prompt}")

        elif choice == "3":
            search_prompt()

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("❌ 1, 2, 3, 4 중에서 선택하세요!")

if __name__ == "__main__":
    main()