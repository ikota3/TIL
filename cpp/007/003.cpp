int input();

int main()
{
    std::vector<int> vi;
    int n{};

    while ((n = input()) != 0)
    {
        vi.push_back(n);
    }

    for (std::size_t i = 0; i < vi.size(); i++)
    {
        std::cout << vi.at(i) << std::endl;
    }
}

int input()
{
    int n{};
    std::cin >> n;
    return n;
}