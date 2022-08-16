#include <iostream>
#include <iomanip>
using namespace std;

int sum(int x, int y){
    return x + y;
}

int main()
{
    int a, b;
    cout << "Hello World!" << endl;
    cout << "Enter 1st number: ";
    cin >> a ;
    cout << "Enter 2nd number: ";
    cin >> b ;
    cout << "The sum is " << sum(a, b);
    float num1, num2;
    double resnum1, resnum2;
    cin >> num1;
    cin >> num2;
    return 0;
}