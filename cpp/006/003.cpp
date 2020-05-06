int input()
{
    std::cout << ">"s;
    int x{};
    std::cin >> x;
    return x;
}

int main()
{
    int sum = 0;
loop:
    sum += input();
    std::cout << sum << std::endl;
    goto loop;
}