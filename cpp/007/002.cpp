int main()
{
    std::vector<int> vi;
    for (int i = 0; i < 10; i++)
    {
        vi.push_back(i);
    }

    for (std::size_t i = 0; i < vi.size(); i++)
    {
        std::cout << vi.at(i) << std::endl;
    }
}