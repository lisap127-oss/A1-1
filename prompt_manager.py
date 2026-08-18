# 프롬프트 관리 프로그램

prompts = []  # 프롬프트를 저장할 리스트

def main():
    print("=== 프롬프트 관리 프로그램 ===")
    
    while True:
        print("\n1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 종료")
        
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
            print("프로그램을 종료합니다.")
            break
            
        else:
            print("❌ 1, 2, 3 중에서 선택하세요!")

if __name__ == "__main__":
    main()