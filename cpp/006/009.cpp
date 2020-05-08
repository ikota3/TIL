void hello();

int main()
{
    hello();
}

void hello()
{
    std::cout << "hello"s << std::endl;
    // 自分自身を呼び出す
    hello();
}