int main()
{
    auto printTwice = [](auto value) {
        std::cout << value << " "s << value << "\n"s;
    };

    printTwice(5);
}