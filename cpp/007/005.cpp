int main()
{
    std::vector<int> vi = {8, 3, 7, 4, 2, 9, 3};
    std::size_t size = vi.size();

    std::size_t min = 0;
    for (std::size_t i = 0; i < size; i++)
    {
        if (vi.at(i) < vi.at(min))
        {
            min = i;
        }
    }

    std::cout << vi.at(min);
}