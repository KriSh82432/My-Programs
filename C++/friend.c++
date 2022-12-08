#include <iostream>
using namespace std;

class test{
private:
    int x = 5;
public:
    friend int display(test);
};

int display(test a){
    a.x += 5;
    cout << a.x << endl;
    return a.x;
}

int main(){
    test a1;
    display(a1);
}