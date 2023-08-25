from pydantic import ValidationError, validate_call


@validate_call
def repeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
    b = s.encode()
    return separator.join(b for _ in range(count))


if __name__ == '__main__':
    # TEST 1 ------------------------------------------------------------------------------------------------------------------
    a = repeat('hello', 3)
    print(a)
    #> b'hellohellohello'

    # TEST 2 ------------------------------------------------------------------------------------------------------------------
    b = repeat('x', '4', separator=' ')
    print(b)
    #> b'x x x x'

    # TEST 3 ------------------------------------------------------------------------------------------------------------------
    try:
        c = repeat('hello', 'wrong')
    except ValidationError as exc:
        print(exc)
    