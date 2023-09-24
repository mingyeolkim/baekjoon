while 1:
    try:
        print(input())
    except EOFError:
        break


#input()은 EOF를 받을 때 EOFError를 일으키지만 sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴을 한다.
#만약에 sys.stdin.readline 함수를 사용하고 싶다면, EOFError를 발생시키지 않고 EOF를 빈 문자열로 받는 특성을 이용해 if 문으로 확인하는 식으로 코드를 작성하면 될 것이다. 그 코드는 다음과 같다.