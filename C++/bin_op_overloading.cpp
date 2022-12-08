#include <iostream>
using namespace std;

class Add{
public:
    int num, result;
    Add(){}
    Add(int x){
        num = x;
    }
    void operator+(Add);
    void display(){
        cout << "Sum" << result << endl;
    }
};

void Add::operator+(Add one){
    result = one.num + num;
    display();
}

int main(){
    Add a1(3);
    Add a2(5);
    a1+a2;
    return 0;
}