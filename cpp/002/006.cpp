int main()
{
    auto print_two = [](auto x, auto y) {
        std::cout << x << " "s << y << "\n"s;
    };

    print_two(1, 2);
    print_two("Hello?", 18964);
}