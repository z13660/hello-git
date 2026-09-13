def greet(name: str = "world") -> str:
    """返回一句问候语。"""
    return f"Hello, {name}!"


def main() -> None:
    print(greet("GitHub"))
    print("This project was created with the help of DeepSeek Harness.")


if __name__ == "__main__":
    main()
