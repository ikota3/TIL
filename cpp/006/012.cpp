int input();
void output(int binary);
int convert(int n);
int solve(int n);

int main()
{
    while (true)
    {
        // 底が2の整数を入力
        auto decimal = input();
        // 底が2の整数を底が10の整数に変換する
        auto binary = convert(decimal);
        // 出力
        output(binary);
    }
}

int input()
{
    std::cout << ">";
    int x{};
    std::cin >> x;
    return x;
}

void output(int binary)
{
    std::cout << binary << std::endl;
}

int convert(int n)
{
    if (n > 0)
    {
        return solve(n);
    }
    else
    {
        return -solve(-n);
    }
}

int solve(int n)
{
    /**
     * 底が2の整数を、底が10の整数に変換するには、
     * 右から 2^0 * n[0] + 2^1 * n[1] + 2^2 * n[2] + ... + 2^n * n と計算していき求める。
     * 右に行くにつれて2の倍数となっているので、2の等比数列。
     * 
     * 例えば、111(2) -> 1 + 2*1 + 2*2 = 7(10) となる。
     * これを求めるプロセスは、一番右端を `111 % 10 = 1` を使って求め、
     * 左にある数字らは、右端にある数字を無視して、右にシフトするようにする 111 -> 11。
     * これをするには `111 / 10 = 11` で求める。
     * 右端に行くにつれて、2を掛けることで底が10の整数にすることが出来るので、これに2を掛ける。
     */
    if (n <= 1)
    {
        return n;
    }
    else
    {
        return n % 10 + 2 * solve(n / 10);
    }
}