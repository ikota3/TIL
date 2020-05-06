int main()
{
    int i = 1;
    while (i < 10)
    {
        int j = 1;
        while (j < 10)
        {
            std::cout << i * j << "\t"s;
            j++;
        }
        std::cout << std::endl;
        i++;
    }
}