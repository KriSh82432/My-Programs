#include <iostream>
using namespace std;
#define MKSTR(x, y) #x #y;
#define concat(a, b) a##b;

int main(){
    cout << MKSTR(Hello Krishna, hello);
    cout << endl;
    int xy = 82;
    string str1 = "Krishna";
    cout << concat(x, y);
    cout << endl;
    cout << concat(str, 1);
    cout << endl;
    return 0;
}