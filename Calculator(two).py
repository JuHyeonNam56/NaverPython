def calculator():
    while True:
        try:
            num1 = float(input("숫자를 입력 : "))
            op = input("연산자 (+, -, *, /) : ")
            num2 = float(input("숫자를 입력 : "))

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2
            else:
                print("올바르지 않은 연산자입니다.")
                continue

            print("계산 결과 :", result)

        except ValueError:
            print("숫자를 입력하셔야 합니다.")
            continue
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
            continue
        except Exception as e:
            print("예상 못한 오류가 발생했습니다:", e)
            continue
        finally:
            print("계산기를 종료하거나 계속 사용하실 수 있습니다.\n")

        again = input("계속 하시겠습니까? (y : 계속, n : 종료): ").lower()
        if again != 'y':
            print("👋 계산기를 종료합니다.")
            break

# 함수 실행
calculator()
