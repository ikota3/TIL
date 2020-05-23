int main()
{
    int a = 123;
    auto b = 123;

    unsigned int c = 123;
    auto d = 123u;

    std::vector<int> vi;
    vi.push_back(a);
    vi.push_back(b);
    vi.push_back(c);
    vi.push_back(d);

    auto print = [](auto x) {
        std::cout << x << std::endl;
    };

    for (std::size_t i = 0; i < vi.size(); i++)
    {
        print(vi.at(i));
    }
}