int main()
{
    std::cout << 1;

    goto skip;

    std::cout << 2;

skip:
    std::cout << 3;
}