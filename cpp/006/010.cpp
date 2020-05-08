void loop();

int main()
{
    loop();
}

void loop()
{
    int x{};
    std::cin >> x;
    if (x == 0)
    {
        return;
    }
    else
    {
        loop();
    }
}