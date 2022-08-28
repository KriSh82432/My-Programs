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
    cout << "\nEnter num1: ";
    cin >> num1;
    cout << "Enter num2: ";
    cin >> num2;
    resnum1 = num1;
    resnum2 = num2;
    cout << std::setprecision(9);
    cout << resnum1 << endl;
    cout << std::setprecision(9);
    cout << resnum2 << endl;
    int x = 3;
    int y = 7;
    int result = x % y;
    cout << result;
    return 0;
}