def calculator():
    try:
        num1 = float(input("숫자를 입력 :"))
        op = input("연산자 (+, -, *, /) :")
        num2 = float(input("숫자를 입력 :"))

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else :
            print("올바르지 않은 연산자 입니다.")
            return
        print("계산결과 :", result)

    except ValueError:
        print("숫자를 입력하셔야 합니다.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except Exception as e:
        print("예상못한 오류가 발행했습니다.",e)
    finally:
        print("계산기 종료")

calculator()