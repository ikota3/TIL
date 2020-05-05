int main()
{
    std::cout << std::boolalpha;
    auto print = [](auto condition) {
        std::cout << condition << std::endl;
    };

    // true
    print(true || true);
    // true
    print(true || false);
    // true
    print(false || true);
    // false
    print(false || false);
}