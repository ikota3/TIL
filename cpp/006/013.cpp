int solve(int n);

int main()
{
    int num{};
    std::cin >> num;
    std::cout << solve(num) << std::endl;
}

int solve(int n)
{
    int result = 0;
    int i = 1;
    while (n != 0)
    {
        result += n % 10 * i;
        i *= 2;
        n /= 10;
    }

    return result;
}