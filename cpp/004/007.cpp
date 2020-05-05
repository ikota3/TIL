int main()
{
    auto print = [](auto result) {
        std::cout << result << std::endl;
    };

    // 2
    print(true + true);
    // 1
    print(true + false);
    // 1
    print(false + true);
    // 0
    print(false + false);
}