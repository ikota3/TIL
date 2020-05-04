int main()
{
    auto f = []() {
        std::cout << "f is called!\n"s;
        return 0;
        std::cout << "this sentence won't be printed";
    };

    auto result = f();
    std::cout
        << "Return value is: "s << result << "\n"s;
}