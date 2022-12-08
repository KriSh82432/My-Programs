#include <iostream>
using namespace std;

class test{
public:
    test(){
        cout << "First" << endl;
    }
    void display(){
        cout << "Success" << endl;
    }
};

int main(){
    test t1;
    test t2(t1);
    t2.display();
}