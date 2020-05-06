void hello(int n);

int main()
{
    int n{};
    std::cin >> n;

    hello(n);
}

void hello(int n)
{
    if (n < 0)
    {
        return;
    }

    int i = 0;
loop:
    if (n != i)
    {
        std::cout << "hello!"s << std::endl;
        i++;
        goto loop;
    }

    std::cout << "End!" << std::endl;
}