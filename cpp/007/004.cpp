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
        for (std::size_t j = i + 1; j < vi.size(); j++)
        {
            int tmp{};
            if (vi.at(i) > vi.at(j))
            {
                tmp = vi.at(i);
                vi.at(i) = vi.at(j);
                vi.at(j) = tmp;
            }
        }
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