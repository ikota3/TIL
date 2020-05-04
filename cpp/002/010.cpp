int plus_integers(int x, int y)
{
    return x + y;
}

int plus_doubles(double x, double y)
{
    return x + y;
}

std::string plus_strings(std::string x, std::string y)
{
    return x + y;
}

int main()
{
    // 3
    std::cout << plus_integers(1, 2) << "\n"s;
    std::cout << plus_doubles(1.5, 2.5) << "\n"s;
    std::cout << plus_strings("Hello!", "World!") << "\n"s;
}