#include <iostream>
using namespace std;
class Diff
{
    int num;
public:
    friend void operator>>(istream &in, Diff &obj)
    {
        in >> obj.num;
    }
    friend void operator<<(ostream &out, Diff &obj)
    {
        int sum = 0;
        int square = 0;
        int differ = 0;
        for (int i = 1; i <= obj.num; i++){
            sum = sum + i;
        }
        for (int i = 1; i <= obj.num; i++){
            square = square + (i * i);
        }
        differ = (sum*sum) - (square);
        out << differ;
    }
};
int main()
{
    Diff obj;
    cin >> obj;
    cout << obj;
    return 0;
}