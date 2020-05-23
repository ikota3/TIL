int main()
{
    auto print = [](std::size_t s) {
        std::cout << s << std::endl;
    };

    print(sizeof(char));
    print(sizeof(short));
    print(sizeof(int));
    print(sizeof(long));
    print(sizeof(long long));
}