#include <iostream>
using namespace std;

int main(){
    int age;
    cout << "Enter your age: ";
    cin >> age;
    try
    {
        if(age < 18){
            throw age;
        }
        if(NULL == NULL){
            throw "NULL";
        }
    }
    catch(int age)
    {
        cout << "Your age is small " << age << endl;
    }
    catch(...){
        cout << "NULL error" << endl;
    }
    return 0;
}