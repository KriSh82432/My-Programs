#include <iomanip>
#include <iostream>
using namespace std;

int main(){
    int arr[10],inp;
    cout << "Enter no. of inputs: " << endl;
    cin >> inp;
    for (int i = 0; i < inp; i++){
        cout << "Enter number" << i + 1 << endl;
        cin >> arr[i];
    }
    cout << "Index" << setw(10) << "Values" << endl;
    for (int i = 0; i < inp; i++)
    {
        cout << setw(3) << i << setw(9) << arr[i] << endl;
    }
    return 0;
}