
void printNumberUntilTen(int n);

using namespace std;

int main()
{
    printNumberUntilTen(1);
}

void printNumberUntilTen(int n)
{
    if (n > 10)
    {
        return;
    }
    else
    {
        cout << n << endl;
        printNumberUntilTen(n + 1);
    }
}