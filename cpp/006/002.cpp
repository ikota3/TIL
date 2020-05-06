void hello()
{
    std::cout << "Hello!"s << std::endl;
}

int main()
{
loop:
    hello();
    goto loop;
}
