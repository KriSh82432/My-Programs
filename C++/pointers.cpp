#include <iostream>
using namespace std;

int main(){
    int* ptr;
    int value = 20;
    ptr = &value;
    cout << ptr << endl;
    cout <<value << endl;
    cout << *ptr << endl;
    return 0;
}