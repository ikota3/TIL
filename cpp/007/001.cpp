int main()
{
    std::vector<int> vi;
    vi.push_back(15);
    vi.push_back(5);

    // 5
    std::cout << vi.at(1) << std::endl;

    // 15
    std::cout << vi.at(0) << std::endl;
}