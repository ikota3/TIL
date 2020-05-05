int main()
{
    std::cout << std::boolalpha;
    auto print = [](auto condition) {
        std::cout << condition << std::endl;
    };

    // true
    print(true && true);
    // false
    print(true && false);
    // false
    print(false && false);
    // false
    print(false && true);
}