int main()
{
    // 選択ソート
    std::vector<int> vi = {8, 3, 7, 4, 2, 9, 3};
    for (std::size_t i = 0; i < vi.size(); i++)
    {
        std::size_t min = i;
        for (std::size_t j = i + 1; j < vi.size(); j++)
        {
            if (vi.at(j) < vi.at(min))
            {
                min = j;
            }
        }
        int tmp = vi.at(i);
        vi.at(i) = vi.at(min);
        vi.at(min) = tmp;
    }

    for (std::size_t i = 0; i < vi.size(); i++)
    {
        std::cout << vi.at(i) << std::endl;
    }
}